import pandas as pd
import os


dirpath = 'data/合并/专家'
df_result = pd.DataFrame()  # 存储结果
for filename in os.listdir(dirpath):
    df = pd.read_excel(dirpath + '/' + filename)
    df = df.drop(df[df['推荐级别（初、中、高）'] == '（初、中、高）'].index)
    df_result = df_result.append(df)
print(df_result)
df_result.to_excel('data/合并/专家/评估专家推荐表.xlsx', index=False)

count = 0
dirpath = 'data/合并/报告'
df_result = pd.DataFrame()  # 存储结果
for filename in os.listdir(dirpath):
    df = pd.read_excel(dirpath + '/' + filename)
    df_result = df_result.append(df)
    count += len(df)
print(df_result)
print(count)
df_result.to_excel('data/合并/报告/评估报告登记表.xlsx', index=False)




