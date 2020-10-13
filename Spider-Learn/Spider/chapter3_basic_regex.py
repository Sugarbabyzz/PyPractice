

# ****** 3.3 正则表达式 ******

# 1、实例
#   正则表达式测试工具： http://tool.oschina.net/regex/
import re

# 2、match()
#   传入要匹配的字符串以及正则表达式
#   返回匹配的结果

content = '''Hello 1234567 World_This 
            is a Regex Demo'''

result = re.match('^He.*?(\d+).*Demo$', content, re.S)

print(result)
print(result.group(1))

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result.group())

# 3、search()
#   匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
#   一般网页代码有换行，第三个参数需要传入re.S

result = re.search('<li.*?active.*?singer="(.*?)>(.*?)</a>', content, re.S)

# 4、findall()
#   匹配时会扫描整个字符串，然后返回匹配的所有内容

result = re.findall('<li.*?singer="(.*?)>(.*?)</a>', content, re.S)

# 5、sub()
#   用来修改文本，简化搜索匹配

content = 'dsa32da2fdsa1fdsa9g9fd'
content = re.sub('\d+', '', content)
print(content)

# 6、compile()
#   将正则字符串编译成正则表达式对象，以便在后面的匹配中复用

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
