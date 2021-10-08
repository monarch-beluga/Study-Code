# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import pandas as pd
import numpy as np

with open(r'E:/public/Data/columns.txt', encoding='utf-8') as fp:
    a = fp.read()
columns = a.split()
types = ['PRCP', 'TAVG', 'TMAX', 'TMIN', 'AWND', 'TSUN']
path = r'E:/public/数据/数据库入库数据/'
for year in range(2019, 2021):
    # year = 2019
    file = path+'{0}.csv'.format(year)
    Pieces = pd.read_csv(file, usecols=[0, 1, 2, 3], header=None, chunksize=1000000)
    mask = pd.read_csv(r'E:\public\数据\数据库入库数据\all{0}.txt'.format(year), header=None, usecols=[0])
    for j, df in enumerate(Pieces):
        df.columns = ['台站', '日期', '类型', '值']
        df = df[df['类型'].isin(types)]
        df1 = df.set_index(['台站', '日期', '类型'])
        df1 = df1/10
        df2 = df1.unstack()
        df2.columns.names = ['value', 'type']
        df3 = df2.stack('value').reset_index()
        df3['年'] = df3['日期'] // 10000
        df3['月'] = df3['日期'] % 10000 // 100
        df3['日'] = df3['日期'] % 100
        df4 = df3.drop(['value', '日期'], axis=1)
        ret = list(set(columns) ^ set(df4.columns))
        for i in ret:
            df4[i] = 32766
        df5 = df4[columns]
        df6 = df5[~df5['台站'].isin(mask[0])]
        df6['TSUN'] = df6['TSUN']/6
        df6 = df6.replace(np.nan, 32766)
        df6.to_csv(path+'{0}/{0}_{1}.txt'.format(year, j), header=False, index=False, float_format='%.2f')
        print('{0}_{1}.txt导出成功'.format(year, j))


