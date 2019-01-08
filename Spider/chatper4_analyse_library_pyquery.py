

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



