

#****** 6.1 Ajax ******

# Asynchronous JavaScript and XML
# requests获取的是原始HTML文档，页面可能经过JavaScript处理数据后生成，也可能通过Ajax加载

# 1、原理
#   1）发送请求
#   2）解析内容
#   3）渲染网页

#****** 6.2 Ajax分析方法 ******

# 1、查看请求
# 2、过滤请求

#****** 6.3 Ajax结果提取 ******

# 1、分析请求
#   打开Chrome的XHR过滤器，选定其中一个请求，分析参数
# 2、分析响应
#   只有page是可变参数
# 3、实战演练
#   获取前十页微博
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=2

from urllib.parse import urlencode
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)





