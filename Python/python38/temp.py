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
ld_df = df.loc[df[0].str.extract(r'(路)', expand=False).notna()]
ld_df[1] = 'A70'
# ld_df.to_csv(r"E:\Data\3S\路灯.dat", encoding='gbk', index=False, header=False)
