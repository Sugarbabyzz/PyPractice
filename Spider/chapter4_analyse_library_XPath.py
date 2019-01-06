

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
result = etree.tostring(html)
print(result.decode('utf-8'))