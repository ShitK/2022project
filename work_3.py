# -*- coding: UTF-8 -*-

import pandas as pd
import xlrd
import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar
import matplotlib.pyplot as plt

from pyecharts.globals import CurrentConfig


CurrentConfig.ONLINE_HOST = "C:\\Users\\Lenovo\\Desktop\\learn_pytorch\\kang_homework\\pyecharts-assets-master\\pyecharts-assets-master\\assets"
# CurrentConfig.ONLINE_HOST = 'D:/python/pyecharts-assets-master/assets/'

# 提取编程语言名字
name = list(pd.read_excel('average.xlsx')['Programing'].drop_duplicates())#['Programing'].drop_duplicates()
print(name)
data = xlrd.open_workbook('average.xlsx')

table = data.sheets()[0]
print(table.nrows)
dic1 = {k: [] for k in name}
# 各编程语言对应每年里不同时间的热度
for i in range(1, table.nrows):
    x = table.row_values(i)
    print(x)
    dic1[x[0]].append((int(x[1]), x[2]))
print(dic1['Python'][0][1])
def all_year_chart(names) :
    year = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
            '2022']
    datas_list = []

    for i in range(14):
        temp_list = []
        datas_list.append(temp_list)
    names = name
    #(m,n) = dic1[name]
    for i in range(14):
        for j in range(10):
            datas_list[j].append(dic1[name[j]][i][1])
    name_ = year
    #折线
    color = ['#00BFFF', '#0000CD', '#000000', '#008000', '#FF1493', '#FFD700', '#FF4500', '#00FA9A', '#191970',
             '#9932CC']
    plt.figure(figsize=(30, 8))
    for k in range(10):
        plt.plot(name_, datas_list[k], color=color[k], marker='D', markersize=5, label="{:}".format(name[k]))
    plt.xlabel('years', fontsize=20)
    plt.ylabel('average heats', fontsize=20)
    plt.legend()
    plt.show()
all_year_chart(name)
