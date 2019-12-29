"""
    这个虽然短，但是有问题。
    更换mid求的公式，结果会出问题。
    去掉24行代码，结果会出问题。
"""


# get max
def get_max_of_domino(L, R, W, left, right):
    if right - left == 1:
        return R[left] * L[right]
    else:
        mid = int((right - left)/2) + left  # +1为了向上取整
        # swap before
        wmid = W[mid]
        maxl = get_max_of_domino(L, R, W, left, mid)
        maxr = get_max_of_domino(L, R, W, mid, right)
        max1 = maxl + maxr
        # swap
        tmp = L[mid]
        L[mid] = R[mid]
        R[mid] = tmp
        # swap after
        W[mid] = wmid ^ 1
        maxl = get_max_of_domino(L, R, W, left, mid)
        maxr = get_max_of_domino(L, R, W, mid, right)
        max2 = maxl + maxr
        # compare
        if max2 > max1:
            W[mid] = wmid ^ 1
            return max2
        else:
            return max1


# main
if __name__ == '__main__':
    L, R, W = [], [], []
    # n = 6  # 设置序列长度
    # initial_domino(L, R, W, n)  # 初始化多米诺骨牌序列
    R = [0, 8, 2, 6, 7, 9, 10, 0]
    L = [0, 5, 4, 9, 7, 3, 11, 0]
    W = [0, 0, 1, 1, 0, 0, 1, 0]
    n = 6
    max_number = get_max_of_domino(L, R, W, 0, n+1)  # 得到最大值
    print(max_number)
    print(W)



