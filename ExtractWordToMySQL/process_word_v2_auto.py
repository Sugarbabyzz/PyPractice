import os
import docx
import re
import pymysql
import datetime
from ExtractWordToMySQL.fields import host, database, user, password, port, provinces, chapter_number_map

# 初始化数据库连接
db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
cursor = db.cursor()


#  存入数据库 字典格式  in (表名，字典）
def store_to_db(table_name, dic):
    keys = ','.join(dic.keys())
    values = ','.join(['%s'] * len(dic))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table_name, keys=keys, values=values)
    cursor.execute(sql, tuple(dic.values()))
    db.commit()


#  提取表格内容，并存入数据库  in （docx中的表，报告编号，报告名称，flag=表类型）
def extra_from_table(table, doc_number, filename, flag):
    for row in table.rows[1:]:
        extra_result_dict = {}
        extra_result_dict['doc_name'] = filename
        extra_result_dict['doc_number'] = doc_number
        extra_result_dict['type'] = row.cells[0].text.replace('\n', '')
        extra_result_dict['number'] = row.cells[1].text
        extra_result_dict['assess_points'] = row.cells[2].text
        extra_result_dict['assessment'] = row.cells[3].text
        if len(row.cells) == 5:  # 表格多一个 评估记录 的情况
            extra_result_dict['assess_record'] = row.cells[4].text

        # for k, v in extra_result_dict.items():
        #     print(k + ':  ' + v)
        # print()

        # 将结果存入数据库
        if flag == 'risk':
            store_to_db('risk_analysis_table', extra_result_dict)
        elif flag == 'ensure':
            store_to_db('ensure_analysis_table', extra_result_dict)


#  解析 评估报告
def process_word_report(filepath, filename):
    # 读取文档
    try:
        docx_file = docx.Document(filepath)
    except:
        print('can`t open ' + filepath + ' ！！！')

    # 处理文档内容
    # 1、解析并存储 报告基本信息 （报告编号、省份、年份）
    content, province = '', ''
    for para in docx_file.paragraphs[:20]:  # 读前20行即可获取基本信息
        content = content + '\n' + para.text

    # doc_number
    match = re.match('(.*)(报告编号：|报告编号:)(.*?)(\s)(.*)', content, re.S)
    doc_number = match.group(3).strip() if match is not None else ''
    # year
    match = re.match('(.*)(\d{4})(\s*)年', content, re.S)
    year = match.group(2).strip() if match is not None else ''
    year = doc_number[:4] if doc_number != '' else year
    # province
    for prov in provinces:
        if prov in content or prov in filename:
            province = prov

    info_dict = {}
    info_dict['report_number'] = doc_number
    info_dict['report_name'] = filename
    info_dict['report_year'] = year
    info_dict['report_province'] = province
    # 存入数据库
    store_to_db('assess_report_info', info_dict)

    # 查看存储结果 （调试）
    print('-——————————————————-——————————————————-——————————————————-——————————————————-——————————————————-———————————')
    print('-————-————' + filepath + '-————-————')  # 打印当前处理报告的路径
    print('-————-————' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '-————-————')  # 打印当前时间
    for k, v in info_dict.items():
        print(k + ': ' + v)

    # 2、解析并存储 报告子章节内容
    flag = 0
    content = ''
    content_dict = {}
    for p in docx_file.paragraphs:
        if p.style.name == 'Heading 1' or p.style.name == 'Heading 2' or '标题' in p.style.name:
            if flag == 0:
                flag = 1
            else:
                content_dict[chapter] = content
                content = ''
            chapter = p.text
        else:
            # if p.style.name == 'Normal' and flag == 1:
            if p.style.name != 'Heading 1' and p.style.name != 'Heading 2' and '标题' not in p.style.name and flag == 1:
                content = content + '\n' + p.text
    content_dict[chapter] = content

    # 存入数据库
    for k, v in content_dict.items():
        # print('--------------------------------------------')
        result_dict = {}
        result_dict['report_number'] = doc_number
        result_dict['report_name'] = filename
        result_dict['chapter'] = ''.join(re.findall('[^\d\.?\d*\s]', k)).strip() if re.findall('[^\d\.?\d*\s]', k) else ''
        result_dict['chapter_number'] = re.findall('\d\.?\d*', k)[0].strip() if re.findall('\d\.?\d*', k) else ''
        for key, value in chapter_number_map.items():
            if key in k:
                result_dict['chapter_number'] = chapter_number_map.get(key)
        result_dict['content'] = v.strip()

        # for key, value in result_dict.items():
        #     print(key + ': ' + value)

        # 将结果存入数据库
        store_to_db('assess_report_content', result_dict)

    # 3、解析并存储 表格
    # 首先确定 风险分析表 risk_analysis_table 和 保障能力分析表 ensure_analysis_table
    risk_analysis_table, ensure_analysis_table = '', ''
    for table in docx_file.tables:
        cell = table.rows[0].cells[0]
        if cell.text == '风险类型':
            risk_analysis_table = table
        elif cell.text == '保障能力类型':
            ensure_analysis_table = table
    # 提取并存储 风险分析表 和 保障能力分析表
    if risk_analysis_table != '':
        extra_from_table(risk_analysis_table, doc_number, filename, flag='risk')
    if ensure_analysis_table != '':
        extra_from_table(ensure_analysis_table, doc_number, filename, flag='ensure')


if __name__ == '__main__':

    # 处理  评估报告
    rootpath = 'data/评估报告/待处理'
    for dirname in os.listdir(rootpath):
        dirpath = rootpath + '/' + dirname
        for filename in os.listdir(dirpath):
            filepath = dirpath + '/' + filename
            # 默认是docx文件，如果是doc需要先转成docx
            process_word_report(filepath, filename[:-5])










