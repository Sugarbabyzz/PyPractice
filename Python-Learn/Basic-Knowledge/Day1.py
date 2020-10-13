
# part 1
# score = input("请输入分数  ")
# i = int(score)
# if i>90:
#     print("真棒")
# else:
#     print("一般")

# part 2
# a=3
# b=4
# c=a+b
# print(c)

# part 3
# 打印全部关键字
# import keyword
# print(keyword.kwlist)

# part 4
# ^居中，*剩下的位置用*补满，<左对齐
# 一个中文占一个字符，与Java不同
# print("我叫{:*^20}，今年{:<4}岁".format("张三丰",25))

# part 5
# end向末尾传递一个空字符，实现不换行
# 只能在python3里用
# print("1")
# print("2",end="")
# print("3")

# part 6
# 运算符的运用
# //取整 %取余数
# a = int(input("请输入一个三位数"))
# gw = a%10
# sw = a//10%10
# bw = a//100
# x = gw*100+sw*10+bw
# print(x)

# part 7
# 画等边三角形 （*）
# for i in range(1,7):
#     for j in range(1,6-i+1):
#         print(" ", end='')
#     for j in range(1,2*i-1+1):
#         print("*",end='')
#     print()

# part 8
# 字符串是不可修改，但可以重写，和元组一个道理

# part 9
# 字符串切割
# a = '2010-10-27'
# print(a.split('-'))
# print(a.partition('-'))

# part 10
# yield!
#
# def generator(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
# a = generator(1000)
# print(next(a))
# print(next(a))
# print(next(a))

# part 11
#   装饰器

def hanshu(func):
    def neibu():
        print("***************")
        func()
        print("***************")
    return neibu

@hanshu
def hanshu2():
    print('lalala')

hanshu2()
