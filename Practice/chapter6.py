

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

