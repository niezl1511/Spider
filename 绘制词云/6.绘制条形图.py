import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import *

font = FontProperties(fname='C:\simkai.ttf', size=14)  # 解决中文乱码问题

fig = plt.figure(1)  # 第一步，取出一张白纸

ax1 = plt.subplot(111)  # 第二步，确定绘图范围

# 第三步，准备绘制的数据
data = np.array([1944, 2206, 1982, 1616, 2195, 1803, 2793, 3631, 5212, 9000, 13142, 14854, 16014])

# 第四步，准备绘制条形图，思考绘制条形图需要确定那些要素
# 1、绘制的条形宽度
# 2、绘制的条形位置(中心)
# 3、条形图的高度（数据值）
width = 0.3
x_bar = np.arange(13)

# 第五步，绘制条形图的主体，条形图实质上就是一系列的矩形元素，我们通过plt.bar函数来绘制条形图
rect = ax1.bar(left=x_bar, height=data, width=width, color="lightblue")

# 第六步，向各条形上添加数据标签
for rec in rect:
    x = rec.get_x()
    height = rec.get_height()
    ax1.text(x + 0.1, 1.02 * height, str(height))

# 第七步，绘制x，y坐标轴刻度及标签，标题
ax1.set_xticks(x_bar)
ax1.set_xticklabels(("2017.9", "10", "11", "12", "01", "02", "03", "04", "05", "06", "07", "08", "2018.9"))
ax1.set_ylabel(u"频数", fontproperties=font)
ax1.set_title(u" 2017.09月-2018.09月问题数条形图", fontproperties=font)
ax1.grid(True)
ax1.set_ylim(0, 17000)
plt.show()



