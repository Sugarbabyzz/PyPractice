

#****** 4.1 使用 Beautiful Soup ******
#   Python是一个HTML或XML解析库

# 1、简介
#   自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码

# 2、准备工作
#   安装Beautiful Soup和lxml

# 3、解析库
#   1）"html.parse"   2）"lxml"   3）"xml"   4）"html5lib"
#   推荐使用lxml
from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

# 4、基本用法

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><~-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# BeautifulSoup 对于不标准的HTML字符串自动更正格式
soup = BeautifulSoup(html, 'lxml')
# prittify()方法，将解析的字符串以标准的缩进格式输出
print(soup.prettify())
# soup.title.string 输出HTML中title节点的文本内容
print(soup.title.string)

# 5、节点选择器
#   调用节点名称选择节点，调用string属性得到节点内的文本

# *选择元素
#   当有多个节点时，只匹配第一个节点，其他的后面节点都会忽略
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><~-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)  # 只返回了第一个p节点

# *提取信息
#   1）获取节点名称
print(soup.title.name)
#   2）获取属性
#   调用attrs，返回的是字典
print(soup.p.attrs)
print(soup.p.attrs['name'])
#   也可以不调用attrs，单属性返回字符串，多属性返回列表
print(soup.p['name'])
print(soup.p['class'])
#   3）获取内容
print(soup.p.string)

# *嵌套选择
print(soup.head.title)
print(soup.head.title.string)

# *关联选择
#   选中某个节点元素为基准，再选择它的子节点、父节点、兄弟节点

html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
    <span>Elsie</span>
    </a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
'''
#   1）子节点和子孙节点
#   要得到直接子节点，调用contents属性，返回列表形式
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
#   也可以调用children属性，同样也得到相应的结果，返回的是生成器类型
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i, child)
#   得到所有的子孙节点的话，调用descendants属性，返回的是生成器类型
print(soup.p.descendants)
for i,descendant in enumerate(soup.p.descendants):
    print(i, descendant)

#   2）父节点和祖先节点
#   要得到某个节点元素的父节点，可以调用parent属性，输出结果是父节点及其所有内容
print(soup.a.parent)
#   要获取所有祖先节点，调用parents属性，返回的是生成器类型
print('\n\n\n' + str(type(soup.a.parents)))
print(list(enumerate(soup.a.parents)))  # 用列表输出了它的索引和内容

#   3）兄弟节点
html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
        Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
</p>
'''
soup = BeautifulSoup(html, 'lxml')
#   next_sibling和previous_sibling分别获取下一个和上一个兄弟元素
print('New Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
#   next_siblings和previous_siblings返回后面和前面的兄弟节点
print('New Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Sibling', list(enumerate(soup.a.previous_siblings)))

#   4）提取信息
#   单个节点直接提取，生成器要转换为列表再提取
html = '''
<html>
<body>
<p class="story">
        Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
'''
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


# 6、方法选择器
#   1）find_all()
#   传入一些属性或文本，就可以得到所有符合条件的元素
#   API： find_all(name, attrs, recursive, text, **kwargs)

