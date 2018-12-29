

#****** 16.1 CSV文件格式 ******
#   要在文本文件中存储数据，最简单的方式是将数据作为一系列以逗号分隔的值（CSV）写入文件。这种称为CSV文件

# 1、分析CSV文件头
#   csv模块包含在Python标准库中，可用于分析CSV文件中的数据行
import csv
from matplotlib import pyplot as plt
from datetime import datetime

'''
filename = 'sitka_weather_2014.csv'
# 调用csv.reader将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader）对象
# 模块csv包含函数next()，调用它并将阅读器对象传递给它时，将返回文件中的下一行，调用一次，即得到的是文件的第一行
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    # 1）从文件中获取最高气温
    #   阅读器对象reader将从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行
    #   并用int()将字符串转为数字，让matplotlib能够读取
    # 2）从文件中获取日期
    # 3）从文件中获取最低气温
    dates, highs, lows = [], [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d") # 将row[0]转换为达特time对象，并将其附加到列表dates末尾
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    print(highs)
    # 对列表调用 enumerate() 来获取每个元素的索引及其值
    for index,column_header in enumerate(header_row):
        print(index, column_header)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # alpha指定颜色的透明度
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 向fill_between传递一个x值系列：列表dates；两个y值系列：highs和lows
    # 实参facecolor指定了填充区域的颜色，填充两y值系列之间的空间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 调用fig.autofmt_xdate来绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
'''
# 2、打印文件头及其位置
# enumerate()获取每个元素的索引及其值

# 3、提取并读取数据
# 获取最高气温

# 4、绘制气温图表

# 5、模块datetime
#   首先导入模块datetime中的datetime类，然后调用方法strptime()
#   第一个实参是所需日期的字符串，第二个实参告诉Python如何设置日期的格式，具体见书P317

# 6、在图表中添加日期

# 7、涵盖更长的时间
#   换上整年的气温数据

# 8、再绘制一个数据系列
#   从数据文件中提取最低气温

# 9、给图表区域着色
#   通过着色来呈现每天的气温范围
#   使用方法fill_between()，它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间

# 10、错误检查
#   导入死亡谷的数据，运行程序会报错
#    trackback指出，Python无法处理其中一天的最高气温，因为它无法将空字符串（' ')转换为整数




filename = 'death_valley_2014.csv'
# 调用csv.reader将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader）对象
# 模块csv包含函数next()，调用它并将阅读器对象传递给它时，将返回文件中的下一行，调用一次，即得到的是文件的第一行
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    # 1）从文件中获取最高气温
    #   阅读器对象reader将从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行
    #   并用int()将字符串转为数字，让matplotlib能够读取
    # 2）从文件中获取日期
    # 3）从文件中获取最低气温
    # 4）加入异常处理，处理字符串为空的情况
    #    只要缺失其中一项数据，就会引发ValueError异常
    #    处理：打印一条错误消息，并指出缺失数据的日期，打印后，循环将接着处理下一行
    dates, highs, lows = [], [] ,[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d") # 将row[0]转换为达特time对象，并将其附加到列表dates末尾
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)
    # 对列表调用 enumerate() 来获取每个元素的索引及其值
    for index,column_header in enumerate(header_row):
        print(index, column_header)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # alpha指定颜色的透明度
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 向fill_between传递一个x值系列：列表dates；两个y值系列：highs和lows
    # 实参facecolor指定了填充区域的颜色，填充两y值系列之间的空间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 调用fig.autofmt_xdate来绘制斜的日期标签，以免它们彼此重叠
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# 结果： 死亡谷更暖和，温差更大