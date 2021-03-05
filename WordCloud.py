# -*- coding = utf-8 -*-
# @Time : 2021/2/1 15:29
# @Author : 张微
# @File : WordCloud.py
# @Software : PyCharm

import jieba
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import sqlite3

con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text=text+item[0]
# print(text)
cur.close()
con.close()
cut = jieba.cut(text)
string = "".join(cut)
print(len(string))
