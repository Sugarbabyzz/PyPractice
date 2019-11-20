import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# DateFrame创建的两种方法：
# 1、利用包含等长度列表或NumP数组的字典来行程DataFrame
#    产生的DataFrame会自动为Series分配索引，并且列会按照排序的顺序排列
data = {'state': ['Ohio', 'Nevada', 'Nevada'],
        'year': [2018, 2019, 2020],
        'pop': [1.1, 2.2, 3.3]}
frame = pd.DataFrame(data)
print(frame)
print('\n')

# 2、利用包含字典的嵌套字典
#   将字典的键作为列，将内部字典的键作为索引
data = {'Nevada': {2001: 2.4, 2002: 2.9},
        'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame = pd.DataFrame(data)
print(frame)
print('\n')


# 2.3 索引、选择与过滤
#   df[val]选择单列或列序列，布尔数组（过滤行）、切片（切片行）或布尔值DataFrame
#   df.loc[val]根据标签选择DataFrame的单行或多行

#   Series的索引值不仅是整数
obj = pd.Series(np.array(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

#   Series的切片可以包含尾部
print(obj['b': 'c'])
#   设值会修改Series相应部分
obj['b': 'c'] = 5
print(obj)

#   使用单个值或序列，可以从DataFrame中索引出一个或多个列
#   行选择语法为切片或布尔索引，列选择语法为传递单个元素或一个列表
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

#   使用loc和iloc在行上进行标签索引
#   单行多列
print(data.loc['Colorado', ['one', 'two']])
#   iloc整数标签行索引
print(data.iloc[1, 2], [3, 0, 1])


# 2.4 整数索引
#   对于包含整数的索引，尽量使用loc或iloc
ser = pd.Series(np.arange(3))
print(ser.loc[:2])


# 2.5 算数和数据对齐
#   Series中，将两个对象相加时，如果存在某个索引对不相同，则返回结果的索引将是索引对的并集
#   没有交叠标签的位置上，会产生缺失值
s1 = pd.Series([1.1, 2.2, 3.3, 4.4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([1.1, 2.2, 3.3], index=['a', 'b', 'c'])
print(s1 + s2)
#   DataFrame中，行和列都会执行对齐

#   方法一：使用填充值的算术方法
#   add, sub, div, floordiv, mul, pow
#   每种方法都有以r开头的副本，用于将参数翻转
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df1.loc[1, 'b'] = np.nan
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
print(df1 + df2)
print(df1.add(df2, fill_value=0))

#   方法二：DataFrame和Series间的操作
#   默认情况下，DataFrame和Series的数学操作会将Series的索引和DataFrame的列进行匹配，并广播到各行
arr = np.arange(12.).reshape((3, 4))
print(arr - arr[0])
#   减法对每一行都做了运算，这就是广播机制
#   如果一个索引值不在Series索引中，也不再DataFrame列中，对象会重建索引形成联合
#   如果想改为在列上进行广播，行上进行匹配，必须使用算术方法中的一种


# 2.6 函数应用和映射

#   方法一：Numpy的通用函数（逐元素数组方法）
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Orange'])

print(frame)

#   方法二：将函数应用到一行或一列的一维数组上
f = lambda x: x.max() - x.min()
print(frame.apply(f))  # 对每一列调用
print(frame.apply(f, axis='columns'))  # 对每一行调用


# 2.7 排序和排名
#   需按行或列索引进行字典型排序，需要使用sort_index方法，返回一个新的、排序好的对象。
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())  # 对行索引排序
print(frame.sort_index(axis=1))  # 对列索引排序
print(frame.sort_index(ascending=False))

#   对Series的值排序，使用sort_values方法，缺失值自动放在最后
obj = pd.Series([4, np.nan, 3, 2, 9, np.nan])
print(obj.sort_values())
#   对DataFrame排序，需要用by参数选择需要排序的列
frame = pd.DataFrame({'b': [4, 8, -2, 2], 'a': [0, -1, 1, 0]})
print(frame.sort_values(by=['a', 'b']))


