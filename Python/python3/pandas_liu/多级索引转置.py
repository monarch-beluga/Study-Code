# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/07
@file: 多级索引转置.py
@function:
@modify:
"""
import pandas as pd
import numpy as np
from glob import glob

temp = r'E:\Data\all2019.txt'
df = pd.read_csv(temp, header=0)
df.set_index(['台站', '年', '月', '日'], inplace=True)
for year in range(2015, 2019):
    files = glob(r'E:\Data\气象\*{0}*.txt'.format(year))
    t_d = 28
    if year % 4 == 0:
        t_d = 29
    types = ['降水量', '平均相对湿度', '日照时数', '平均气温', '日最高气温', '日最低气温', '平均风速']

    days = [31, t_d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    column = ["{0}_{1}".format(i+1, k+1) for i, j in enumerate(days) for k in range(j)]
    data = 0
    for i in range(7):
        df1 = pd.read_csv(files[i], header=None, index_col=0, sep='\t')
        df2 = df1.iloc[:, 3:]
        df2.columns = column
        df3 = df2.stack().to_frame()
        df3.columns = [types[i]]
        df3.rename_axis(index=['台站', '日期'], inplace=True)
        df3.reset_index(inplace=True)
        df3 = df3[df3['台站'].str.contains('CH')]
        if i == 0:
            data = df3
        else:
            data = pd.merge(data, df3, how='outer', on=['台站', '日期'])

    data['年'] = year
    data['月'], data['日'] = data['日期'].str.split('_').str
    data['月'] = data['月'].astype('int')
    data['日'] = data['日'].astype('int')
    data.drop('日期', axis=1, inplace=True)
    data.set_index(['台站', '年', '月', '日'], inplace=True)
    data.replace([np.nan, -9999], -99990, inplace=True)
    data = data/10
    data.replace(-9999, np.nan, inplace=True)
    data = data.dropna(axis=0, how='all')
    ret = list(set(df.columns) ^ set(data.columns))
    for i in ret:
        data[i] = 'null'
    data1 = data[df.columns]
    data1.reset_index(inplace=True)
    data1 = data1.round(decimals=1)
    df_sort = data1.sort_values(by=['月', '台站', '日'], ascending=(True, True, True))
    df_sort.replace(np.nan, 'null', inplace=True)
    df_sort.to_csv(r'E:/Data/all{0}.txt'.format(year), header=False, index=False)

