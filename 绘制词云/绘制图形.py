# coding:utf-8
# 导入读取Excel的库
import xlrd

# 导入需要读取Excel表格的路径
data = xlrd.open_workbook(r'测试.xlsx')
table = data.sheets()[0]
y = ''
# 将列的值存入字符串
y = table.col_values(2)  # 读取列的值
# 导入pyechats库
from pyecharts import Bar
import numpy as np

t = np.linspace(1, 1000000, len(y))  # 等间隔取值
bar = Bar("文章阅读量展示", "统计如下")  # 主副标题
bar.add("博客文章阅读量折线图展示", t, y, is_more_utils=True)  # 标题
bar.show_config()  # 展示HTML源代码
bar.render(r"bokezhexiantu.html")  # 保存到本地bokezhexiantu.html




