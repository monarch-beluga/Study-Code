# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/08/05
@file: 格式化输出.py
@function:
@modify:
"""

import pandas as pd

df = pd.read_csv(r'E:\Data\sta.txt')


def df_format(fp, f_mat, data):
    for i in range(len(data)):
        print(f_mat.format(*data.loc[i].to_list()), file=fp)


with open(r'test.txt', 'w') as f:
    out_format = '{:10s}'+'{:12.2f}'*2
    df_format(f, out_format, df)

