

#****** 5.2.1 MYSQL的存储 ******

# 1、安装PyMYSQL
#   MYSQL仅仅是用来存储数据的数据库，提供存储服务
#   若要与Python交互，需要安装Python存储库
#   pip3 install pymysql

# 2、连接数据库
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")

# 3、创建表
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)


# 4、插入数据
#   更改操作都是事务，以下为标准写法
id = '2012001'
user = 'Bob'
age = 20
sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))  # 元组传递数值
    db.commit() # 执行完这句还真正将语句提交到数据库执行
except:
    db.rollback()   # 相当于数据回滚，什么都没有发生过

#   或者用字典实现动态插入
data = {
    'id': '2012002',
    'name': 'Jerry',
    'age': 20
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful!')
        db.commit()
except:
    print('failed')
    db.rollback()


# 5、更新数据
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()

#   去重方法：数据存在，则更新数据；数据不存在，则插入数据
data = {
    'id': '2012003',
    'name': 'Tom',
    'age': 22
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('failed')
    db.rollback()


# 6、删除数据
table = 'students'
condition = 'age < 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


# 7、查询数据
#   查询不需要db.commit()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)    # rowcount获取查询结果的条数
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall() #  注意：调用一次fetchone后，偏移指针指向下一条数据，fetchall返回的就是偏移指针指向的数据一致到结束的所有数据
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

#   推荐用以下方法逐条取数据
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')









db.close()
