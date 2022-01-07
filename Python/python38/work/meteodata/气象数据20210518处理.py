# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/01/07
@file: 气象数据20210518处理.py
@function:
@modify:
"""

import pandas as pd
from glob import glob
import numpy as np
import os

os.chdir(r'E:\Work\气象数据20210518')
types = ['PRS', 'TEM', 'RHU', 'PRE', 'WIN', 'SSD']
rows = [[7, 8, 9], [7, 8, 9], [7, 8], [9], [7, 8, 9, 10, 11], [7]]
con = [2000, 50, 100, 2000, 1000, 24]
for year in [2020]:
    mask = pd.read_csv(f'E:/public/Data/all{year}.txt', header=None, usecols=[0])[0].unique()
    # t = types[5]
    # row = rows[5]
    # c = con[5]
    df = []
    for t, row, c in zip(types, rows, con):
        t_files = glob(f'{t}*{2020}*{2020}*/*{year}*.txt')
        data = []
        for f in t_files:
            with open(f, 'r') as fp:
                temp = pd.DataFrame([i.split() for i in fp.readlines()]).loc[1:, [0, 4, 5, 6]+row]
            temp[0] = 'CH0000' + temp[0]
            temp.dropna(inplace=True)
            data.append(temp.loc[~temp[0].isin(mask)])
        t_df = pd.concat(data)
        t_df.set_index([0, 4, 5, 6], inplace=True)
        t_df.replace('999999', np.nan, inplace=True)
        # t_df = t_df.astype(float) / 10
        t_df = t_df.astype(float)
        t_df[t_df > c] = np.nan
        t_df.columns = [f'{t}_{i}' for i in row]
        df.append(t_df)
    df1 = pd.concat(df, axis=1)
    # df1['WIN_9'] = df1['WIN_9']*10
    # df1['WIN_11'] = df1['WIN_11']*10
    df1 = df1.replace(np.nan, 32766)
    # df1['WIN_9'] = df1['WIN_9'].astype(int)
    # df1['WIN_11'] = df1['WIN_11'].astype(int)
    # df1.to_csv(f'CH_{year}.txt', header=False, index=True, float_format='%.2f')

