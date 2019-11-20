# python2
# coding=utf-8
import sys
import os
import time
import threading
import shutil
from queue import Queue


# args = ' '.join(sys.argv)

# print('Path=' + args)

# 1. Get Videos Files and Convert MP4toJPG

path = '/u01/short187/test_videos'
cpath='/u01/short187/finish_videos'
q = Queue()


def aa():
    for file_name in os.listdir(path):
        file_path = path + '/' + file_name
        q.put(file_name)


def bb(q):
    if(not q.empty()):
        file_name = q.get()
        file_path = path + '/' + file_name
        os.mkdir('/u01/short187/test_result/{0}'.format(file_name.split('.')[0]))
        os.system('ffmpeg -i {0} -vf "select=(gte(n\,25))*not(mod(n\,25))" -vsync 0 {1}'.format(file_path,'/u01/short187/test_result/' +file_name.split('.')[0] + '/%06d.jpg'))
        print('Start Recognizing')
        os.chdir('/u01/short187/faceapi/build')
        path_result = '/u01/short187/test_result'
        dir_name = file_name.split('.')[0]
        print(dir_name)
        dir_path = path_result + '/' + dir_name
        print(dir_path)
        os.system('/u01/short187/faceapi/build/main {0} {1}'.format(dir_path, dir_path + '.txt'))
        print('Recognize Finished!')
        opfile(file_path, cpath)

def opfile(file_path, new_file_path):
    print("拷贝文件....")
    shutil.copy(file_path, new_file_path)
    os.remove(file_path)

def test():

    for file_name in os.listdir(path):
        file_path = path + '/' + file_name
        print(file_path)
        print(file_name.split('.')[0])
        os.mkdir('/u01/short187/test_result/{0}'.format(file_name.split('.')[0]))
        os.system('ffmpeg -i {0} -vf "select=(gte(n\,25))*not(mod(n\,25))" -vsync 0 {1}'.format(file_path,'/u01/short187/test_result/' + file_name.split('.')[0] + '/%06d.jpg'))


    # 2.Train and Get Result

    print('Start Recognizing')

    #os.chdir('/u01/short187/faceapi/build')

    #path = '/u01/short187/test_result'

    for dir_name in os.listdir(path):
        print(dir_name)
        dir_path = path + '/' + dir_name
        os.system('/u01/short187/faceapi/build/main {0} {1}'.format(dir_path, dir_path + '.txt'))


print('Recognize Finished!')


if __name__ == '__main__':
    print('Start Decoding Videos')

    while(1):
        aa()
        while not q.empty():
            print("数量:", q.qsize())
            if( q.qsize() > 10):
                for i in range(10):
                    th1 = threading.Thread(target=bb(q), daemon=True)
                    th1.start()
            else:
                for i in range(q.qsize()):
                    th1 = threading.Thread(target=bb(q), daemon=True)
                    th1.start()

        time.sleep(10)
        break
    print('ceshi')
