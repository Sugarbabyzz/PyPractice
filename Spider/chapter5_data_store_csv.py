

#****** 5.1.3 CSV文件存储 ******

#   其文件以纯文本形式存储表格数据，可以由任意数目的记录组成，记录间以某种换行符分隔，最常见的是逗号或制表符。

# 1、写入

import csv

#   默认分隔符为逗号
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '21'])

#   delimiter参数，以空格分隔
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '21'])

#   调用writerows写入多行
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', '20'], ['10002', 'Bob', '22'], ['10003', 'Jordan', '21']])

#   字典方式写入
with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '21'])

