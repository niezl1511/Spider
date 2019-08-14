import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd

labels = ['China', 'USA', 'EU', 'Japan', 'UK', 'France', 'Austrilia', 'Others']
data = np.array([0.12, 0.18, 0.15, 0.06, 0.03, 0.025, 0.015, 0.42])

plt.figure(figsize=(8, 8))
pie = plt.pie(data,
              labels=labels,   #labels参数设置每一块的标签
              labeldistance=1.2,  #labeldistance参数设置标签距离圆心的距离（比例值）
              explode=[0.2, 0, 0.1, 0, 0.2, 0, 0.1, 0],  #explode参数设置每一块顶点距圆形的长度（比例值）
              autopct='%0.2f%%',  #autopct参数设置比例值的显示格式(%1.1f%%)
              pctdistance=0.6,  #pctdistance参数设置比例值文字距离圆心的距离
              shadow=True, #shadow参数为布尔值，设置是否绘制阴影
              startangle=90)


# 2、按数值大小绘制饼状图

# x = [5,13,3]
# plt.pie(x,labels=['dog','pig','dragon'])
# plt.axis('equal')


plt.show()
