# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 22:51
# @Author  : Monarch
# @File    : 国内站点合并.py
# @Software: PyCharm

import pandas as pd
import os

os.chdir(r'D:\Work\ECA\MeteoFilled_2019_2020\TAVG')

out_path = r'D:\Work\ECA\国内站点(合并)'
if not os.path.exists(out_path):
    os.mkdir(out_path)

sep = 16
for year in range(1980, 1990):
    columns = ['Station', 'Year', 'Y', 'X', 'Elva']
    df = pd.read_csv(f'TAVG_{year}_Filled.csv')
    df.columns = columns + [str(year * 1000 + (i // sep) * sep + 1) for i in range(len(df.columns) - 5)]
    df.set_index(columns, inplace=True)
    data_mean = df.groupby(df.columns, axis=1).mean() / 10
    data_columns = data_mean.columns.to_list()
    data_mean.reset_index(inplace=True)
    data = data_mean[['Station', 'X', 'Y'] + data_columns]

    data.to_csv(f'{out_path}/{year}.txt', float_format='%.3f', index=False)


