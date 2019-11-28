"""
    Exercise (3). 现有 n 块“多米诺骨牌” s1, s2, · · · , sn 水平放成一排，每块骨
        牌 si 包含左右两个部分，每个部分赋予一个非负整数值，如下图所示为包含 6
        块骨牌的序列。骨牌可做 180 度旋转，使得原来在左边的值变到右边，而原来
        在右边的值移到左边，假设不论 si 如何旋转，L[i] 总是存储 si 左边的值，R[i]
        总是存储 si 右边的值，W [i] 用于存储 si 的状态:当 L[i] ≤ R[i] 时记为 0，否
        则记为 1，试采用分治法设计算法求 ∑n−1 R[i] · L[i + 1] 的最大值，以及当取 i=1
        得最大值时每个骨牌的状态。下面是 n = 6 时的一个例子。
"""
"""
    思路： 首先，需要对原序列进行结构补全，添加一个R[0]和L[n+1]。
          然后，将该问题分为两个子问题，分治解决，即原始序列分为两个子序列进行处理，递归求子序列最大乘积和，将L和R的位置作相应调整。
"""
import random


# initial
def initial_domino(L, R, W, n):
    R.append(0)  # 0位补0
    L.append(0)
    W.append(0)
    for i in range(1, n+1):  # 随机生成其中的n个数
        L.append(random.randint(1, 15))
        R.append(random.randint(1, 15))
        if L[i] > R[i]:
            W.append(1)
        else:
            W.append(0)
    L.append(0)  # n+1位补0
    R.append(0)
    W.append(0)
    print(L)
    print(R)
    print(W)


# get max
def get_max_of_domino(L, R, W, left, right):
    if right-left == 0:
        return 0
    elif right-left == 1:
        return R[left] * L[right]
    else:
        mid = int((left + right + 1) / 2)  # +1为了向上取整
        # print(mid)

        if L[mid] > R[mid]:  # W[mid] == 1 的情况
            maxl1 = get_max_of_domino(L, R, W, left, mid)
            maxr1 = get_max_of_domino(L, R, W, mid, right)
            max1 = maxl1 + maxr1
            tmp = L[mid]  # swap
            L[mid] = R[mid]
            R[mid] = tmp
            maxl0 = get_max_of_domino(L, R, W, left, mid)
            maxr0 = get_max_of_domino(L, R, W, mid, right)
            max0 = maxl0 + maxr0
            if max1 > max0:
                W[mid] = 1
                return max1
            else:
                W[mid] = 0
                return max0
        else:  # W[mid] == 0 的情况
            maxl0 = get_max_of_domino(L, R, W, left, mid)
            maxr0 = get_max_of_domino(L, R, W, mid, right)
            max0 = maxl0 + maxr0
            tmp = L[mid]
            L[mid] = R[mid]
            R[mid] = tmp
            maxl1 = get_max_of_domino(L, R, W, left, mid)
            maxr1 = get_max_of_domino(L, R, W, mid, right)
            max1 = maxl1 + maxr1
            if max1 > max0:
                W[mid] = 1
                return max1
            else:
                W[mid] = 0
                return max0


# main
if __name__ == '__main__':
    L, R, W = [], [], []
    n = 2  # 设置序列长度
    initial_domino(L, R, W, n)  # 初始化多米诺骨牌序列
    max_number = get_max_of_domino(L, R, W, 0, n+1)  # 得到最大值
    print(max_number)



