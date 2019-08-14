#!C:\Python36\python.exe
# -*- coding:utf-8 -*-
'''
@Time    : 2018/6/27 9:30
@Author  : Fate
@File    : 03绘制词云.py
'''

from wordcloud import WordCloud, STOPWORDS  # 词云

from matplotlib import pyplot as plt  # 数据视图

import jieba  # 分词

from PIL import Image  # 图片处理

import numpy as np  # 科学计算

jobInfo = open("妇科.txt", 'r', encoding='GBK').read()
# print(jobInfo)


# 分词
jobInfoCut = jieba.cut(jobInfo, cut_all=True)
jobInfoCut = ' '.join(jobInfoCut)
print(jobInfoCut)

# RGB底色
bg = np.array(Image.open('44.jpg'))
print(bg)

myworlcloud = WordCloud(font_path='simkai.ttf',  # 中文字体
                        width=400, height=200,
                        mask=bg,  # 字体底色
                        scale=1,  # 缩放
                        max_words=300,  # 最大词语数量
                        min_font_size=4,  # 最小字体大小
                        stopwords=STOPWORDS,  # 停止词
                        random_state=30,  # 字体随机状态，单位°
                        background_color='white',  # 背景颜色
                        max_font_size=200  # 最大字体大小
                        ).generate(jobInfoCut)  # 生成词云

# plt.imshow(myworlcloud)  # 绘制
# plt.show()  # 显示
plt.figimage(myworlcloud)
plt.imsave('妇科.png', myworlcloud)
# plt.imsave('不孕不育-悬赏问题词云.png', myworlcloud)


