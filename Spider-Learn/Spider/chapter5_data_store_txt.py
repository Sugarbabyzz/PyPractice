

#****** 5.1.1 TXT文本存储 ******

#   优点：兼容任何平台
#   缺点：不利于检索

# 1、目标：保存知乎上"发现"页面的"热门话题"部分

# 2、实例
import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers=headers).text
print(html)
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()

    # file = open('explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    # file.write('\n' + '==' * 50 + '\n')
    # file.close()

    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '==' * 50 + '\n')










