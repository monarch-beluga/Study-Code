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
from glob import glob
import numpy as np


def f_write(f_name):
    with open(f_name, 'w') as fp:
        for x in df2.index:
            print('{0:11s}{1:12.2f}{2:12.2f}{3:10.3f}'
                  .format(df2.loc[x, 0], df2.loc[x, 1], df2.loc[x, 2], df2.loc[x, 3]), file=fp, sep='', end='')
            for y in df2.columns[4:]:
                print('%10.2f' % df2.loc[x, y], file=fp, sep='', end='')
            print('', file=fp)


var = ['PRCP', 'TMIN', 'SSD', 'WIN', 'RHU', 'TMAX']
path = r'E:/Data/re_data/'
for v in var[:1]:
    files = glob(path+v+'*.dat')
    for f in files:
        df = pd.read_csv(f, delim_whitespace=True, header=None, index_col=[0, 1, 2, 3])
        df[df > 10000] = np.nan
        df1 = df.interpolate(method='linear', limit_direction='both', axis=1).round(2)
        df2 = df1.reset_index()
        out_file = f.replace(v, 'reult/{0}'.format(v))
        f_write(out_file)
        print(f.split('\\')[-1], '处理完成！！')



