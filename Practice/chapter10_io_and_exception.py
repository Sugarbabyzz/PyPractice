

#****** 10.1 从文件中读取数据 ******
#   ✅ 读取文本文件时，Python将其中的所有文本都解读为字符串
#      如果要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数

# 1、读取整个文件
#   *函数open()接受一个参数：要打开的文件的名称
#    Python在当前执行的文件所在的目录中查找指定的文件
#    函数open()返回一个表示文件的对象
#   *关键字with在不再需要访问文件后将其关闭
#    可使用close()函数关闭文件，但如果程序异常，文件将不会关闭，用with Python会在合适的时候自动将其关闭
#   *read()方法，将文件内容作为一个长长的字符串存储在变量contents中
#    结果多出来一个空行，是因为read()到达文件末尾时返回一个空字符串，而将这个字符串显示出来时就是一个空行
#    删除末尾的空行，可在print语句中使用rstrip()
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    # print(contents)
    print(contents.rstrip())  # 并没有解决?>

# 2、文件路径
#   有时可能要打开不在程序文件所属目录中的文件
#   1）相对路径
#      相对文件路径让Python到指定的位置去查找，而该位置时相对于当前运行的程序所在目录的
#      在Windows中，文件路径使用反斜杠（\）
with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
    print(contents)
#   2）绝对路径
#      绝对路径，可读取系统任何地方的文件，需要提供完整的路径
#      在Windows中，最前面需要加盘符和冒号（C:\），路径用反斜杠（\）
file_path = '/Users/sugar/Documents/GitHub/PyPractice/Practice/text_files/filename.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# 3、逐行读取
#   适用：可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本
filename = "pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 4、创建一个包含文件各行内容的列表
#   适用关键字with，open()返回的文件对象只在with代码块内可用。
#   如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表：
#   可以立即处理文件的各个部分，也可推迟到程序后面再处理
with open(filename) as file_object:
    lines = file_object.readlines()  # 注意：这里是readlines不是readline，不能少s
                                     # 此处的lines是列表
for line in lines:
    print(line.rstrip())
print(lines)

# 5、使用文件的内容
#   将文件中的内容存储到列表中，使用循环将各行都加入pi_string
pi_string = ''
for line in lines:
    pi_string += line.strip()  #  .strip剔除左右两边的空白

print(pi_string)
print(len(pi_string))

# 6、包含一百万位的大型文件
#   使用"切片"只打印小数点后几位，以免全部显示
#   Python对可处理的数据量没有任何限制，前提系统的内存足够多
print(pi_string[:20] + "...")

# 7、检查某字符串是否包含于另一字符串中
if 'contain' in pi_string:
    print("Yes")
else:
    print("No")

#****** 10.2 写入文件 ******
# 调用open()时提供了两个实参，第一个实参也是要打开的文件的名称，第二个实参（'w')表示以写入模式打开文件
#   * 读取模式（'r')     写入模式（'w')     附加模式('a')     能够读取和写入文件的模式('r+')
#   如果省略了模式实参，默认以只读模式打开文件
#   如果写入的文件不存在，函数open()将自动创建它；如果已存在，将在返回文件对象前清空该文件！！！！！！（注意）
# 1、写入空文件
filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love python")

# 2、写入多行
#   使用空格、制表符和空行来设置这些输出的格式
with open(filename, 'w') as file_object:
    file_object.write("I love python\n")
    file_object.write("I love creating new games.\n")

# 3、附加到文件
#   给文件添加内容，而不会复原原有的内容，可以用附加模式打开文件
#   将写入到文件的行都将添加到文件末尾
#   如果指定的文件不存在，Python将创建一个空文件
with open(filename, 'a') as file_object:
    file_object.write("No reasons.\n")



#****** 10.3 异常 ******
#   Python使用被称为异常的特殊对象来管理程序执行期间发生的错误
#   每当发生让Python不知所措的错误时，将创建一个异常对象；如果编写了处理该异常的代码，程序将继续运行，否则，程序停止，并显示traceback异常报告
#   异常时使用try-except代码块处理的

# 1、处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 2、使用异常避免崩溃
#   将可能出异常的代码放入try-except代码块中，
#   并包含一个else代码块，将依赖于try代码块成功执行的代码都应放到else代码块中
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Running ok")

# 3、处理FileNotFoundError异常
#   使用文件时，常见的问题是找不到文件
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# 4、分析文本
#   split()方法将一个字符串拆分成多个部分，存储到一个列表中
#   split括号中可以传入一个参数，以某种方式进行划分
title = 'alice in Wonderland'
print(title.split())
title = 'alice-in-Wonderland'
print(title.split('-'))
print(len(title.split('-'))) # 打印长度

# 5、使用多个文件
#   将代码主体放入到一个函数中，文件存入到列表中
#   对列表做个循环，调用函数

# 6、出现异常时，继续运行
#   pass语句，可在代码块中使用让Python什么都不要做
#   pass还可以充当占位符，提醒你在程序的某个地方什么都没有做，并且以后也许要做些什么
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass



#****** 10.4 存储数据 ******
#   程序总会把用户提供的信息存储在列表和字典等数据结构中
#   模块 Json 能将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件

# 1、使用json.dump()和json.load()
#   1）json.dump()  (写入）
#      接受两个实参：要存储的数据以及可用于存储数据的文件对象
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
#   2）json.load()  （读取）
#      使用json.load将这个列表读取到内存中
filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)

# 2、保存和读取用户生成的数据
#   使用json保存用户生成的数据，可避免程序停止运行时用户的信息丢失
#   1)存储用户信息
username = input("What's your name?")

filename = 'username.json'
with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("Remembered " + username)
#   2)读取用户信息
with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back " + username + "!")
#   3)合并
#   如果以前存储了用户名，就加载；否则，提示用户输入用户名并存储
filename = 'username.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What's your name?")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Remembered " + username)
else:
    print("Welcome back " + username + "!")

# 3、重构
#   代码能够正确地运行，但可做进一步的改进----将代码划分为一系列完成具体工作的函数

