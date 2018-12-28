

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









