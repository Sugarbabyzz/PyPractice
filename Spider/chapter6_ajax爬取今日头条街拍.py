

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

    url = basic_url + urlencode(params)  # urlencode构造GET参数
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        return None

#   解析方法：提取image_list字段中的每一张图片链接，将图片链接和图片所属标题一并返回
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }

#   实现保存图片的方法，其中item是get_images方法返回的一个字典
import os
from hashlib import md5

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError as e:
        print('Failed to Save Image')

#   主程序





