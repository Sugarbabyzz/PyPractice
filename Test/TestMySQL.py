import pymysql


db = pymysql.connect("localhost", "root", "123456", "rent")
cursor = db.cursor()

city = '北京'
title = '啦啦啦'
sql = 'INSERT INTO test(city, title) values (%s, %s)'

try:
    cursor.execute(sql, (city, title))
    db.commit()
    print('插入成功')
except:
    db.rollback()
    print('失败')

db.close()

# import pymysql
#
# db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
# cursor = db.cursor()
#
# id = '2012001'
# user = 'Bob'
# age = 20
# sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))  # 元组传递数值
#     db.commit() # 执行完这句还真正将语句提交到数据库执行
#     print('成功')
# except:
#     db.rollback()   # 相当于数据回滚，什么都没有发生过
#     print('失败')