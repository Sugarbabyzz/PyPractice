

#****** 5.1 if语句简单实例 ******
# 包含bmw则大写打印，否则首字母大写打印
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#****** 5.2 条件测试******
# 1、是否相等用 == ，考虑大小写
#   若大小写无关紧要，可用.lower()转换成小写比较
# 2、不相等用 !=
# 3、比较符号 =、<、>、<=、>=
# 4、检查多个条件
#   1）使用and检查多个条件
#   条件需要都满足
age_0 = 10
age_1 = 20
if age_0 == 10 and age_1 == 20:
    print("Yes")
#   2)使用or检查多个条件
#   只需满足其中一个条件
if age_0 == 10 or age_1 == 2:
    print("Yes")
# 5、检查特定值是否包含于列表中
print(cars)
if 'bmw' in cars:
    print("Yes")
# 6、检查特定值是否不包含于列表
if 'benz' not in cars:
    print("No")
# 7、布尔表达式
#   布尔的结果要么为True，要么为False。常用于记录条件


#****** 5.3 if语句 ******
# 1、if结构
#   if将执行后面所有缩进的代码行
age = 19
if age >=18:
    print("You are old enough to vote")
# 2、if-else结构
if age >=18:
    print("You are old enough to vote")
else:
    print("Sorry")
# 3、if-elif-else结构
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
# 4、使用多个elif代码块
#    可根据需要使用任意数量的elif代码块
# 5、省略else代码块
#   使用一条elif语句来处理待定的情形更清晰，else是一条包罗万象的语句，可能会引入无效甚至恶意的数据
# **总结**
# 如果只想执行一个代码块，就是用if-elif-else结构;如果要运行多个代码块，就使用一系列独立的if语句

#****** 5.4 使用if语句处理列表 ******
# 1、检查特殊元素
#   在for循环中加入一条if语句来检查特殊值
# 2、确定列表不是空的
#   在if语句中将列表名用在条件表达式中，Python将在列表中至少包含一个元素时返回True
digits4 = []
if digits4:
    print("Exist")
else:
    print("Not exist")
# 3、使用多个列表

#****** 5.5 设置if语句的格式 ******
#PEP8建议 在运算符两边各添加一个空格，如 if age >= 18