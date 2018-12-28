#****** 10.1 从文件中读取数据 ******
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
file_path = '/Users/sugar/Documents/GitHub/PyPractice/text_files/filename.txt'
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









#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******
#****** 4.1 遍历整个列表 ******