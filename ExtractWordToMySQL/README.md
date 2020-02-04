- - - 
### fields.py
存储常量字段。

- - - 
### process_combine.py
处理 <评估专家推荐表> 和 <评估报告登记表> 的合并。

- - - 
### process_table.py
将合并好的 <评估专家推荐表> 和 <评估报告登记表> 导入数据库。 

- - - 
### process_word_v1_regex.py
正则匹配方法。 \
缺点：效率低，设置规则复杂，所以暂不使用。

- - - 
### process_word_v2_auto.py
自动识别方法。 \
只能解析docx文件（可以手动重命名） \
自动识别标题，并获取章节内容。\
优点：高效。\
缺点：格式不标准的word还需要手动调整。（没辙） 









数据存在231服务器上。
数据库 assess。

assess_report_info表：评估报告基本信息 \
assess_report_content表：评估报告内容 \
risk_analysis_table表：评估报告中的安全风险分析表 \
ensure_analysis_table表：评估报告中的安全保障能力分析表 \
expert_recom_table表：评估专家推荐表 \
report_register_table表：评估报告登记表 



- - - 
