# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 10:53
# @Author  : Monarch
# @File    : 国外站点合并.py
# @Software: PyCharm

from datetime import datetime
import numpy as np
import pandas as pd
import os

os.chdir(r'D:\Work\ECA\国外站点')

out_path = r'D:\Work\ECA\国外站点(合并)'
if not os.path.exists(out_path):
    os.mkdir(out_path)

sep = 16
for year in range(1980, 1990):
    df = pd.read_csv(f'{year}.txt', sep='\t', header=0)
    df['date'] = df['Year'] * 10000 + df['Month'] * 100 + df['Day']
    df['unique'] = df['date'].apply(lambda x:
                                    ((datetime.strptime(str(x), "%Y%m%d") -
                                      datetime.strptime(str(year), "%Y")).days) // sep * sep + year * 1000 + 1)
    df['MTEM'].replace(32766, np.nan, inplace=True)
    temp = df[['Station', 'unique', 'MTEM']]
    temp.set_index(['Station', 'unique'], inplace=True)
    data_mean = temp.groupby(temp.index)['MTEM'].mean()
    data = df[['Station', 'X', 'Y', 'unique']].drop_duplicates(subset=['Station', 'X', 'Y', 'unique'],
                                                               keep='first')
    data['MTEM'] = data_mean.values
    data.set_index(['Station', 'X', 'Y', 'unique'], inplace=True)
    data1 = data.unstack()
    data1.columns = data1.columns.levels[1]
    data1[np.isnan(data1)] = 32766
    data1.to_csv(f'{out_path}/{year}.txt', float_format='%.3f')

