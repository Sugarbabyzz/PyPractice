

#****** 3.1 使用urllib ******

import urllib.request
import urllib.parse
import socket
import urllib.error

# 1、发送请求
#   1）urlopen()

# response = urllib.request.urlopen('https://www.baidu.com')
# print(type(response))   # type输出响应的类型
# print(response.status)  # 响应状态码
# print(response.getheaders())    # 响应的头信息
# print(response.getheader('Server'))     # 获取响应头信息中Server的值

# *data参数

'''
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
'''

# *timeout参数

'''
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time out!")
'''

#  *其他参数见书P106

#   2)Request
#   请求中需要加入Headers等信息，需要Request类来构建

'''
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

# *url参数（必传）
# *data参数 bytes类型，如果是字典用urllib.parse模块里的urlencode()编码
# *headers参数 是一个字典，也就是请求头。 可直接构建，也可以通过调用请求实例的add_header()方法添加
# *origin_req_host参数 请求方的host名称或IP地址
# *unverifiable参数 是否可验证
# *method 字符串，用来指示请求使用的方法

'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict ={
    'name': 'Germey'
}
data = bytes(urllib.parse.urlencode(dict), encoding='UTF-8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)') # 也可以用add_header
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
'''

#   3)高级用法

# *验证
#   借助HTTPBasicAuthHandler：用于管理认证，如果一个链接打开时需要认证，可用它解决认证问题

'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
'''

# *代理
#   本地搭建一个代理，运行在9743端口上

'''
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'http://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''

# *Cookies

'''
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

# 也可以以文本保存cookies
filename = 'cookies.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 读取文本并利用（LWP为例）
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
'''

# 2、处理异常

#   1）URLError
#   是error异常模块的基类，由request模块产生的异常都可以通过这个类处理
#   只有一个属性reason，返回错误的原因
from urllib import request, error
'''
try:
    response = request.urlopen('http://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)
'''
#   2)HTTPError
#   URLError的子类，专门用来处理HTTP请求错误
#   由三个属性：code、reason、headers

'''
try:
    response = response = request.urlopen('http://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
'''

# 3、解析链接

#   1）urlparse()
#   实现URL的识别和分段
#   协议；域名；访问路径；参数；查询条件；锚点
#   返回的结果ParseResult 是一个元组，可以按顺序索取，也可以按属性名获取
from urllib.parse import urlparse

'''
result = urlparse('https://www.baidu.com/index.html;user?id=5%comment')
print(type(result), result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
'''

#   2）urlunparse()      代码看书P116
#   实现URL的构造

#   3）urlsplit()
#   和urlparse相似，parms会合并到path中

#   4）urlunsplit()
#   实现URL的构造

#   5）urljoin()
#   实现URL的构造，对长度要求不严格，易用

#   6）urlencode()
#   构造GET请求参数，常用！

from urllib.parse import urlencode

parms = {
    'name': 'germey',
    'age': 20
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(parms)
print(url)

#   7）parse_qs()
#   GET请求参数转换为字典

#   8）parse_sql()
#   GET请求参数转换为列表

#   9）quote()
#   将内容转换为URL编码的格式
#   解决URL中含有中文参数，乱码的问题

#   10）unquote()
#   对URL编码进行解码


# 4、分析Robots协议
#   1）Robots协议
#   告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取

#   2）爬虫名称

#   3）robotparser
#   用robotparser模块来解析robots.txt
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=1&type=collections'))










