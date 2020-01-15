import pandas as pd
import os
from sqlalchemy import create_engine
import docx
import re
import pymysql
from ProcessDataToMySQL.fields import match_list
from ProcessDataToMySQL.fields import fields_map
from ProcessDataToMySQL.fields import host, database, user, password, port


filepath = 'data/'
dirList = os.listdir(filepath)
for file in dirList:
    print(file)
print()

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/process')

'''存储 评估专家推荐表（新疆）.xlsx'''
# print('评估专家推荐表（新疆）.xlsx  Processing')
# columns = ['name', 'province', 'recom_level', 'more_than_twice', 'cisp_number', 'other_cert', 'work_years', 'recom_reason']
# data = pd.read_excel('data/评估专家推荐表（新疆）.xlsx', names=columns)
# data.to_sql('pgzjtjb_xj', con=engine, if_exists='append', index=False)
# print('评估专家推荐表（新疆）.xlsx  Done')


'''存储 评估报告登记表（重庆）.xlsx'''
# print('评估报告登记表（重庆）.xlsx  Processing')
# columns = ['assess_report_time', 'assess_report_title', 'category', 'intro', 'user_scale', 'risk_points', 'assessor',
#            'project_province', 'assessor_province', 'counterpart']
# data = pd.read_excel('data/评估报告登记表（重庆）.xlsx', names=columns)
# data['assess_report_time'] = data.loc[:, 'assess_report_time'].apply(lambda x: x.strftime('%Y-%m-%d'))
# data.to_sql('pgbgdjb_cq', con=engine, if_exists='append', index=False)
# print('评估报告登记表（重庆）.xlsx  Done')

'''存储 江西评估报告'''
# 初始化数据库连接
db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
cursor = db.cursor()

# 读取文档
try:
    docx_file = docx.Document('data/jiangxi.docx')
except:
    print('can`t open docx ')

# 获取文档内容
# docx_para = docx_file.paragraphs
# content = ''  # 存储word中的文字内容
# for para in docx_para:
#     content = content + '\n' + para.text
# # print(content)
# # 1、处理内容
# # 提取文档中子标题下的内容
# result_dict = {}
# for item in match_list:
#     # 暂不处理 附件
#     if item[0] == '(报告编号：|报告编号:)':
#         match = re.match('(.*)' + item[0] + '(.*?)' + item[1] + '(.*)', content, re.S)
#     elif item[0] == '(6安全评估结论意见|6 安全评估结论意见)':
#         match = re.match('(.*)' + item[0] + '\s(.*?)(\s)', content, re.S)
#     else:
#         match = re.match('(.*)' + item[0] + '(.*)' + item[1] + '(.*)', content, re.S)
#     result_dict[fields_map.get(item[0])] = match.group(3).strip()
#
# # 查看存储结果
# for k, v in result_dict.items():
#     print(k + ': \n' + v)
#     print('------------------------------------')
#
# # 将结果存入数据库
# table = 'assess_report'
# keys = ','.join(result_dict.keys())
# values = ','.join(['%s'] * len(result_dict))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# cursor.execute(sql, tuple(result_dict.values()))
# db.commit()


# 2、处理表格

table_list = []
t = docx_file.tables[1]
for i, row in enumerate(t.rows):
    row_content = []
    for cell in row.cells:  # 读一行中每个单元格
        c = cell.text.replace('\n', '')
        row_content.append(c)
    table_list.append(row_content)

print(table_list)
# 首先确定 风险分析表 risk_analysis_table 和 保障能力分析表 ensure_analysis_table
for table in docx_file.tables:
    row = table.rows[0]
    cell = row.cells[0]
    if cell.text == '风险类型':
        risk_analysis_table = table
    elif cell.text == '保障能力类型':
        ensure_analysis_table = table
print('--------')
# 提取 风险分析表
# risk_result_dict = {}
# for row in risk_analysis_table.rows[1:]:
#     risk_result_dict['risk_type'] = row.cells[0].text.replace('\n', '')
#     risk_result_dict['risk_number'] = row.cells[1].text
#     risk_result_dict['risk_assess_points'] = row.cells[2].text
#     risk_result_dict['assessment'] = row.cells[3].text
#     for k, v in risk_result_dict.items():
#         print(k + ':  ' + v)
#     # 将结果存入数据库
#     risk_table = 'risk_analysis_table'
#     keys = ','.join(risk_result_dict.keys())
#     values = ','.join(['%s'] * len(risk_result_dict))
#     sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=risk_table, keys=keys, values=values)
#     cursor.execute(sql, tuple(risk_result_dict.values()))
#     db.commit()

# 提取 保障能力分析表
ensure_result_dict = {}
for row in ensure_analysis_table.rows[1:]:
    ensure_result_dict['ensure_type'] = row.cells[0].text.replace('\n', '')
    ensure_result_dict['ensure_number'] = row.cells[1].text
    ensure_result_dict['ensure_assess_points'] = row.cells[2].text
    ensure_result_dict['assessment'] = row.cells[3].text
    for k, v in ensure_result_dict.items():
        print(k + ':  ' + v)
    print()
    # 将结果存入数据库
    ensure_table = 'ensure_analysis_table'
    keys = ','.join(ensure_result_dict.keys())
    values = ','.join(['%s'] * len(ensure_result_dict))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=ensure_table, keys=keys, values=values)
    cursor.execute(sql, tuple(ensure_result_dict.values()))
    db.commit()























