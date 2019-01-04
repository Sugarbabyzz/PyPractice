# ****** 3.2 使用requests ******

# 1、基本用法

#   1）准备工作
#   安装requests库

#   2）实例
import requests

'''
#   实现与urlopen()相同的操作
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
#   其他的请求类型也一句话完成
r = requests.post('https://httpbin.org/post')
'''

#   3）GET请求

#   *基本实例
'''
data = {
    'name': 'germey',
    'age': 20
}
r = requests.get('https://httpbin.org/get', params=data)
print(r.text)
#   str类型的，也是JSON格式的，可以转换为字典
print(type(r.text))
print(r.json())
print(type(r.json()))
'''

#   *抓取页面
#   抓取知乎-发现页面为例
#   加入headers信息，包括User-Agent字段信息，即浏览器标识信息，防止反爬
#   用正则表达式匹配出所有问题的内容

'''
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_line.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(r.text)
print(titles)
'''

#   *抓取二进制数据
#   获取多媒体文件

'''
import requests

r = requests.get("https://github.com/favicon.ico")
print(r.text)       # str
print(r.content)    # 二进制
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
'''

#   *添加headers

'''
# 不添加headers访问知乎，将 Error 400
import requests

r = requests.get('https://www.zhihu.com/explore')
print(r.text)
'''

#   4）POST请求

'''
data = {
    'name': 'germey' ,
    'age': 24
}
r = requests.post('https://httpbin.org/post', data=data)
print(r.text)
'''

#   5）响应

'''
r = requests.get('https://www.baidu.com')
exit() if not r.status_code == requests.codes.ok else print('Successfully')
'''

# 2、高级用法

#   1）文件上传

'''
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('https://httpbin.org/post', files=files)
print(r.text)
'''

#   2）Cookies

'''
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print(key + "=" + value)
'''

'''
#   没登录上啊
headers = {
    'Cookies': '_zap=9b7580c8-b4e3-4f4f-88ff-ba2507de34b2; _xsrf=d3kYwAdAXjNZSrjmzVEmz1rz0mxatd4v; d_c0="AOBhiYtZuA6PThvhGtcHSPg_5kMNT1v4Pwo=|1545669673"; capsion_ticket="2|1:0|10:1545669684|14:capsion_ticket|44:MDE1ZjE0ZTljMWMyNGY1ODk1MWM3ZTVjYTE4NTBhNzM=|5de726d514b61701d8b9858dd449826cc55dc2ad575389c911fafcad7471b9e1"; z_c0="2|1:0|10:1545669688|4:z_c0|92:Mi4xUzFRa0FnQUFBQUFBMEtKOGkxbTREaVlBQUFCZ0FsVk5PRm9PWFFBZFJadEE1QWZsNGkwTVNvckFVa3Q3NklITmNn|23a4497b07c558d98c0bf81c58bab7256514516ad3d578930a8e5afcba26f6aa"; tst=r; q_c1=7ac1f0e6e2c94d599faa90b276b207c4|1545669689000|1545669689000; __utmv=51854390.100--|2=registration_date=20150930=1^3=entry_date=20150930=1; __gads=ID=4e9d5f25767b6536:T=1546073202:S=ALNI_MbY2JPVDaqX958AWufLnv6SReAOMg; __utmz=51854390.1546261259.4.4.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=51854390.1868916653.1545669741.1546261259.1546485975.5; __utmc=51854390; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
'''

#   3）会话维持

'''
#   以下错误示例
requests.get('https://httpbin.org/cookies/set/number/123456789')
r = requests.get('https://httpbin.org/cookies')
print(r.text)

#   以下正确示例
s = requests.Session()
s.get('https://httpbin.org/cookies/set/number/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)
'''

#   4）SSL证书验证

'''
#   设置忽略警告来屏蔽警告
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
'''

#   5）代理设置
#   防止大规模访问被封禁

'''
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
requests.get('https://www.baidu.com' , proxies=proxies)
'''

#   6）超时设置

'''
r = requests.get('https://www.taobao.com', timeout = 0.001)
print(r.status_code)
'''

#   7）身份认证

'''
# HTTPBasicAuth类认证
r = requests.get('http://127.0.0.1:5000', auth=('username', 'psasword'))
print(r.status_code)
# OAuth认证
#   安装oauth包， pip3 install requests_oauthlib
'''

#   8）Prepared Request

from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)



