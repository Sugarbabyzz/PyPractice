#****** 16.2 制作交易收盘价走势图：JSON格式 ******

# 1、下载收盘价数据
#   统计日期、月份、周数、周几以及收盘价
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

try:
    # Python 3.x 版本
    from urllib.request import urlopen
except ImportError:
    # Python 2.x 版本
    # from urllib2 import urlopen
    print("Import Error")

import json

'''
json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# urlopen(json_url)将网址传入urlopen函数，执行后，向Github服务器发送请求，响应后将对应文件发送给Python
response = urlopen(json_url)
# 使用response.read()就可以读取文件数据
req = response.read()
# 将数据写入文件'btc_close_2017_urllib.json'中
with open('btc_close_2017_urllib.json', 'wb') as f:
    f.write(req)
# 加载json格式，使用json.load将文件内容转换成Python能够处理的格式
file_urllib = json.loads(req)
print(file_urllib)
'''

# **第三方模块requests的使用**
#   让数据的下载和读取方式变得简单
import requests
'''
json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# requests通过get方法向Github服务器发送请求
# Github服务器响应请求后，返回的结果存储在req变量中
req = requests.get(json_url)
# 将数据写入文件
# req.text属性可以直接读取文件数据，返回格式是字符串，文件内容与上面的是一样的
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
# 直接用req.json()就可以将文件的数据转换成Python列表，内容与上面的是一样的
file_requests = req.json()
print(file_urllib == file_requests)
'''


# 2、提取相关的数据
import pygal
import math

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # 这里套用int(float())，先将收盘价从字符串转为浮点数，再去掉小数部分，转为整数
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

'''------------------------------------------------'''

# 创建Line实例，x_label_rotation=20让x轴上的日期标签顺时针旋转20°，show_minor_x_labels=False告诉图形不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20  # 轴坐标每隔20天显示依次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图（￥）.svg')

'''------------------------------------------------'''

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20  # 轴坐标每隔20天显示依次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')

# **用对数变换剔除非线性趋势之后，整体上涨的趋势更接近线性增长，可见每个季度末似乎有显著的周期性

'''------------------------------------------------'''

# 3、将字符串转换为数字值
#   json文件中，每个键和值都是字符串，为了对交易数据进行计算，需要将周数和收盘价的字符串转换为数值

# 4、绘制收盘价折线图

# 5、时间序列特征初探
#   进行实践序列分析，总是期望发现趋势（trend）、周期性（seasonality）和噪声（noise），从而能够描述事实、预测未来、做出决策
#   折线图中，总体趋势是非线性的，而且增长幅度不断增大
#   3、6、9月有一些波动，其中也许有周期性
#   为了验证周期性的假设，需要首先将非线性的趋势消除
#   对数变换（log transformation）是常用的处理方法之一

#   这里以10为底的对数函数math.log10计算收盘价，日期仍然保持不变。这种方式成为半对数（semi-logarithmic）变换

# 6、收盘价均值
#   绘制2017年前11个月的日均值、前49周的日均值，以及每周中各天的日均值

#   将之前的绘图代码封装成函数，以便重复使用
from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

''' 这部分不会了，需要用到时候再看吧 书p332'''





















