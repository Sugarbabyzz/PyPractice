
# Hello world
print("Hello world")

#****** 2.2 变量 ******
# 对同一变量重复赋值，会修改变量内容
message = "Hello world"
print(message)

message = "Change"
print(message)

#****** 2.3 字符串 ******
# 引号括起的都是字符串，单引号双引号都可以

# 2.3.1 使用方法修改字符串的大小写
# title()方法将每个单词的首字母改为大写
name = "ada lovelace"
print(name.title())
# upper()全改为大写
print(name.upper())
# lower()全改为小写
print(name.lower())

# 2.3.2 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello：" + full_name)

# 2.3.3 使用制表符或换行符添加空白
# 制表符 /t
# 换行符 /n
print("language:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
# 含有空白和不含有空白的字符串是完全不同的
# rstrip() 剔除末尾空白
# lstrip() 剔除开头空白
# strip() 同时剔除两端空白
# 剔除函数经常用于存储用户输入前对其进行清理
space = " python "
print(space.rstrip())
print(space.strip())

# 2.3.5 字符串的使用
# 应该在双引号里使用单引号

#****** 2.4 数字 ******
# 用 ** 表示乘方运算
print(3**2)
# 使用str()避免类型错误
age = 23
# print("Happy " + age) 这里python不知道是23还是2和3，需要对其进行函数表示
print("Happy " + str(age))
# python2 中除法运算只包含整数部分，可将其中一个操作数变为浮点数来避免
print(3 / 2)
print(3.0 / 2)
# //表示取整数部分，%表示取余数
print(3 // 2)
print(6 % 4)

#****** 2.5 注释 ******
# 单行注释
'''多行注释
   多行注释'''


#****** 3.1 列表 ******
# 列表，也就是数组
bicycles = [ 'trek', 'cannondale', 'redline', 'specialized']
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



#****** 6.1 字典简单实例 ******
# 字典是一系列键-值对，是动态的
# 每个键都与一个值相关联，可以用键访问与之相关联的值
# 值可以是数字、字符串、列表乃至字典
# 键和值之间用冒号隔开，键-值对之间用逗号隔开
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#****** 6.2 使用字典 ******
# 1、访问字典中的值：需指定字典和放在方括号内的键
print(alien_0['color'])
# 2、添加键-值对：需一次指定自点名、用方括号括起的键和相关联的值
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 3、创建字典
alien_1 = {}
alien_1['color'] = 'green'
print(alien_1)
# 4、修改字典中的值
alien_1['color'] = 'yellow'
print(alien_1)
# 5、删除键-值对
del alien_0['color']
print(alien_0)
# 6、由类似对象组成的字典
#  之前的实例是，字典存储的是一个对象的多种信息，但也可以使用字典来存储众多对象的同一种信息
#  使用多行来定义字典时，后续的键-值对的缩进量与第一个键-值对相同
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    }
print("Sarah`s favorite language is " +
      favorite_languages['sarah'].title() +
      ".")




#****** 6.3 遍历字典 ******
# 1、遍历所有的键-值对
# 字典名和方法items()，返回一个键-值对列表
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():  #key和value不是固定的，可根据实际更换为描述性名称，更易读
    print("\nKey: " + key)
    print("Value: " + value)
# 2、遍历字典中的所有键
# 不需要字典中的值时，可以用方法key()
# 以下两种都可以，相比之下，上面的更易读
for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages:
    print(name.title())
# 3、按顺序遍历字典中的所有键
#  字典明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
#  可使用函数sorted()来获得按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
    print(name.title())
# 4、遍历字典中的所有值
# 用方法values()，返回一个值列表
for language in favorite_languages.values():
    print(language.title())
# 为了剔除重复项，可使用集合（set）
# 通过对包含重复元素的列表调用set()，找出列表中独一无二的元素
for language in set(favorite_languages.values()):
    print(language.title())

#****** 6.4 嵌套 ******
# 嵌套：将一系列字典存储在列表中，或将列表作为值存储在字典中，甚至字典中嵌套字典
# 1、字典列表
#   创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yello', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
#   也可以用range()生成30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#   修改前三个外星人
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['potins'] = 10
#   显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
# 2、在字典中存储列表
#  存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
# 3、在字典中存储字典
#  在网站有多个用户的情况下，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username,user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())



#****** 7.1 函数input()的工作原理 ******
# input()函数让程序暂停运行，等待用户输入一些文本，获取用户输入后，将其存储在一个变量中。
# input()默认将输入解读为字符串。
# msg = input("Tell me something, and I will repeat it back to you: ")
# print(msg)
# 1、对于横跨两个的提示，可以将前半部分存在一个变量中，用运算符+=再存储后半部分。
# 2、用int()来获取数值输入
#   age = input("How old are you ? " )
#   print(age)
#   此时的age是字符串，无法与整数进行比较。
#   为此，可使用函数int()，将其由字符串转换为数值表示。
age = int(age)
#   因此，将数值输入用于计算和比较前，务必将其转换为数值表示 ✅
# 3、求模运算符
#   （%），将两个数相除并返回余数

#****** 7.2 while循环  ******
# while循环不断地运行，直到指定的条件不满足为止
# 1、使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 2、在while循环中，定义一个退出值，用户输入这个值，则退出程序
# 3、使用标志
#   定义一个变量，用于判断整个程序是否处于活动状态
active = True
while active:
    message = 'quit'
    if message == 'quit':
        active = False
    else:
        print(message)
# 4、使用break退出循环
#   可使用break语句，立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何。
while True:     #True即无限循环
    city = 'quit'
    if city == 'quit':
        break
    else:
        print(city)
# 5、在循环中使用continue
#   可使用continue语句，返回到循环开头，并根据条件测试结果决定是否继续执行循环。
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue            # 不执行下面代码了，重新判断条件
    print(current_number)
# 6、避免无限循环

# ****** 7.3 使用while循环来处理列表和字典 ******
#  for循环中不应该修改列表，否则将导致Python难以跟踪其中的元素
#  while循环可以在遍历列表的同时对其进行修改
# 1、在列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# 2、删除包含特定值的所有列表元素
#   remove()方法只能删除列表中的特定值依次，多次删除需要借助while
pets = ['dog', 'cat', 'dog', 'rabbit', 'cat', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
# 3、使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = "John" # input
    response = "Yes" # input
    responses[name] = response

    repeat = 'no' # input
    if repeat == 'no':
        polling_active = False

print("\n---Poll Results---")
for name,response in responses.items():
    print(name + " want " + response)



# ****** 8.1 定义函数 ******
#   实例  用关键字def,在括号内传递参数，后面的缩进行构成函数体
def greet_user():
    print("Hello")
greet_user()
# 1、向函数体传参数
def greet_user(username):
    print("Hello " + username)
greet_user('jesse')
# 2、形参与实参
#   形参：在函数的定义中，括号内的参数，实完成其工作所需的一项信息
#   实参：在调用函数时括号内的参数，时传递给函数的信息

#****** 8.2 传递实参 ******
# 1、位置实参
#   基于实参顺序的关联方式
#   基本方式
# 2、关键字实参
#   传递给函数 名称-值 对。
#   在实参中将名称和值关联起来，传递实参时不会混淆，顺序无关紧要
def sum(a,b):
    print(a+b)
sum(a=3,b=2)
# 3、默认值
#   在调用函数中给形参提供了实参，则使用该实参，否则使用默认值
#   需要在定义函数中，给形参设置默认值
#   可使用位置实参，也可使用关键字实参
def sum2(a,b=5):
    print(a+b)
sum2(2)
# 4、等效的函数调用
#   可混合使用位置实参、关键字实参和默认值
# 5、避免实参错误
#   当提供的实参多余或少于函数完成其工作所需的信息时，将出现实参不匹配的错误

#****** 8.3 返回值 ******
#  使用return语句将值返回到调用函数的代码行
# 1、返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') # 在这里调用函数
print(musician)
# 2、让实参变成可选的
#   有些参数有些对象有，有些没有，可将其设定一个默认值
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')  # 在这里调用函数
print(musician)
# 3、返回字典
#   函数可返回任何类型的值，包括列表和字典等复杂数据结构
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
# 4、结合函数和while循环

#****** 8.4 传递列表 ******
# 示例
def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['Tom', 'John', 'Ty']
greet_user(usernames)
# 1、在函数中修改列表
def copy(uncopyed, copyed):
    while uncopyed:
        current_copy = uncopyed.pop()
        print("Copying " + current_copy)
        copyed.append(current_copy)

def show(copyed):
    for copy in copyed:
        print("Completed: " + copy)
uncopyed = ['qq', 'ww', 'ee']
copyed = []

copy(uncopyed, copyed)
show(copyed)
# 2、禁止函数修改列表
#   若要保留原来的列表，可向函数传递列表的副本，而不影响原件
#   用 切片表示法[:]创建列表的副本
#   除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数
#   避免花时间和内存创建副本，从而提高效率
copy(uncopyed[:], copyed)

#****** 8.5 传递任意数量的实参 ******
# 示例
# 形参名*topping中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这一元组中
# 传递多少实参都可以，都存入元组中
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('green', 'yellow', 'blue')
# 1、结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print("Size: " + str(size))
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'green', 'yellow', 'blue')
# 2、使用任意数量的关键字实参
#   需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息
#   这种情况下，可将函数编写成能够接受任意数量的键-值对，
#   形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的的名称-值对都孔封装到这个字典中
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile['key'] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

#****** 8.6 将函数存储在模块中 ******
#   为了将代码块与主程序分离
#   可以将函数存储在被称为模块的独立文件中，再将模块导入到主程序中
#   import语句循序在当前运行的程序文件中使用模块中的代码
# 1、导入整个模块
#   import让Python打开文件pizza.py，并将其中的所有函数都复制到这个程序中，可使用所有定义了的函数
import pizza
pizza.make_pizza(16, 'green', 'yellow', 'blue')
# 2、导入特定的函数
#   通过逗号分割函数名，可根据需要从模块中导入任意数量的函数
#   用这种语法，调用函数时就无需使用句点
#   import语句中显式地导入了函数
from pizza import make_pizza, build_profile, sum2
sum2(10,2)
# 3、使用as给函数指定别名
#   如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名
#   关键字 as 可将函数重命名为提供的别名
#   下面将函数make_pizza()重命名为mp()
from pizza import make_pizza as mp
mp(16, 'green', 'yellow', 'blue')
# 4、使用as给模块指定别名
import pizza as p
p.make_pizza(16, 'green', 'yellow', 'blue')
# 5、导入模块中的所有函数
#   使用星号（*）运算符可让Python导入模块中的所有函数
#   导入了所有函数，调用函数时无需使用句点
#   注意：并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，会覆盖函数
#   最佳解决：要么只导入需要使用的函数，要么导入整个模块并使用句点表示法
from pizza import *
make_pizza(16, 'green', 'yellow', 'blue')

#****** 8.7 函数编写指南 ******
# 1、应给函数指定描述性名称，且只在其中使用小写字母和下划线
# 2、每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式
# 3、给形参指定默认值时，等号两边不要有空格
# 4、函数调用中的关键字实参，也应该遵循这种规律
# 5、PEP8要求代码行不超过79字符
# 6、如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
# 7、import语句应放在文件开头




#****** 9.1 创建和使用类 ******
# 1、创建Dog类
class Dog():

    def __init__(self, name, age):
        # 初始化属性name和age
        # 开头和末尾各有两个下划线，这是一个特殊的方法：
        # 每当根据Dog类创建新实例时，Python都会自动运行它
        # 形参self时必不可少的，还必须位于其他形参的前面
        # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
        # 每当我们根据Dog类创建实例时，都只需给出最后两个形参（name和age）提供至，而不需要传递self，它会自动传递
        self.name = name
        self.age = age

    def sit(self):
        # 方法：蹲下
        # 不需要传递额外的参数，self自动传递
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 方法：打滚
        print(self.name.title() + " is rolled over!")
# 2、根据类创建实例
#   并未显式的包含return语句，但自动返回一个表示这条小狗的实例
#   命名规则：首字母大写的名称一般指类
#   访问属性和方法：可使用句点表示法，指定实例的名称和要访问的属性或调用的方法
my_dog = Dog('willie', 6)
print("My dog`s name is " + my_dog.name + ", age is " + str(my_dog.age))

#****** 9.2 使用类和实例 ******
#   可以直接修改实例的属性，也可以编写方法以特定的方式进行修改
# 1、创建Car类
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):     # 通过方法修改属性的值
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('Audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 2、给属性指定默认值
# 在_init_中设定，如上
print(my_new_car.odometer_reading)
# 3、修改属性的值
#   1）直接修改属性的值
my_new_car.odometer_reading = 23
print(my_new_car.odometer_reading)
#   2）通过方法修改属性的值
my_new_car.update_odometer(40)
print(my_new_car.odometer_reading)
#   3）通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
print(my_new_car.odometer_reading)

#****** 9.3 继承 ******
#   一个类继承另一个类时，将自动获得另一个类的所有属性和方法
#   原有的类成为父类，而新类成为子类
#   子类继承了其父类所有属性和方法，同时还可以定义自己的属性和方法
#   创建子类时，父类必须包含在当前文件中，且位于子类前面
# 1、子类的方法_init_()
#   创建子类的实例时，Python首先需要完成的任务时给父类的所有属性赋值
#   在Car类基础上创建ElectricCar类
#   super()是一个特殊函数，将父类和子类关联起来
#   super调用了父类的_init_()方法，让ElectricCar实例包含父类的所有属性
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size =70   # 定义子类的属性

    def describle_battery(self):    # 定义子类的方法
        print("This car has s " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 2、给子类定义属性和方法
my_tesla.describle_battery()
# 3、重写父类的方法
#   在执行父类子类同名方法时，Python将忽略父类中的方法，而执行子类中的方法
# 4、将实例用作属性




#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******


















