import pandas as pd
import numpy as np
# import modin.pandas as pd

# 不含header和index读取和写回excel的操作
df = pd.read_excel('data/test.xlsx', header=None, index_col=None)
print(df)
df.to_excel('data/test_back.xlsx', index=None, header=None)
""" 一、生成数据表 """
# 开始使用pandas
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                   columns=['id', 'date', 'city', 'category', 'age', 'price'])
df.to_excel('data/data.xlsx')

""" 二、数据表检查 """
# 1、查看数据维度
print(df.shape)
# 2、查看数据表信息
print(df.info())
# 3、查看数据格式
print(df.dtypes)
# 查看单列数据格式
print(df['date'].dtypes)
# 4、查看空值
print(df.isnull())
# 查看特定列空值
print(df['price'].isnull())
# 5、查看唯一值
print(df['city'].unique())
# 6、查看数据表的值，转为numpy.ndarray类型
print(df.values)
# 7、查看数据表中的列名称
print(df.columns)
# 8、查看前10条数据
print(df.head(10))
# 9、查看后10条数据
print(df.tail(10))

""" 三、数据表清洗 """
# 1、删除数据表中含有空值的行
df.dropna(how='any')
# 2、使用数字0来填充空值
df.fillna(value=0)
# 使用price的均值来填充空值   ,要对原df修改，加上Inplace=True参数即可
df['price'].fillna(df['price'].mean(), inplace=True)
# 3、清除空格
df['city'] = df['city'].map(str.strip)
# 4、大小写转换
df['city'] = df['city'].str.lower()
# 5、更改数据格式
df['price'] = df['price'].astype('int')
# 6、更改列名称
df = df.rename(columns={'category': 'category-size'})
# 7、删除重复值
df = df.drop_duplicates(['city'])
# 8、数值修改及替换
df['city'] = df['city'].replace('sh', 'shanghai')


""" 四、数据预处理 """
df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                  "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                  "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y'],
                  "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})

# 1、数据表合并，以公共列为基准
df_inner = pd.merge(df, df1, how='inner')  # inner交集
df_left = pd.merge(df, df1, how='left')
df_right = pd.merge(df, df1, how='right')
df_outer = pd.merge(df, df1, how='outer')
print(df_outer)
# 2、设置索引
df_inner = df_inner.set_index('id')
# 3、排序（按索引，按数值）
df_inner = df_inner.sort_values(by=['age'])
df_inner = df_inner.sort_index()
# 4、数据分组
df_inner['group'] = np.where(df_inner['price'] > 3000, 'high', 'low')  # 将price高于3000的分组为high，否则为low
df_inner.loc[(df_inner['city']=='shenzhen') & (df_inner['price']>3000), 'sign'] = 1
# 5、数据分列
df3 = pd.DataFrame((x.split('-') for x in df_inner['category-size']), index=df_inner.index, columns=['category', 'size'])
print(df3)


""" 五、数据提取 """
# 1、按标签提取（loc）
# 索引提取单行数据
print(df_inner.loc[1001])
# 索引提取区域行数据
print(df_inner.loc[1001:1004])
# 重设索引
df_inner = df_inner.reset_index()
# 设置日期为索引
df_inner = df_inner.set_index('date')
# 提取4日前的数据
print(df_inner.loc[: '2013-01-04'])
# 2、按位置提取
# 使用位置区域提取数据
print(df_inner.iloc[:3, :2])
print(df_inner.iloc[[1, 2, 3], [4, 5]])
# 3、按标签和位置提取数据
# But .ix is deprecated.
# print(df_inner.ix[: '2013-01-04', :4])
# 4、按条件提取（区域和条件值）:使用loc和isin配合，对指定条件数据进行提取
print(df_inner.loc[df_inner['city'].isin(['beijing', 'shanghai'])])


""" 六、数据筛选 """
# 1、按条件筛选（与、或、非）
# 与
print(df_inner.loc[(df_inner['age'] > 20) & (df_inner['city'] == 'beijing'),
                ['id', 'city', 'age', 'pay']])
# 或
print(df_inner.loc[(df_inner['age'] > 20) | (df_inner['city'] == 'beijing'),
                ['id', 'city', 'age', 'pay']])
# 非
print(df_inner.loc[df_inner['city'] != 'beijing'])
# 使用count进行计数
print(df_inner.loc[df_inner['city'] != 'beijing'].age.count())
# 使用query进行筛选
print(df_inner.query('city == ["beijing", "shanghai"]'))
# 使用sum进行求和
print(df_inner.query('city == ["beijing", "shanghai"]').price.sum())


""" 七、数据汇总 """
# 1、分类汇总
# 对所有列进行计数汇总
print(df_inner.groupby('city').count())
# 对特定ID列进行计数汇总
print(df_inner.groupby('city')['id'].count())
# 对两个字段进行汇总计数
print(df_inner.groupby(['city', 'age'])['id'].count())
# 对汇总后的数据进行多维度计算
print(df_inner.groupby('city')['price'].agg([len, np.sum, np.mean]))
# 2、数据透视
#


""" 八、数据统计 """
# 1、数据采样
# 简单数据采样
print(df_inner.sample(n=3))
# 手动设置权重采样
# weights = [0, 0, 0, 0, 0.5]
# print(df_inner.sample(n=2, weights=weights))
# 2、描述统计
# 数据表描述性统计
print(df_inner.describe().round(2).T)
# 3、相关分析
# 数据表相关性分析
print(df_inner.corr())
print(df_inner['age'].corr(df_inner['price']).round(2))





