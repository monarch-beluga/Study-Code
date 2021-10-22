# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: data_year_to_day.py
@function:
@modify:
"""

import pandas as pd
import numpy as np
import os

path = r'H:\Monarch\Data'
os.chdir(path)
type_me = ['TMN', 'TMX', 'PRE', 'RHU', 'SSD', 'WIN', 'TEM']
types = ['TMIN', 'TMAX', 'PRCP', 'RHU', 'SSD', 'WIN', 'TAVG']
columns = ['Station', 'Year', 'Month', 'Day', 'APRE', 'DMXP', 'DMNP', 'TEM', 'TMX', 'TMN', 'RHU', 'MNRH',
           'PRE', 'WIN', 'MXWS', 'DMWS', 'EXWS', 'DEWS', 'SSD']

for year in range(2018, 2019):
    t_d = 28
    if year % 4 == 0:
        t_d = 29
    days = [31, t_d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    column = ["{0}_{1}".format(i+1, k+1) for i, j in enumerate(days) for k in range(j)]

    data = []
    for t in range(len(type_me)):
        # df1 = pd.read_csv(f'MeteoDaily8012/{type_me[t]}/{type_me[t]}_{year}.csv', sep=',', header=None)
        # df1[0] = 'CH0000' + df1[0].astype('str')
        # df1.set_index(0, inplace=True)
        # df1 = df1.iloc[:, 3:]
        # df1[(df1 == 32700) | (df1 == 32766)] = np.nan
        # df1.columns = column
        # if year >= 1990:
        df = pd.read_csv(f'meteodata/{types[t]}/{types[t]}_{year}.txt', sep='\t', header=None, index_col=0).iloc[:, 3:]
        df = df[df.index.str[:6] == 'CH0000']
        df[df == -9999] = np.nan
        df.columns = column
        # df = df[~df.index.isin(df1.index)]
        # df1 = pd.concat([df1, df])
        df2 = df.stack().to_frame()
        df2.rename_axis(index=['Station', 'date'], inplace=True)
        df2.columns = [type_me[t]]
        df2.reset_index(inplace=True)
        if t == 0:
            data = df2
        else:
            data = pd.merge(data, df2, how='outer', on=['Station', 'date'])

    data['Year'] = year
    a = data['date'].str.split('_').str
    data['Month'] = a[0].astype('int')
    data['Day'] = a[1].astype('int')
    data.drop('date', axis=1, inplace=True)
    data[['TMN', 'TMX', 'SSD', 'TEM']] = data[['TMN', 'TMX', 'SSD', 'TEM']]/10
    ret = list(set(columns) ^ set(data.columns))
    for i in ret:
        data[i] = 32766
    data.replace(np.nan, 32766, inplace=True)
    data1 = data[columns]
    data1.to_csv(f'H:/Monarch/Data/数据库入库文件/气象数据/CH_{year}.txt', header=False, index=False, float_format='%.2f')
    print(f'{year} export success !!!')

