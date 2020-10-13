# 打印txt以ing结尾的单词
for line in open('data/file.txt'):
    for word in line.split():
        if word.endswith('ing'):
            print(word)

