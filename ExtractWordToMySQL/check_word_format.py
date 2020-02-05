import docx
import pandas as pd
import re
import os


# check 标题格式是否符合要求
# cncert
rootpath = 'data/评估报告处理中/待处理'
count = 0
for dirname in os.listdir(rootpath):
    dirpath = rootpath + '/' + dirname
    if dirname == '.DS_Store':
        continue
    print(dirpath)
    for filename in os.listdir(dirpath):
        if filename == '.DS_Store':
            continue
        print('-——————————————————-——————————————————-——————————————————')
        filepath = dirpath + '/' + filename
        count += 1
        print('-————-————' + filepath + '-————-————')
        # 默认是docx文件，如果是doc需要先转成docx
        try:
            docx_file = docx.Document(filepath)
            for p in docx_file.paragraphs:
                if p.style.name == 'Heading 1' or p.style.name == 'Heading 2' or '标题' in p.style.name:
                    print(p.style.name + ' : ' + p.text.strip())
                # print(p.style.name)
        except:
            print('处理错误！ ：' + filepath)

print('------------------------------------------')
print(count)