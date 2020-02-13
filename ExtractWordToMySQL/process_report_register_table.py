import pymysql
import re
from ExtractWordToMySQL.fields import provinces, operators

'''
处理 report_register_table ，从report_name中解析出业务名称
'''

# 省份+运营商 的组合
list = []
for p in provinces:
    for o in operators:
        list.append(p+o)

# 数据库连接
# db = pymysql.connect(host='192.168.10.231', user='bj', password='bj2016', port=3307, db='assess')
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='process')
cursor_query = db.cursor()  # 查询游标
cursor_update = db.cursor()  # 更新游标

# 解析数据
query_sql = 'SELECT * FROM report_register_table'
# try:
cursor_query.execute(query_sql)
row = cursor_query.fetchone()
while row:
    # 获取报告名称
    report_name = row[2]
    print('Row:', report_name)
    # 解析业务名称逻辑
    business = report_name
    # 1、根据""解析
    match = re.match('(.*)“(.*)”(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 2、根据""解析
    match = re.match('(.*)"(.*)"(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 3、根据[]解析
    match = re.match('(.*)\[(.*)\]\[(.*)\]\[(.*)\](.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(4).strip()
    # 4、根据【】解析
    match = re.match('(.*)【(.*)】【(.*)】【(.*)】(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(4).strip()
    # 5、xxxx-xxxx-xxxx-xx 业务名称 安全评估报告
    match = re.match('(.*?)-(.*?)-(.*?)-\d*(——)?(.*)安全评估报告(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(5).strip()
    # 6、xxxx-xxxx-xxxx-xx-业务名称
    match = re.match('(.*?)-(.*?)-(.*?)-(.*?)-(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(5).strip()
    # 7、*公司 业务名称 互联网新技术新业务|互联网新技术新业务信息安全评估复核报告
    match = re.match('(.*)公司(.*)(互联网新技术新业务|互联网新技术新业务信息安全评估复核报告)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 8、*公司 业务名称 复核
    match = re.match('(.*)公司(.*)复核(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 9、*公司 业务名称 业务信息安全评估(报告)
    match = re.match('(.*)公司(.*)业务信息安全评估(报告)?', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 9、*公司 业务名称 信息安全评估(报告)
    match = re.match('(.*)公司(.*)信息安全评估(报告)?', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 10、山西xx-业务名称
    match = re.match('山西(联通|电信|移动)-(.*)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(2).strip()
    # 11、[浙江][业务名称]业务信息安全评估报告
    match = re.match('\[浙江\]\[(.*)\]业务信息安全评估报告', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(1).strip()
    # 12、省份运营商 业务名称 (安全评估复核报告|信息安全评估报告|新技术新业务评估报告)
    for item in list:
        match = re.match('(.*)' + item + '-?(.*)(安全评估复核报告|信息安全评估报告|新技术新业务评估报告)', report_name, re.S)
        if match is not None and business == report_name:
            business = match.group(2).strip()
    # 13、省份运营商 业务名称 (安全评估报告)
    for item in list:
        match = re.match('(.*)' + item + '(.*)(安全评估报告)', report_name, re.S)
        if match is not None and business == report_name:
            business = match.group(2).strip()
    # 14、省份运营商 业务名称 (评估报告|评估)
    for item in list:
        match = re.match('(.*)' + item + '(.*)(评估报告|评估)(.*)', report_name, re.S)
        if match is not None and business == report_name:
            business = match.group(2).strip()
    # 15、(.*) 省份运营商 业务名称
    for item in list:
        match = re.match('(.*)?' + item + '(.*)(互联网新技术新业务信息)?', report_name, re.S)
        if match is not None and business == report_name:
            business = match.group(2).strip()
    # 16、业务名称 （数据安全合规评估报告|信息安全评估报告）
    match = re.match('(.*)(数据安全合规评估报告|信息安全评估报告|信息安全复评报告)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(1).strip()
    # 17、xxxx-xxxx-xxxx-xx-（业务名称）
    match = re.match('(.*)-(.*?)(（|\()(.*)(）|\))', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(4).strip()
    # 18、业务名称 （安全评估报告）
    match = re.match('(.*)(安全评估报告|复核报告)', report_name, re.S)
    if match is not None and business == report_name:
        business = match.group(1).strip()

    # 更新业务名称到数据库
    try:
        update_sql = "UPDATE report_register_table SET report_business = %s WHERE report_name = %s"
        cursor_update.execute(update_sql, (business, report_name))
        db.commit()
    except:
        db.rollback()
        print('Error')

    # 游标指向下一行
    row = cursor_query.fetchone()
# except:
#     print('except')

db.close()

