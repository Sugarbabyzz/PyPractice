

#****** 3.2 使用requests ******

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

