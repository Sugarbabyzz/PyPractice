

#****** 4.3 使用pyquery ******
#   适合于用CSS选择器较多的情况

# 1、安装
#   pip3 install pyquery
import pyquery
#   引入PyQuery，别名py
from pyquery import PyQuery as pq

# 2、初始化
#   传入一个参数来初始化Pyquery
#  *字符串初始化

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href ="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div
'''
doc = pyquery.PyQuery(html)
#   简化后
doc = pq(html)
print(doc('li'))

#  *URL初始化
# doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

#  *文件初始化
doc = pq(filename='test.html')
print(doc('li'))

# 3、基本CSS选择器
#   返回的是PyQuery类型
# 实例
html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href ="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
#   #container选择的是id为container的
#   .list选择的是class为list的
#   li直接选择li节点
print(doc('#container .list li'))
print(type(doc('#container .list li')))


# 4、查找节点

#  *子节点
#   查找子节点，用到find()方法，传入的参数是CSS选择器
#   find()的范围是所有子孙节点，如果只查找子节点，用children()方法
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
lis = items.children('.active')
print(type(lis))
print(lis)

#  *父节点
#   用parent()方法，返回直接父节点
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href ="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)
#   用parents()方法，会返回所有的祖先节点
container = items.parents()
print(type(container))
print(container)
#   筛选某个祖先节点，可以传入CSS选择器
container = items.parents('.wrap')
print(type(container))
print(container)

#  *兄弟节点
#   用siblings()方法，返回所有兄弟节点，可传入CSS选择器
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())

#  *遍历
#   单个节点，可以直接打印输出，也可以转成字符串
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(str(li))
#   多个节点，遍历，用items()方法，返回生成器类型
doc = pq(html)
lis = doc('li').items()  # lis是generator类型
print(type(lis))
for li in lis:
    print(li, type(li))


# 6、获取信息

#  *获取属性
#   用attr()方法获取属性
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
#   用attr属性获取属性
print(a.attr.href)
#   但是attr()只能得到第一个节点的属性，要获取所有a节点的属性，就要遍历
doc = pq(html)
a = doc('a')
for item in a.items():
    print(item.attr('href'))

#  *获取文本
#   总结：html()方法返回的是第一个节点的内部HTML文本，多个节点的结果，需要遍历
#        text()方法返回的是所有节点取文本后合并成一个字符串，不需要遍历

#   获取其内部的文本，调用text()方法实现
#   此时会忽略掉节点内部包含的所有HTML，只返回纯文字内容
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href ="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
a = doc('.item-0.active')
print(li)
print(li.text())

#   获取这个节点内部的HTML文本，调用html()方法实现
li = doc('.item-0.active')
print(li)
print(li.html())


# 7、节点操作


