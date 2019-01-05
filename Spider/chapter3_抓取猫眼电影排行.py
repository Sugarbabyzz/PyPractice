

#****** 3.4 抓取猫眼电影排行 ******

#   利用requests库和正则表达式来抓取猫眼电影TOP100的相关内容
#   requests库比urllib使用更加方便，还没有学习HTML解析库，用正则表达式代替

# 1、目标
#   提取猫眼电影TOP100的电影名称、时间、评分、图片等信息
#   站点：http://maoyan.com/board/4
#   提取结果以文件形式保存

# 2、准备
#   安装requests库

# 3、抓取分析
#   http://maoyan.com/board/4?offset=n
#   偏移量为n，则显示的电影序号就是n+1到n+10，每页显示10个
#   获取TOP100，只需分别请求10次

# 4、抓取首页
import requests
import re
import json

'''传入url参数，将抓取的页面结果返回'''
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

'''解析页面，正则表达式提取出内容，并生成字典'''
def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[5].strip()
        }

'''实现将字典写入到文本文件的过程，content参数即一部电影的提取结果，是一个字典'''
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')




'''主函数'''
def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

'''主程序'''
main()

# 5、正则提取
#   不要在Elemtns选项卡中直接查看源码，那里的源码可能经过Javacript操作而与原始请求不同
#   需要从Network选项卡部分查看原始请求得到的源码

#   定义解析页面的方式parse_one_page()

# 6、写入文件
#   通过JSON库的dumps()方法实现字典的序列化，并指定ensure_ascii参数为False，保证输出结果是中文形式而不是Unicode编码

#   定义write_to_file()方法

# 7、整合代码
#   实现main()方法

