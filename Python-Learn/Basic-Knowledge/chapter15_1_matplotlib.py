
#  matplotlib,是一个数学绘图库，可以使用它来制作简单的图表
#  Pygal包，可以生成适合在数字设备上显示的图表，在与用户与图表交互时突出元素以及调整其大小

#****** 15.1 安装matplotlib ******
'''
pip3 install --user matplotlib
'''

#****** 15.2 绘制简单的折线图******
#  导入pyplot模块，并指定别名plt
import matplotlib.pyplot as plt
'''
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()
'''
# 1、修改标签文字和线条粗细
'''
#   linewidth 决定绘制的线条的粗细
plt.plot(squares, linewidth=5)
# 设置图表标题，并给坐标轴加上标签
#   title 给图表指定标题；xlabel，ylabel 为每条轴设置标题； tick_parm 设置刻度的样式,both将同时影响x，y轴
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
'''

# 2、校正图形
#   折线图默认第一个数据点对应的x坐标值为0，但我们的第一个点对应的是1
#   为了改变这种默认行为，可以给plot()同时提供输入值和输出值
'''
input_valuse = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_valuse, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
'''

# 3、使用scatter()绘制散点图并设置其样式
'''
plt.scatter(2, 4, s=200)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Suare of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''

# 4、使用scatter()绘制一系列点
'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16,25]

plt.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标轴指定标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Suare of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
'''

# 5、自动计算数据
#   手工计算列表包含的值效率低下，可以让Python循环替我们完成这种计算
'''
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# 设置图表标题并给坐标轴指定标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
#   函数axis()要求提供四个值：x和y坐标轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])

plt.show()
'''
# 6、删除数据点的轮廓
#   默认为蓝色点和黑色轮廓
#   绘制很多点时，黑色轮廓可能会粘连在一起
#   删除数据点的轮廓，可在调用scatter()时传递实参edgecolor='none'
'''
plt.scatter(x_values, y_values, edgecolors='none', s=40)
'''

# 7、自定义颜色
'''
#   可向scatter()传递参数c，并将其设置为要使用的颜色的名称
plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
#   也可以使用RGB颜色模式自定义颜色，传递参数c，将其设置为一个元组，分别表示红色，绿色和蓝色分量
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
'''

# 8、使用颜色映射
#   颜色映射：是一系列颜色，从起始颜色渐变到结束颜色
#    在可视化中，颜色映射用于突出数据的规律。
#    较浅的颜色来显示较小的数，并使用较深的颜色来显示较大的数
#    将参数c设置成了一个y值的列表，并使用参数cmap告诉pyplot使用哪个颜色映射
'''
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
'''

# 9、自动保存图表
#   要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用
#   第一个实参指定要以书面样的文件名保存图表，将存储到当前.py文件所在的目录
#   第二个实参指定将图表多余的空白区域裁剪掉
'''
plt.savefig('squares_plot.png', bbox_inches='tight')
'''



#****** 15.3 随机漫步 ******
#  随机漫步：每次行走都完全是随机的，没有明确的方向，结果是由一系列随机决策决定的

# 1、创建RandomWalk()类
#   为模拟随机漫步，创建RandomWalk类，能随机地选择前进方向
#   需要三个属性，其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过每个点的x和y坐标
#   只包含两个方法：_init_()和fill_walk()，其中后者计算随机漫步经过的所有点
from random import choice
#   将所有可能的选择都存储在一个列表中，并在每次做决策时都使用choice()来决定使用哪种选择。
class RandomWalk():
    """ 一个生成随机漫步数据的类 """
    # 将随机漫步包含的默认点数设置为5000
    # 创建两个用于存储x和y值的列表，并让每次漫步都从（0，0）出发
    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步包含的所有点 """

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])       # 1-右 -1-左
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])       # 1-上 -1-下
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

# 2、选择方向 （添加入RandomWalk类中）
#   使用fill_walk()来生成漫步包含的点，并决定每次漫步的方向

# 3、绘制随机漫步图
#   创建一个RandomWalk实例，并将其包含的点都绘制出来
'''
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
'''

# 4、模拟多次随机漫步
#   只要程序处于活动状态，就不断模拟随机漫步
'''
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
'''

# 5、设置随机漫步图的样式
#   定制图表，突出每次漫步的重要特种，让分散注意力的元素不那么显眼
#   突出元素：漫步的起点、终点和经过的路径
#   不突出元素：刻度标记和标签
#   最终的结果是简单的可视化表示，清楚地指出每次漫步经过的路径

# 6、给点着色
#   颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓
while True:
    rw = RandomWalk(50000)  # 增加至50000
    rw.fill_walk()

    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色，单位为英寸
    plt.figure(dpi=128, figsize=(10, 6))

    # range()生成一个数字列表，其中包含的数字个数与漫步包含的点数相同
    # 接着将列表存储在point_numbers中，以便后面使用它来设计每个漫步点的颜色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)

    # 突出起点和终点
    # 起点-绿色，终点-红色
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break

# 7、重新绘制起点和终点 （添加在上面）
#   除了指出先后顺序外，还应呈现随机漫步的起点和终点，使其变得更大，并显示为不同的颜色

# 8、隐藏坐标轴 （添加在上面）

# 9、增加点数 （添加在上面）

# 10、调整尺寸以适应屏幕 （添加在上面）

