

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

