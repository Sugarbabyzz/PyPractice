

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
        # self.battery = Battery()

    def describle_battery(self):    # 定义子类的方法
        print("This car has s " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 2、给子类定义属性和方法
my_tesla.describle_battery()
# 3、重写父类的方法
#   在执行父类子类同名方法时，Python将忽略父类中的方法，而执行子类中的方法
# 4、将实例用作属性
#  _init_方法的形参是可选的，如果未提供值，则电瓶容量将被设置为70
'''class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

my_tesla.battery.describe_battery()'''

#****** 9.4 导入类 ******
#   Python允许将类存储在模块中，然后在主程序中导入所需的模块
# 1、导入单个类
from car import Car

my_new_car = Car('Ferrari', '458', 2016)
print(my_new_car.get_descriptive_name())
# 2、在一个模块中存储多个类
from car import ElectricCar

my_tesla = ElectricCar('biyadi', 'qin', 2016)
print(my_tesla.get_descriptive_name())
# 3、从一个模块中导入一个类
from car import Car,ElectricCar

my_new_car = Car('benz', '458', 2016)
print(my_new_car.get_descriptive_name())
my_tesla = ElectricCar('aodi', 'qin', 2016)
print(my_tesla.get_descriptive_name())
# 4、导入整个模块
import car

my_new_car = car.Car('benz', '458', 2016)
print(my_new_car.get_descriptive_name())
my_tesla = car.ElectricCar('aodi', 'qin', 2016)
print(my_tesla.get_descriptive_name())
# 5、导入模块中的所有类
#   不推荐这种导入方式，
#   ⑴没有明确指出使用了模块中哪些类
#   ⑵如果不小心导入了一个与程序文件中其他东西同名的类，会引发错误
from car import *
# 6、在一个模块中导入另一个模块
#   例如：将Car类存储在一个.py中，将ElectricCar和Battery类存储在一个.py中
#   在第二个.py文件的开头，写 import car from Car，即将一个模块导入了另一个模块
# 7、自定义工作流程
#   尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中

#****** 9.5 Python标准库  ******
#   为使用标准库中的任何函数和类，只需在程序开头包含一条简单的import语句
# 1、模块collections中的 OrderedDict类
#   字典能够将信息关联起来，但不记录添加键-值对的顺序。
#   要创建字典并记录其中的键-值对的添加顺序，可使用OrderedDict类
#   OrderedDict实例的行为几乎与字典相同，区别只在于记录了键-值对的添加顺序
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
            language.title() + ".")

#****** 9.6 类编码风格 ******
# 1、命名方式：驼峰命名法，即将类名中的每个单词的首字母都大写，而不适用下划线。
#                      实例名和模块名都采用小写格式，并在单词之间加上下划线。
# 2、对于每个类，都应紧跟在类定义后面包含一个文档字符串，简要地描述类的功能
# 3、在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类
# 4、需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，
#    再添加一个空行，然后编写导入你自己编写的模块的import语句。









