

#****** 3.1 列表 ******
# 列表
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
# 这个是字典哟 dict = {'name': 'hello', 'age': 'world'}
print(bicycles)
# python列表下标是从0开始的
print(bicycles[0])
print(bicycles[0].title())
# 访问列表最后一个元素，将索引指定为-1；访问倒数第二个，为-2
print(bicycles[-1])

#****** 3.2 对列表修改、添加和删除 ******
# 1、修改
bicycles[0] = 'honda'
print(bicycles)
# 2、添加
# append()函数在列表末尾添加元素
bicycles.append('ducati')
print(bicycles)
# 3、插入
# insert()函数在列表任何位置添加新元素，需要指定新元素的索引和值
bicycles.insert(0, 'yamaha')
print(bicycles)
# 4、删除
# 1）使用del语句删除元素 （需要知道索引）
del bicycles[0]
print(bicycles)
# 2）使用pop()方法删除元素
#   将列表末尾的元素弹出，获取值继续使用
#   也可以指定任意位置，在括号中指出
popped_bicycles = bicycles.pop()
print(bicycles)
print(popped_bicycles)
popped_bicycles2 = bicycles.pop(2)
print(bicycles)
print(popped_bicycles2)
# 3）根据值删除元素  （需要知道元素的值）
bicycles.remove('honda')
print(bicycles)

#****** 3.3 组织列表 ******
# 1、使用sort()方法对列表进行永久性排序
# 传入 reverse=True 参数，实现逆序排序
# 该排序是永久性的
numbers = ['1', '50', '2', '99', '33']
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# 2、使用sorted()方法对列表进行临时排序
# 临时排序：保留序列原本的序列，同时以特定的形式呈现
numbers2 = ['1', '50', '2', '99', '33']
print("Original list: ")
print(numbers2)
print("Sorted list : ")
print(sorted(numbers2))
print("Again original list: ")
print(numbers2)
# 3、反转列表元素
# reverse()方法
numbers2.reverse()
print(numbers2)
# 4、获取列表长度
# len()方法，计算元素数时从1开始
print(len(numbers2))

#****** 3.4 避免列表索引错误 ******
'''Python的列表索引是从0开始的，索引不存在的位置会报错'''



#****** 4.1 遍历整个列表 ******
# 利用 for 循环遍历列表
# 将列表中的元素存储在变量magician中，依次打印
# 单数复数的命名形式规范
# 对于缩进了的每趟都执行一遍，未缩进的代码只执行一次
magicians =['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can`t wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#****** 4.2 避免缩进错误 ******
# python中利用缩进判断代码行与前一个代码行的关系
# 1、缩进的代码才能包含于之前的循环体中
# 2、要避免不必要的缩进，会报错
# msg = "Hello world"
#     print(msg)    这种写法是错误的，print并不包含于上一条代码
# 3、不要遗漏了冒号

#****** 4.3 创建数字列表 ******
# 1、使用函数range()
# range()函数能够轻松地生成一系列的数字
# 但不会打印最后一个数字，有必要的话需要+1或-1
for value in range(1,4):
    print(value)
# 2、使用range()创建数字列表
# 可使用函数list()将range()的结果直接转换为列表。
numbers3 = list(range(1,6))
print(numbers3)
# 使用range()函数，还可以指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)
# Eg. 将前10个整数的平方加入到一个列表中
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
# 3、对数字列表执行简单的统计计算
#   1）求最大值
digits = [1,2,3,4,5]
print(max(digits))
#   2）求最小值
print(min(digits))
#   3）求总和
print(sum(digits))
# 4、列表解析
# 将for循环和创建新元素的代码合并成一行，并自动附加新元素
# ①指定一个描述性列表名  ②指定左方括号，定义表达式，用于生成存储到列表的值
# ③编写for循环，为列表提供值  ④加上右方括号
squares2 = [value**2 for value in range(1,11)]
print(squares2)

#****** 4.4 使用列表的一部分 ******
# 1、切片
# 和range一样，需要给出第一个数和最后一个数+1
# 索引从0开始
print(digits)
print(digits[1:3]) #只打印digits列表中前两个元素
print(digits[:3])  #如果未给出第一个元素索引，则默认从列表开头提取
print(digits[0:])  #如果未给出末尾元素索引，则遍历到末尾
print(digits[-3:]) #打印倒数三个元素
# 2、遍历切片
# 3、复制列表
#   即创建一个始于第一个元素，终止于最后一个元素的切片
digits2 = ['1','2','3','5']
digits3 = digits2[:]
print(digits2)
print(digits3)
digits3.append('666')   #证明digits2与digits3是不同的列表
print(digits2)
print(digits3)
# ❌错误示范
# 这种相当于指针，指向了同一列表，同时变化
digits3 = digits2

#****** 4.5 元组 ******
# 列表--可以修改，适合用于存储在程序运行期间可能变化的数据集
# 元组--不能修改，如果需要存储一组值在程序的整个生命周期内不变，可使用元组
# 1、定义元组
#   使用圆括号而非方括号来标识
dimensions = (200, 50)
print(dimensions[0])
# 2、遍历元组
for dimension in dimensions:
    print(dimension)
# 3、修改元组变量
#   修改元祖的元素会报错，但是可以给存储元组的变量赋值
#   即重新定义整个元组
dimensions = (250, 20)
for dimension in dimensions:
    print(dimension)

#****** 4.6 设置代码格式 ******
# 1、用空格代替制表符，一个制表符=四个空格
# 2、行长不超过79字符
# 3、PEP8规范

