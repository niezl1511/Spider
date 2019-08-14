from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams


def cleanInput(input):
    input = re.sub('\n+', " ", input)  # 去除换行符
    input = re.sub('\[[0-9]*\]', "", input)  # 去除带中括号的数字
    input = re.sub('[0-9]', "", input)  # 去除数字
    input = re.sub('[，。.、！：%；”“\[\]]', "", input)  # 去除中文标点符号
    input = re.sub(' +', " ", input)  # 去除空格
    input.strip(string.punctuation)  # 去除英文标点符号
    return input


def getngrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input) - n + 1):
        newNGram = "".join(input[i:i + n])  # 以指定字符串连接生成新的字符串
        if newNGram in output:
            output[newNGram] += 1  # 如果字符出现过则加1
        else:
            output[newNGram] = 1  # 没出现过则设置为1
    return output


html = urlopen("http://news.ifeng.com/a/20170305/50754278_0.shtml")
bsObj = BeautifulSoup(html, "lxml")
content = bsObj.find("div", {"id": "main_content"}).get_text()
ngrams = getngrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))

datafile = open("2017report.txt", 'w+')
count = []
count_label = []
for k in ngrams:
    print("(%s,%d)" % (k, ngrams[k]))
    datafile.write("(%s,%d)\n" % (k, ngrams[k]))
    if (ngrams[k] > 30):
        count.append(ngrams[k])
        count_label.append(k)
x = np.arange(len(count)) + 1
fig1 = plt.figure(1)
rects = plt.bar(x, count, width=0.5, align="center", yerr=0.001)
plt.title('2017政府工作报告词频统计')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.03 * height, '%s' % int(height))


autolabel(rects)
plt.xticks(x, count_label, rotation=90)
# plt.xticks(x,count_label)
plt.show()
