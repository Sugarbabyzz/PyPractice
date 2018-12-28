

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
'''age = int(age)'''
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

