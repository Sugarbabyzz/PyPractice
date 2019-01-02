

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
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

# *timeout参数
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.001)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("Time out!")

#  *其他参数见书P106

#   2)Request
#   请求中需要加入Headers等信息，需要Request类来构建

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# *url参数（必传）
# *data参数 bytes类型，如果是字典用urllib.parse模块里的urlencode()编码
# *headers参数 是一个字典，也就是请求头。 可直接构建，也可以通过调用请求实例的add_header()方法添加
# *origin_req_host参数 请求方的host名称或IP地址
# *unverifiable参数 是否可验证
# *method 字符串，用来指示请求使用的方法





