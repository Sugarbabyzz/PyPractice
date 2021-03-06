

#****** 5.1.2 JSON文件存储 ******

#   通过对象和数组的组合来表示数据，构造简介但是结构化程度高
#   是一种轻量级的数据交换格式

# 1、对象和数组
#   对象：用{}包裹起来的内容，{key1:value1, key2:value2...}
#   数组：用[]包裹起来的内容，["java", "javascript", ...]

# 2、读取JSON
#   利用JSON库来实现JSON文件的读写操作
#   loads()方法将JSON文字字符串转为JSON对象
#   dumps()方法将JSON对象转为文本字符串

#   我们可以将JSON形式的字符串，转换为可操作的数据结构，如列表或字典
import json

#   JSON的数据必须用双引号来包围，不能使用单引号
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))  # 推荐这种，key数错的不报错，返回None

#   若从JSON文本中读取内容，可以先读取再loads转化
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
    print(type(data))


# 3、输出JSON
#   利用dumps()方法将JSON对象转化为字符串

data = [{
    "name": "Bob",
    "gender": "男",
    "birthday": "1992-10-18"
}]
# indent代表缩进字符个数，可以保存JSON的格式
# 中文字符会变成Unicode字符，需要制定参数ensure_ascii为False，并规定文件输出的编码
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))






