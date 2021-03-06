

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
url = 'redis://:123456@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)

# 4、键操作

# 5、字符串操作

# 6、列表操作

# 7、集合操作

# 8、有序集合操作

# 9、散列操作

# 10、RedisDump

#   1）redis-dump用于导出数据
#   终端导出命令：redis_dump -u :123456@localhost:6379
#   其他的看书P231吧

#   2）redis-load用于导入数据

