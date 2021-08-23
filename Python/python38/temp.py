# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/05
@file: temp.py
@function:
@modify:
"""

import pandas as pd
import numpy as np


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print(f_mat.format(*Data.loc[i].to_list()), file=fp)


file_name = r'E:\public\sjy\TAVG\TAVG00000.dat'
with open(file_name, 'r') as f:
    lines = f.readlines()
data = []
for line in lines:
    data.append(line.split())

df = pd.DataFrame(data)
df.set_index([0, 1, 2, 3], inplace=True)
df = df.astype('float')
df[df > 100] = np.nan
df1 = df.interpolate(method='linear', limit_direction='both', axis=1)
df1.reset_index(inplace=True)
df1.set_index(0, inplace=True)
df1 = df1.astype('float')
df1.reset_index(inplace=True)

with open(file_name, 'w') as f:
    out_format = '{:11s}'+'{:12.2f}'*2+'{:10.3f}'+'{:10.2f}'*19
    df_format(f, out_format, df1)

