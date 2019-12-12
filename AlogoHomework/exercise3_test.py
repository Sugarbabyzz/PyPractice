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


def initial_domino(L, R, W, n):
    L.append(0)
    R.append(0)
    W.append(0)
    for i in range(n):
        L.append(random.randint(1, 15))
        R.append(random.randint(1, 15))
        if L[i+1] > R[i+1]:
            W.append(1)
        else:
            W.append(0)
    L.append(0)
    R.append(0)
    W.append(0)


def get_max_value(L, R, W, left, right):

    # if right-left == 0:
    #     return 0
    if right-left == 1:
        return R[left]*L[right]
    else:
        mid = int((left+right+1) >> 1)
        # 这种写法也可以得到正确结果，但是无法得到W的值了
        maxl = get_max_value(L, R, W, left, mid)
        maxr = get_max_value(L, R, W, mid, right)
        max_before = maxl + maxr
        tmp = R[mid]
        R[mid] = L[mid]
        L[mid] = tmp
        maxl = get_max_value(L, R, W, left, mid)
        maxr = get_max_value(L, R, W, mid, right)
        max_after = maxl + maxr
        if max_before > max_after:
            return max_before
        else:
            return max_after


if __name__ == '__main__':
    # L, R, W = [], [], []
    # n = 2
    # initial_domino(L, R, W, n)
    # L = [0, 5, 4, 9, 7, 3, 11, 0]
    # R = [0, 8, 2, 6, 7, 9, 10, 0]
    # W = [0, 0, 1, 1, 1, 0, 1, 0]
    # n = 6
    L = [0, 1, 5, 3, 0]
    R = [0, 2, 4, 1, 0]
    W = [0, 0, 0, 0, 0]
    n = 3
    print(L)
    print(R)
    print(W)
    max_value = get_max_value(L, R, W, 0, n+1)
    print(max_value)


