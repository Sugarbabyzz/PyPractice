from lxml import etree
import json

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
result = etree.tostring(html).decode('utf-8')
html_data = html.xpath('/html/body/div/ul/li/a')
print(etree.tostring(html).decode('utf-8'))
print(html_data)
li = html.xpath('//ul/li[contains(@class, "inactive"]')
for i in li:
    print(i.text)

