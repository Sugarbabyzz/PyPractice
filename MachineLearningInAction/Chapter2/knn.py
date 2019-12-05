import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

'''
KNN步骤：
1、计算当前点与已知类别数据集中的点的距离
2、按照距离递增次序排序
3、选取与当前点距离最小的k个点
4、确定前k个点所在类别出现的频率
5、选取出现频率最高的类别作为预测类别
'''


# 创建数据集
def createDataSet():
    group = np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# 实现欧式距离计算： (（xA0-xB0)^2 + (xA1-xB1)^2 )^0.5
def classify0(inX, dataSet, labels, k):
    # inX 输入向量是个一维两位的向量，
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet  # np.tile （1,x)横向复制  (x,1)纵向复制
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()  # 将数组排序后，将其索引组成新数组返回
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1   # dict.get方法，获取指定的键，不存在则返回默认值0
    sortedClassCount = sorted(classCount.items(), key=lambda x: x, reverse=True)  # 根据dict的值进行降序排列
    # print(classCount)
    # print(sortedClassCount)
    return sortedClassCount[0][0]


def file2matrix(filename):
    # fr = open(filename)
    # arrayLines = fr.readlines()
    # lenOfLines = len(arrayLines)
    # returnMat = np.zeros((lenOfLines, 3))
    # classLabelVector = []
    # index = 0
    # for line in arrayLines:
    #     line = line.strip()
    #     listFromLine = line.split('\t')
    #     returnMat[index, :] = listFromLine[0:3]
    #     classLabelVector.append(int(listFromLine[-1]))
    #     index += 1
    # print(type(returnMat))
    # print(type(classLabelVector))

    # 上面是书上的写法，太繁琐了，用dataframe更简洁
    # returnMat存储三个特征，narray类型 ； classLabelVector存储目标变量，list类型。
    df = pd.read_csv(filename, header=0, names=['飞机', '游戏', '冰淇淋', '类别'], sep='\t')
    returnMat = df[['飞机', '游戏', '冰淇淋']].values
    classLabelVector = df['类别'].values.tolist()
    return returnMat, classLabelVector


# 归一化公式： newValue = (oldValue - min) / (max - min)
def autoNorm(dataSet):
    minVal = dataSet.min(0)  # 选取每列的最小值   0为列，1为行
    maxVal = dataSet.max(0)
    ranges = maxVal - minVal
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVal, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVal


# 对数据集进行测试
def datingClassTest():
    hoRatio = 0.10  # 选取10%作为测试集
    datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat, ranges, minVal = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVec = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVec):
        # 将numTestVec条作为测试集送入KNN分类器。   每次用numTextVec:m条数据作为训练集。
        classifierResult = classify0(normMat[i, :], normMat[numTestVec:m, :], datingLabels[numTestVec:m], 3)
        print('Classified Result: %d and Real Answer is: %d' % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0

    print('error rate : %f' % (errorCount/numTestVec))
    print('errorcount : ' + str(errorCount))


# 使用算法
def classifyPersion():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentOfGames = float(input("The percent of time spent playing game?"))
    flyMiles = float(input("Miles fly a year?"))
    iceCream = float(input("icecream ate?"))
    datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    normMat, ranges, minVal = autoNorm(datingDataMat)
    inArr = np.array([flyMiles, percentOfGames, iceCream])
    print()
    result = classify0((inArr-minVal)/ranges, normMat, datingLabels, 3)
    print('The classifier result is : ' + resultList[result - 1])



if __name__ == '__main__':
    # 1、knn分类器实现
    # group, labels = createDataSet()
    # inX = [[0, 0]]
    # result = classify0(inX, group, labels, 3)
    # print(result)

    # 2、改进约会网站
    # datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
    #            15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
    # plt.show()  # 选前两列特征，画图
    # # 数值之间差值过大，进行归一化处理 (0, -1)
    # normDataSet, ranges, minVal = autoNorm(datingDataMat)
    # print(normDataSet)
    # 测试
    # datingClassTest()

    # 使用
    classifyPersion()


