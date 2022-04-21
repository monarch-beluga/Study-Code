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

df = pd.read_csv(r"E:\Data\3S\all_points.dat", encoding='gbk', header=None)
dzy_df = df.loc[df[0].str[:3] == '电子眼']
dzy_df[1] = '165960'
