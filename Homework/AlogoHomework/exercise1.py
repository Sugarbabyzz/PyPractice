"""
Exercise (1). 已知一个长度为 n 的数组和一个正整数 k，并且最多只能使用一个用于交换数组元素的附加空间单元，
              试设计算法得到原数组循环右移 k 次的结果并分析算法的时间复杂度。
"""

"Method 1 利用切片实现，最为高效，时间复杂度为O(1)，需要两个空间单元存储"
def shift1(array, k):
  return array[-k:] + array[:-k]  # 左移k为负，右移k为正，去掉这里k前的负号就相反


"Method 2 速度慢，时间复杂度为O(n^2)，需要一个空间单元存储"
def shift2(array, k):
    temp = array[:]
    for i in range(k):
        temp.insert(0, temp.pop(-1))
    return temp

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
print(shift1(array, 5))
print(shift2(array, 6))


