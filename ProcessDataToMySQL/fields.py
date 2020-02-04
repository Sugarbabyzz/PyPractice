# 年份、省份
provinces = ['江西', '江苏', '上海', '重庆']

# db
host = 'localhost'
database = 'process'
user = 'root'
password = '123456'
port = 3306

'''
    v1 -    2017年江苏移动
            2017年江西移动
            2018江西移动15个报告
            2018年江西联通
            重庆电信2018年8月
            上海联通2017年
            其他 - 江西省一保通医联万家业务信息安全评估报告
            网约车 - 江南出行平台业务信息安全评估报告
            
    v2 -    网约车 - 江西幸福汽车服务有限公司幸福专车业务信息安全评估报告20181101
            网约车 - 江西易至智行汽车运营服务有限公司20190805
            网约车 - 联途出行信息安全评估报告
'''
# 数据库字段映射   （2017，2018）
# fields_map_v1 = {
#     '(报告编号：|报告编号:)': 'report_number',
#     '(1.1\s?业务名称)': '1_1_name',
#     '(1.2\s?业务功能介绍)': '1_2_func',
#     '(1.3\s?技术实现方式介绍)': '1_3_tech',
#     '(1.4\s?（预期）用户规模)': '1_4_user_scale',
#     '(1.5\s?市场发展情况)': '1_5_market_status',
#     '(2.1\s?安全评估情况概述)': '2_1_assess_intro',
#     '(2.2\s?评估人员组成)': '2_2_assess_member',
#     '(2.3\s?评估实施流程)': '2_3_assess_flow',
#     '(3.1\s?安全风险分析表)': '3_1_risk_aly_table',
#     '(3.2\s?风险说明)': '3_2_risk_state',
#     '(4.1\s?日常安全管理介绍)': '4_1_safe_manage',
#     '(4.2\s?应急管理措施介绍)': '4_2_emergency',
#     '(4.3\s?安全保障能力分析表)': '4_3_safe_aly_table',
#     '(4.4\s?安全保障能力说明)': '4_4_safe_asr_state',
#     '(5.1\s?信息安全管理风险评估结果)': '5_1_info_manage_safe',
#     '(5.2\s?信息内容安全风险评估结果)': '5_2_info_safe',
#     '(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)': '5_3_user_or_plat_safe',
#     '(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)': '5_4_plat_or_run_safe',
#     '(6\s?安全评估结论意见)': '6_conclusion'
# }

fields_map_v1 = {
    '(1.1\s?业务名称)': ['业务名称', '1.1'],
    '(1.2\s?业务功能介绍)': ['业务功能介绍', '1.2'],
    '(1.3\s?技术实现方式介绍)': ['技术实现方式介绍', '1.3'],
    '(1.4\s?（预期）用户规模)': ['（预期）用户规模', '1.4'],
    '(1.5\s?市场发展情况)': ['市场发展情况', '1.5'],
    '(2.1\s?安全评估情况概述)': ['安全评估情况概述', '2.1'],
    '(2.2\s?评估人员组成)': ['评估人员组成', '2.2'],
    '(2.3\s?评估实施流程)': ['评估实施流程', '2.3'],
    '(3.1\s?安全风险分析表)': ['安全风险分析表', '3.1'],
    '(3.2\s?风险说明)': ['风险说明', '3.2'],
    '(4.1\s?日常安全管理介绍)': ['日常安全管理介绍', '4.1'],
    '(4.2\s?应急管理措施介绍)': ['应急管理措施介绍', '4.2'],
    '(4.3\s?安全保障能力分析表)': ['安全保障能力分析表', '4.3'],
    '(4.4\s?安全保障能力说明)': ['安全保障能力说明', '4.4'],
    '(5.1\s?信息安全管理风险评估结果)': ['信息安全管理风险评估结果', '5.1'],
    '(5.2\s?信息内容安全风险评估结果)': ['信息内容安全风险评估结果', '5.2'],
    '(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)': ['用户信息安全风险评估结果_or_业务平台安全风险评估结果', '5.3'],
    '(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)': ['业务平台安全风险评估结果_or_业务运行安全风险评估结果', '5.4'],
    '(6\s?安全评估结论意见)': ['安全评估结论意见', '6']
}

# 文档提取规则    （2017，2018）
match_list_v1 = [
    ['(1.1\s?业务名称)', '(1.2\s?业务功能介绍)'],
    ['(1.2\s?业务功能介绍)', '(1.3\s?技术实现方式介绍)'],
    ['(1.3\s?技术实现方式介绍)', '(1.4\s?（预期）用户规模)'],
    ['(1.4\s?（预期）用户规模)', '(1.5\s?市场发展情况)'],
    ['(1.5\s?市场发展情况)', '(2\s?安全评估情况)'],
    ['(2.1\s?安全评估情况概述)', '(2.2\s?评估人员组成)'],
    ['(2.2\s?评估人员组成)', '(2.3\s?评估实施流程)'],
    ['(2.3\s?评估实施流程)', '(3\s?业务安全风险分析)'],
    ['(3.1\s?安全风险分析表)', '(3.2\s?风险说明)'],
    ['(3.2\s?风险说明)', '(4\s?配套安全管理措施)'],
    ['(4.1\s?日常安全管理介绍)', '(4.2\s?应急管理措施介绍)'],
    ['(4.2\s?应急管理措施介绍)', '(4.3\s?安全保障能力分析表)'],
    ['(4.3\s?安全保障能力分析表)', '(4.4\s?安全保障能力说明)'],
    ['(4.4\s?安全保障能力说明)', '(5\s?评估结果|5\s?评估结果及整改建议)'],
    ['(5.1\s?信息安全管理风险评估结果)', '(5.2\s?信息内容安全风险评估结果|5.4\s?业务平台安全风险评估结果)'],  # 2017江苏
    ['(5.2\s?信息内容安全风险评估结果)', '(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)'],  # 2018
    ['(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)', '(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)'],
    ['(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)', '(6\s?安全评估结论意见|5.5\s?匹配性控制分析)'],  # 2018重庆
    ['(6\s?安全评估结论意见)', '\s'],
    # ['(附件)', '']   # 附件未处理
]


# 数据库字段映射   （网约车）
fields_map_v2 = {
    '(报告编号：|报告编号:)': 'report_number',
    '(1.1\s?业务名称)': '1_1_name',
    '(1.2\s?业务功能介绍)': '1_2_func',
    '(1.3\s?技术实现方式介绍)': '1_3_tech',
    '(1.4\s?（预期）用户规模)': '1_4_user_scale',
    '(1.5\s?市场发展情况)': '1_5_market_status',
    '(2.1\s?安全评估情况概述)': '2_1_assess_intro',
    '(2.2\s?评估实施流程)': '2_2_assess_member_or_flow',
    '(3.1\s?安全风险分析表)': '3_1_risk_aly_table',
    '(3.2\s?风险说明)': '3_2_risk_state',
    '(4.1\s?日常安全管理介绍)': '4_1_safe_manage',
    '(4.2\s?应急管理措施介绍)': '4_2_emergency',
    '(4.3\s?安全保障能力分析表)': '4_3_safe_aly_table',
    '(4.4\s?安全保障能力说明)': '4_4_safe_asr_state',
    '(5.1\s?信息安全管理风险评估结果)': '5_1_info_manage_safe',
    '(5.2\s?信息内容安全风险评估结果)': '5_2_info_safe',
    '(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)': '5_3_user_or_plat_safe',
    '(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)': '5_4_plat_or_run_safe',
    '(6\s?安全评估结论意见)': '6_conclusion',
    '(7\s?整改情况及及复核结论)': '7_recheck_conclusion'
}

# 文档提取规则   （网约车）
match_list_v2 = [
    ['(报告编号：|报告编号:)', '(\s)'],
    ['(1.1\s?业务名称)', '(1.2\s?业务功能介绍)'],
    ['(1.2\s?业务功能介绍)', '(1.3\s?技术实现方式介绍)'],
    ['(1.3\s?技术实现方式介绍)', '(1.4\s?（预期）用户规模)'],
    ['(1.4\s?（预期）用户规模)', '(1.5\s?市场发展情况)'],
    ['(1.5\s?市场发展情况)', '(2\s?安全评估情况)'],
    ['(2.1\s?安全评估情况概述)', '(2.2\s?评估实施流程)'],
    ['(2.2\s?评估实施流程)', '(3\s?业务安全风险分析)'],
    ['(3.1\s?安全风险分析表)', '(3.2\s?风险说明)'],
    ['(3.2\s?风险说明)', '(4\s?配套安全管理措施)'],
    ['(4.1\s?日常安全管理介绍)', '(4.2\s?应急管理措施介绍)'],
    ['(4.2\s?应急管理措施介绍)', '(4.3\s?安全保障能力分析表)'],
    ['(4.3\s?安全保障能力分析表)', '(4.4\s?安全保障能力说明)'],
    ['(4.4\s?安全保障能力说明)', '(5\s?评估结果|5\s?评估结果及整改建议)'],
    ['(5.1\s?信息安全管理风险评估结果)', '(5.2\s?信息内容安全风险评估结果|5.4\s?业务平台安全风险评估结果)'],  # 2017江苏
    ['(5.2\s?信息内容安全风险评估结果)', '(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)'],  # 2018
    ['(5.3\s?用户信息安全风险评估结果|5.3\s?业务平台安全风险评估结果)', '(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)'],
    ['(5.4\s?业务平台安全风险评估结果|5.4\s?业务运行安全风险评估结果)', '(6\s?安全评估结论意见|5.5\s?匹配性控制分析)'],  # 2018重庆
    ['(6\s?安全评估结论意见)', '(7\s?整改情况及及复核结论)'],
    ['(7\s?整改情况及及复核结论)', '\s'],
    # ['(附件)', '']   # 附件未处理
]