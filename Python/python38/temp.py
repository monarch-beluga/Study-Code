# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

import pandas as pd

df = pd.read_csv(r'E:\Data\class\R语言区域分析\人口数据.csv', header=0, index_col=0)
df1 = df.T
df2 = df1.sort_index()
df2.insert(2, 'time', range(2000, 2021))
df2.to_csv(r'E:\Data\class\R语言区域分析\人口数据1.csv', header=True, index=True)
