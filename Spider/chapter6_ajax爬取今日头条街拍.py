

#****** 6.4 分析Ajax爬取今日头条街拍 ******

# 1、安装requests库

# 2、抓取分析

# 3、实现
#   图片下载

import requests
from urllib.parse import urlencode

basic_url = 'https://www.toutiao.com/api/search/content/?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

#   加载单个Ajax请求的结果，offset为唯一变量参数
def get_page(offset):
    params = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }

    url = basic_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        return None

    


