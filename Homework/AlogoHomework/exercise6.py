"""
    Exercise6：用动态规划实现Exercies3，时间复杂度O(n).
"""
'''
    思路：
    1、首先将问题分割为子问题，求 max(Σ(i-1)(k=1) R[k]L[k+1])。
      用二维数组M记录子问题结果，原问题求解目标：max(M[0,n], M[1,n])
    2、建立子问题求解递推方程：
      设第i块骨牌上左右两个数为ai, bi, 则：
        1）  M[0,1] = M[1,1] = 0
        2）  M[0, i+1] = max{(M[0, i] + bi*ai+1), (M[1, i] + ai*ai+1)}
            M[1, i+1] = max{(M[0, i] + bi*bi+1), (M[1, i] + ai*bi+1)}
'''
import numpy


def get_max_of_domino(L, R, W, n):
    M = numpy.zeros([2, 7])  # 存储子问题结果
    P = numpy.zeros([2, 7])
    ab = numpy.zeros([2, 7])  # 临时存储第i个骨牌左右两个值a和b

    for i in range(1, 6):
        if W[i] == 0:
            ab[0, i] = L[i]
            ab[1, i] = R[i]
        else:
            ab[0, i] = R[i]
            ab[1, i] = L[i]
        if W[i+1] == 0:
            ab[1, i + 1] = R[i + 1]
            ab[0, i + 1] = L[i + 1]
        else:
            ab[1, i + 1] = L[i + 1]
            ab[0, i + 1] = R[i + 1]

        if (M[0, i] + ab[1, i]*ab[0, i+1]) > (M[1, i] + ab[0, i] * ab[0, i+1]):
            M[0, i+1] = M[0, i] + ab[1, i]*ab[0, i+1]
            P[0, i+1] = 0
        else:
            M[0, i + 1] = M[1, i] + ab[0, i] * ab[0, i + 1]
            P[0, i + 1] = 1

        if (M[0, i] + ab[1, i]*ab[1, i+1]) > (M[1, i] + ab[0, i] * ab[1, i+1]):
            M[1, i+1] = M[0, i] + ab[1, i]*ab[1, i+1]
            P[1, i+1] = 0
        else:
            M[1, i + 1] = M[1, i] + ab[0, i] * ab[1, i + 1]
            P[1, i + 1] = 1

    if M[0, n] > M[1, n]:
        result = M[0, n]
        W[n] = 0
    else:
        result = M[1, n]
        W[n] = 1

    for i in range(n, 2, -1):
        W[i - 1] = P[0, i] if W[i] == 0 else P[1, i]

    return result


if __name__ == '__main__':
    R = [0, 8, 2, 6, 7, 9, 10, 0]
    L = [0, 5, 4, 9, 7, 3, 11, 0]
    W = [0, 0, 1, 1, 0, 0, 1, 0]
    max_number = get_max_of_domino(L, R, W, 6)  # 得到最大值
    print(max_number)
    print(W)