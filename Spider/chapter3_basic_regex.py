

# ****** 3.3 正则表达式 ******

# 1、实例
#   正则表达式测试工具： http://tool.oschina.net/regex/
import re

# 2、match()
#   传入要匹配的字符串以及正则表达式
#   返回匹配的结果

content = 'Hello 1234567 World_This' \
          ' is a Regex Demo'
print(len(content))
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())