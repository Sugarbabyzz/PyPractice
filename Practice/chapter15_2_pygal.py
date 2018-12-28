#****** 15.4 使用Pygal模拟掷骰子 ******
#  使用Python可视化包Pygal来生成可缩放的矢量图形文件
#   对于需要在尺寸不同的屏幕上显示的图表，很有效，因为能够自动缩放，以适合观看者的屏幕
#   若要以在线方式使用图表，请考虑Pygal来生成，这样在任何设备上显示时都会很美观

#   掷骰子：同时掷两个骰子，某些点数出现的可能性将比其他点数大。
#          为确定哪些点数出现的可能性最大，我们将生成一个表示掷骰子结果的数据集，并根据结果绘制出一个图形
import pygal

# 1、安装Pygal
''' pip3 install --user pygal==1.7 '''

# 2、Pygal画廊
''' 
    要了解使用Pygal可创建什么样的图表，查看图表类型画廊：
    访问http://www.pygal.org/，单机Documentation，再单机Chart types。 每个示例都包含源代码。
'''

# 3、创建Die类
from random import randint
# 函数randint()传入两个实参，起始值和终止值，返回一个两值之间的随机数
class Die():
    """ 表示一个骰子的类 """

    def __init__(self, num_sides=6):
        """ 骰子默认为6面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回一个位于1和骰子面数之间的随机值 """
        return randint(1, self.num_sides)

# 4、掷骰子
'''
# 实例化一个筛子
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
# 最后，将图表渲染为一个SVG文件，这种文件的扩展名必须为.svg
# 查看生成的直方图，最简单的方式是使用Web浏览器
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(results)
print(frequencies)
'''

# 5、分析结果 （已添加在上面）
#   为分析结果，计算出每个点数出现的次数

# 6、绘制直方图  （已添加在上面）
#   有了频率列表后，就可以绘制一个表示结果的直方图
#   直方图（histogram）：是一种条形图，指出了各种结果出现的频率

# 7、同时掷两个骰子
'''
# 实例化两个骰子
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for value in range(2,max_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
# 最后，将图表渲染为一个SVG文件，这种文件的扩展名必须为.svg
# 查看生成的直方图，最简单的方式是使用Web浏览器
hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual_of_two_D6.svg')

print(results)
print(frequencies)

# 结果：2或12可能性最小，中间的7可能性最大
'''

# 8、同时掷两个面数不同的骰子
#   下面创建一个6面骰子和一个10面骰子，看看掷50000次的结果
# 实例化两个骰子
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for value in range(2,max_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值）
# 最后，将图表渲染为一个SVG文件，这种文件的扩展名必须为.svg
# 查看生成的直方图，最简单的方式是使用Web浏览器
hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual_of_a_D6_and_a_D10.svg')

print(results)
print(frequencies)



# 结果：可能性最大的点数不是一个，而是5个。
# 因为出现最小点数和最大点数的组合都只有一种，而中间点数的组合数有6种
