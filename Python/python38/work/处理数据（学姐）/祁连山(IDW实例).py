# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/05/11
@file: 祁连山(IDW实例).py
@function:
@modify:
"""
from scipy_liu.IDW import Invdisttree
import os
import pandas as pd
import numpy as np
from datetime import datetime

month = [3, 6, 9, 12]
os.chdir(r'E:\Data')
tdf = pd.read_csv('test.txt', index_col=0)
for year in range(1951, 1952):  # 将1990到2018这几个年份赋予a
    df = pd.read_csv(f'TAVG_{year}_Filled.csv')
    df = df.replace(-9999, np.nan)
    add_st = list(set(tdf.index).difference(set(df.station.to_list())))
    add_df = tdf.loc[add_st, :].reset_index()
    add_df.insert(add_df.shape[1], 'Year', year)
    df1 = df.append(add_df)
    for i in df.columns[5:]:
        data2 = df1[df1[i].isna()]
        q = data2[['LATI', 'LONG']].values.tolist()
        if q:
            data1 = df1[~df1[i].isna()]
            X = data1[['LATI', 'LONG']].values.tolist()
            z = data1[i].values
            in_dist_tree = Invdisttree(X, z)
            y = in_dist_tree(q, nnear=5)
            y = np.around(y, 2)
            df1.loc[df1[i].isna(), i] = y
    df2 = df1.loc[df1['station'].isin(tdf.index), :]
    df_h = df2.iloc[:, :5]
    y_time = datetime.strptime(f'{year}', "%Y")
    s_time = y_time
    s_day = 5
    for i in month:
        e_time = datetime.strptime(f'{year}-{i}', "%Y-%m")
        e_day = (e_time - y_time).days
        df3 = pd.concat([df_h, df2.iloc[:, s_day+5:e_day+5]], axis=1)
        df3.to_csv(f'TAVG_{year}_{s_time.month:02d}_{i-1:02d}_Filled.csv', index=False)
        s_day = e_day
        s_time = e_time
    df3 = pd.concat([df_h, df2.iloc[:, s_day+5:]], axis=1)
    df3.to_csv(f'TAVG_{year}_12_Filled.csv', index=False)


