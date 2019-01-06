

#****** 4.1 使用XPath ******
# XML Path Language， 即XML路径语言，它是一门在XML文档中查找信息的语言，用来搜寻XML文档的，也适用于HTML文档的搜索

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

