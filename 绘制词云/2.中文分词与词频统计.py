import os, codecs
import jieba
from collections import Counter


def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')

    with open('./全部问题.csv', 'a+', encoding='utf-8') as f:
        for (k, v) in c.most_common(200):

            print("关键词：%s   出现次数：%d "% (k, v))
            f.write("{},{}\n".format(k, v))


if __name__ == '__main__':
    with codecs.open('./全部标签.txt', 'r', 'utf-8') as f:
        txt = f.read()
    get_words(txt)




