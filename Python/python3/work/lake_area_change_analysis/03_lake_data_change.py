# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 14:12
# @Author  : Monarch
# @File    : 03_lake_data_change.py
# @Software: PyCharm

import pandas as pd
import os

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
out_path = "csv_data"
if not os.path.exists(out_path):
    os.mkdir(out_path)

lakes = ['太湖', '梁子湖', '洞庭湖', '洪泽湖', '鄱阳湖', "巢湖"]
columns = ['area', "TAVG", "PRCP", 'pop', 'gdp']

for lake in lakes:
    lake_data = pd.read_csv(f'csv_data/{lake}_zonal_statistics.csv', encoding='gbk', index_col=0)
    df = pd.DataFrame(columns=columns)
    for key in columns:
        df[key] = lake_data.iloc[:, lake_data.columns.str.contains(key)].values[0]
    df.index = range(1990, 2021, 5)
    df.to_csv(f'{out_path}/{lake}_statistic.csv', encoding='gbk')
