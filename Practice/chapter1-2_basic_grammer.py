
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