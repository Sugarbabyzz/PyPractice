import numpy as np

data = np.random.randn(3, 2)
print(data)

# ndim、shape、dtype属性
data1 = [[1.1, 2, 3, 4], [5, 6, 7, 8]]
arr1 = np.array(data1)
print(arr1.shape)

print(np.arange(10))

arr = np.array([1.4, 2.2, 3.3, 4.1])
print(arr.dtype)
print(arr.astype(np.int32))

arr = np.arange(10)
print(arr[5])

data1 = [[1.1, 2, 3, 4], [5, 6, 7, 8]]
print(arr1[1, 0:2])

names = np.array(['h', 'e', 'o', 'o', 'l'])
data = np.random.randn(5, 4)
print(data)
print(names == 'o')
print(data[names == 'o', :2])

# 存储数组
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))

# dot
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])

print(np.dot(x, y))
print(x.dot(y))


