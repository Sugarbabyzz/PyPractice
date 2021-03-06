

#****** 4.1 使用XPath ******
# XML Path Language， 即XML路径语言，它是一门在XML文档中查找信息的语言，用来搜寻XML文档的，也适用于HTML文档的搜索
# XPath中提供100多个函数，具体作用参考：http://www.w3school.com/cn/xpath/xpath_functions.asp

# 1、XPath概述

# 2、XPath常用规则
#   title[@lang='eng] 代表选择所有名称为title，属性lang的值为eng的节点

# 3、准备工作
#   安装好lxml库
#   pip3 install lxml
import lxml

# 4、实例
from lxml import etree

#  1）对网页进行解析
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)  # 一个最后一个li节点没有闭合，etree模块自动闭合
result = etree.tostring(html)
print(result.decode('utf-8'))

#   2）对文本文件进行解析
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

# 5、所有节点
#   一般用//开头的XPath规则来选取所有符合要求的节点，*表示所有节点都会被获取
#   返回的是一个列表，每个元素是Element类型，其后跟了节点的名称
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

#   选取所有的li节点，将*换成li即可
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])

# 6、子节点
#   通过/或//即可查找元素的子节点或子孙节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

#   通过'//ul/a'获取的结果是空列表，ul下只有li子节点

# 7、父节点
#   1）选中a节点，获取父节点，再获取class属性
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

#   2）也可以通过partent::来获取父节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 8、属性匹配
#   可以用@进行属性过滤
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

# 9、文本获取
#   用text()方法获取节点中的文本
#   获取上面li节点中的文本，文本内容在li节点下子节点a里
#   1）要获取子孙节点内部的所有文本，用//加text()方式，文本信息最全面，夹杂特殊字符
#   2）要获取某些特定子孙节点下的所有文本，先选取到特定的子孙节点，再调用text()方法获取内部文本，最整洁
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 10、属性获取
#   注意与属性匹配进行区分
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

# 11、属性多值匹配
#   用contains()函数，第一个参数传入属性名称，第二个参数传入属性值
#   以下li节点中，class属性中包含 li li-first两个值
text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# 12、多属性匹配
#   使用运算符and来连接
#   以下li节点同时包含class和name属性
text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

# 13、按序选择
#   同时匹配多个节点，而只要其中某个节点
#   可以利用中括号中传入索引的方法获取特定次序的节点
#   下标是从1开始的

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)
#   选取第一个li节点
result = html.xpath('//li[1]/a/text()')
print(result)
#   选取最后一个li节点
result = html.xpath('//li[last()]/a/text()')
print(result)
#   选取位置小于3的li节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
#   选取倒数第三个li节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)

# 14、节点轴选择
#   XPath中提供很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)
#   调用ancestor轴，获取所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
#   加限定条件div
result = html.xpath('//li[1]/ancestor::div')
print(result)
#   调用attribute轴，获取所有属性的值
result = html.xpath('//li[1]/attribute::*')
print(result)
#   调用child轴，获取所有直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
#   调用descendant轴，获取所有子孙节点
result = html.xpath('//li[1]/descendant::span')
print(result)
#   调用following轴，获取当前节点之后的所有节点（包含li节点）
result = html.xpath('//li[1]/following::*[1]')
print(result)
#   调用following-sibling轴，获取当前节点之后的所有同级节点（包含li节点）
result = html.xpath('//li[1]/following-sibling::*')
print(result)
