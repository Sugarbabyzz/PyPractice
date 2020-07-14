import pandas as pd
from sklearn.utils import shuffle

class_mapping = {
    'EnterSports': 0,
    'Military': 1,
    'Economics': 2,
    'Technology': 3,
    'Government': 4,
}

# df = pd.read_table('origin-data/traindata.txt', sep='\t', header=None)
# df = df.ix[:, [1, 0]]
# df[0] = df[0].map(class_mapping)
# df.to_csv('data2/train.txt', sep='\t', header=None, index=False)
# print(df)
#
# df = pd.read_table('origin-data/testdata.txt', sep='\t', header=None)
# df = df.ix[:, [1, 0]]
# df[0] = df[0].map(class_mapping)
# df.to_csv('data2/test.txt', sep='\t', header=None, index=False)
# print(df)
#
# df = pd.read_table('origin-data/devdata.txt', sep='\t', header=None)
# df = df.ix[:, [1, 0]]
# df[0] = df[0].map(class_mapping)
# df.to_csv('data2/dev.txt', sep='\t', header=None, index=False)
# print(df)

# 统计str长度
# df = pd.read_table('data2/train.txt', sep='\t', header=None)
# print(df)
# df[2] = df[0].str.len()
# print(df)
# print(df[2].mean())

# 复制数据
file_list = ['data2/train.txt', 'data2/test.txt', 'data2/dev.txt']
for file in file_list:
    with open(file, 'r') as f:
        content = f.readlines()
    for i in range(9):
        with open(file, 'a') as f:
            f.writelines(content[0: -1])

# 打乱顺序
df = pd.read_table('data2/dev.txt', sep='\t', header=None)
# df = shuffle(df)
# df.to_csv('data2/dev.txt', sep='\t', header=None, index=False)
print(df.info())
