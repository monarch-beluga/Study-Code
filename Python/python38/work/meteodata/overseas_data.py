# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: overseas_data.py
@function:
@modify:
"""

import pandas as pd
from concurrent.futures.thread import ThreadPoolExecutor
import os
import numpy as np
import gzip

path = r'H:\Monarch\Data\me_data'
os.chdir(path)
columns = ['Station', 'Year', 'Month', 'Day', 'APRE', 'DMXP', 'DMNP', 'TAVG', 'TMAX', 'TMIN', 'AVRH', 'MNRH',
           'PRCP', 'AWND', 'WSF2', 'WDF2', 'WSFI', 'WDFI', 'TSUN']
types = ['PRCP', 'TAVG', 'TMAX', 'TMIN', 'AWND', 'TSUN', 'WSFI', 'WDFI', 'WSF2', 'WDF2']


def piece_handle(df):
    df.columns = ['Station', 'date', 'type', 'value']
    df = df[df['type'].isin(types)]
    df = df[~(df['Station'].str[:6] == 'CH0000')]
    df1 = df.set_index(['Station', 'date', 'type'])
    df1 = df1 / 10
    df2 = df1.unstack()
    df2.columns.names = ['value', 'type']
    df3 = df2.stack('value').reset_index()
    df3['TSUN'] = df3['TSUN'] / 6
    df3['Year'] = df3['date'] // 10000
    df3['Month'] = df3['date'] % 10000 // 100
    df3['Day'] = df3['date'] % 100
    df4 = df3.drop(['value', 'date'], axis=1)
    ret = list(set(columns) ^ set(df4.columns))
    for i in ret:
        df4[i] = 32766
    df5 = df4[columns]
    df6 = df5.replace(np.nan, 32766)
    return df6


def data_handle(year):
    gz_file = f'{year}.csv.gz'
    csv_file = f'{year}.csv'
    with gzip.GzipFile(gz_file) as gf:
        with open(csv_file, 'wb+') as fp:
            fp.write(gf.read())
    pieces = pd.read_csv(csv_file, usecols=[0, 1, 2, 3], header=None, chunksize=3000000)
    with ThreadPoolExecutor(max_workers=30) as worker:
        data = worker.map(piece_handle, pieces)
    data = pd.concat(data)
    data.drop_duplicates(subset=['Station', 'Year', 'Month', 'Day'], keep='first', inplace=True)
    data.to_csv(f'result/overseas_{year}.txt', header=False, index=False, float_format='%.2f')
    print(f'{csv_file} 处理完成!!!')
    os.remove(csv_file)

