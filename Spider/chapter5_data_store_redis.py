

#****** 5.2.3 Redis存储 ******
# Redis是一个基于内存的高效的键值型非关系型数据库。

# 1、安装Redis及redis-py库，要做数据导入/导出操作，还需要RedisDump

# 2、redis-py提供Redis和StrictRedis库
#    推荐使用StrictRedis库

# 3、连接Redis
#   1)使用StrictRedis连接
from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')
#   调用set()方法，设置一个键值对，然后获取并打印
redis.set('name', 'Bob')
print(redis.get('name'))

#   2）使用ConnectionPool连接
from redis import ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0, password='123456')
redis = StrictRedis(connection_pool=pool)
#   3）使用URL连接
