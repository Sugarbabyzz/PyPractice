import pandas as pd
from sqlalchemy import create_engine
import pymysql
from ExtractWordToMySQL.fields import host, database, user, password, port

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/process')
db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
cursor = db.cursor()


#  处理 评估专家推荐表.xlsx
def process_expert_recom_table(filepath):
    columns = ['name', 'province', 'recom_level', 'more_than_twice', 'cisp_number', 'other_cert', 'work_years',
               'recom_reason']
    data = pd.read_excel(filepath, names=columns)
    data.to_sql('expert_recom_table', con=engine, if_exists='append', index=False)


#  处理 评估报告登记表.xlsx
def process_report_register_table(filepath):
    columns = ['assess_time', 'report_name', 'category', 'intro', 'user_scale', 'risk_points',
               'assessor', 'project_province', 'assessor_province', 'counterpart']
    data = pd.read_excel(filepath, names=columns)
    data.to_sql('report_register_table', con=engine, if_exists='append', index=False)


if __name__ == '__main__':

    # 1、处理  评估专家推荐表（新疆）.xlsx
    filepath_xj = 'data/评估专家推荐表/评估专家推荐表.xlsx'
    process_expert_recom_table(filepath_xj)

    # 2、处理  评估报告登记表（重庆）.xlsx
    filepath_cq = 'data/评估报告登记表/评估报告登记表.xlsx'
    process_report_register_table(filepath_cq)










