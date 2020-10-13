import pandas as pd
import re


filepath = 'data/watermeter_dets.txt'
despath = 'data/result.txt'
n = 0  # 计数：当前图片剩余未处理的数字个数
count = 0  # 计数：当前图片总数字个数
position = []  # 存放该图片所有的数字对应的坐标，每个数字对应坐标以list形式存储
img = ''  # 当前图片名

with open(filepath, 'r', encoding='UTF-8') as f, open(despath, 'a', encoding='UTF-8') as f1:
    lines = f.readlines()
    for line in lines:
        newline = line.strip('\n')
        # print(newline)

        if n != 0:  # 不等于0，即当前图片的坐标还未存储完。  为0则当前图片处理完毕。
            pos = newline.split(' ')   # 存储单个数字坐标
            pos = list(map(float, pos))  # 将坐标数组str转为float
            position.append(pos)  # 存储当前图片所有数字坐标
            n -= 1
        elif newline.endswith('.jpg'):
            # 先处理上一张图片
            position.sort()  # 将坐标按照数字顺序排序
            numbers = img.split('-')[-1].replace('.jpg', '')
            num_list = list(numbers)  # 得到该图片中出现的数字，以list存储
            print(num_list)
            print(img + ' ' + str(count) + ' ' + str(position))
            if count == len(num_list) and count == len(position):
                # 处理路径
                # if img.startswith('201901') or img.startswith('201901') or img.startswith('201901') or img.startswith('201901'):
                #     img = '2rightwm/' + img
                # else:

                for i in range(count):
                    f1.write(img + ' ' + num_list[i] + ' ' + str(position[i]) + '\n')
            position = []

            # 开始处理当前这张图片
            img = newline  # 获取当前图片名
        elif len(newline) == 1:
            count = int(newline)
            n = count  # 获取当前图片数字总数




