

#****** 5.3 MongoDB ******

# 1、安装
#   MongoDb、 PyMongo

# 2、连接
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# 3、指定数据库
db = client.test

# 4、指定集合
collection = db.students

# 5、插入数据
# insert_one() and insert_many()
student = {
    'id': '20170101',
    'name': 'Lili',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)

student1 = {
    'id': '20170202',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170303',
    'name': 'Mike',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)

# 6、查询
#   find_one() and find()

result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)

results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)

#   加上大于20的条件
#   比较符号见书P217
results = collection.find({'age': {'$gt': 20}})
#   正则匹配
#   功能符号见书P218
results = collection.find({'name': {'$regex': '^M.*'}})

# 7、计数
#   count()
count = collection.find().count()
print(count)

count = collection.find({'age': 20}).count()
print(count)

# 8、排序
#   sort()
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 9、偏移
#   skip()偏移几个位置
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

#   limit()截取
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

#   大量数据时，偏移量大会导致内存溢出，最好记录好上次查询的_id
from bson.objectid import ObjectId
collection.find({'_id': {'$gt': ObjectId('21321dsafda232fdsa')}})

# 10、更新
#   update()
condition = {'name': 'Lili'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})
print(result)

# 11、删除

result = collection.delete_one({'name': 'Jordan'})
print(result)
result = collection.delete_many({'age': {'$lt': 25}})

