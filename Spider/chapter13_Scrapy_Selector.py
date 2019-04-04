

#****** 13.1 Scrapy框架的使用 ******



#****** 13.2 Scrapy入门 ******

# 建Scarpy项目命令行流程
#   在项目目录下
#   scrapy startproject tutorial

#   cd tutorial
#   scrapy genspider quotes quotes.toscrape.com

#   scrapy crawl quotes 运行


#****** 13.3 Selector的用法 ******

# Selector基于lxml构建。支持XPath选择器、CSS选择器以及正则表达式

# 1、直接使用

from scrapy import Selector

body = '<title>Hello World</title>'
selector = Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)

# 2、Scrapy shell

# scrapy shell xxxx

# 3、XPath选择器

# response有一个属性selector，调用response.selector返回的内容相当于用response的text构造了一个Selector对象
# 而response.xpath()和response.css()功能与上面的相同

# 可以为extract_first()设置默认值

# 4、CSS选择器

#   获取文本和属性需要用::text和::attr()的写法

# 可以先用xpath在用CSS
#   response.xpath('//a').css('img').xpath('@src').extract()

# 5、正则匹配

#   response.xpath('//a/text()').re('Name:\s(.*)')
#   输出括号内的，列表形式

#   response.xpath('//a/text()').re_first('Name:\s(.*)')
#   输出第一个

#   注意：response不能直接调用re，可以先用xpath再正则




#****** 13.4 Spider的用法 ******



