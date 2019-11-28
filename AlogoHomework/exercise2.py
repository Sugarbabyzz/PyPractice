"""
Exercise (2). 定义文件 xx.tar.gz 的产生方式如下:
    • 以 xx 为文件名的文件通过 tar 和 gzip 打包压缩产生，该文件中以字符串的方式记录了一个非负整数;
    • 或者以 xx 为名的目录通过 tar 和 gzip 打包压缩产生，该目录中包含若干 xx.tar.gz。
其中，x ∈ [0, 9]。现给定一个根据上述定义生成的文件 00.tar.gz (该文件 从课程网站下载)，
请确定其中包含的以 xx 为文件名的文件个数以及这些文件中所记录的非负整数之和。
"""

import tarfile
count, count_file = 0, 0
def aa(bb):
    global count, count_file
    count += bb
    count_file += 1
def unpack_path_file(filepath, despath):
    print(filepath + '>>>' + despath)
    archive = tarfile.open(filepath, 'r:gz')  # 获取压缩包
    for tarinfo in archive:
        archive.extract(tarinfo, despath)   # 三种文件类型：目录、tar和文本   第一个参数为要解压的tarinfo，第二个参数为解压的目标路径
        if str(tarinfo.isdir()) == "False":
            if tarinfo.name.endswith('.tar.gz'):
                unpack_path_file(despath + '/' + tarinfo.name, despath + '/' + tarinfo.name.split('/')[0])
            else:
                with open(despath + '/' + tarinfo.name, encoding='utf8') as f:
                    aa(int(f.read()))
    archive.close()
if __name__ == '__main__':
    filepath = 'data/00.tar.gz'
    unpack_path_file(filepath, filepath.split('/')[0])
    print('Count:' + str(count) + ' >>>> Count_file:' + str(count_file))

