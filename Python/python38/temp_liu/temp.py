# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import pandas as pd
import numpy as np
import os

path = r'H:/Monarch/Data/'
os.chdir(path)
columns = ['Station', 'Year', 'Month', 'Day', 'APRE', 'DMXP', 'DMNP', 'TAVG', 'TMAX', 'TMIN', 'AVRH', 'MNRH',
           'PRCP', 'MEWS', 'MXWS', 'DMWS', 'EXWS', 'DEWS', 'SOHR']
types = ['PRCP', 'TAVG', 'TMAX', 'TMIN']

with open(r'ghcnd-stations.txt', encoding='utf-8') as fp:
    lines = fp.readlines()
    select = []
    for line in lines:
        select.append(line.split())
select = pd.DataFrame(select).iloc[:, :3].set_index(0).astype('float')
select = select[(select[2] >= 40) & (select[2] <= 100) & (select[1] >= 35) & (select[1] <= 57)]
for year in range(2019, 2021):
    data = []
    file = '{0}.csv'.format(year)
    Pieces = pd.read_csv(file, usecols=[0, 1, 2, 3], header=None, chunksize=1000000)
    mask = pd.read_csv(r'all{0}.txt'.format(year), header=None, usecols=[0])
    for j, df in enumerate(Pieces):
        df.columns = ['Station', 'date', 'type', 'value']
        df = df[df['type'].isin(types)]
        df = df[df['Station'].isin(select.index)]
        df = df[~df['Station'].isin(mask[0])]
        df1 = df.set_index(['Station', 'date', 'type'])
        df1 = df1/10
        df2 = df1.unstack()
        df2.columns.names = ['value', 'type']
        df3 = df2.stack('value').reset_index()
        df3['Year'] = df3['date'] // 10000
        df3['Month'] = df3['date'] % 10000 // 100
        df3['Day'] = df3['date'] % 100
        df4 = df3.drop(['value', 'date'], axis=1)
        ret = list(set(columns) ^ set(df4.columns))
        for i in ret:
            df4[i] = 32766
        df5 = df4[columns]
        df6 = df5.replace(np.nan, 32766)
        data.append(df6)
    df7 = pd.concat(data)
    df7.to_csv(f'Asia_{year}.txt', header=False, index=False, float_format='%.2f')


