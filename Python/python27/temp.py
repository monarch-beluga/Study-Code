# -*- coding: utf-8 -*-

import pandas as pd


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print >> fp, f_mat.format(*Data.loc[i].tolist())


st_df = pd.read_csv(r'E:/Work/气温站点数据.csv'.decode('utf-8'), encoding='gbk', index_col=0)
st_df.index = st_df.index.astype(str)
t_df = pd.read_csv(r'E:/Work/temper.csv', index_col=0).T
df = pd.concat([st_df, t_df], axis=1)
df = df.reset_index()
df.rename(columns={'index': 'station'}, inplace=True)
count = df.shape[1]

with open(r'E:/Work/station_temper.dat', 'w') as f:
    print >> f, ('\t'.join(df.columns.tolist())).encode('utf-8')
    out_format = '{:6s}' + '{:14.6f}' * 2 + '{:6.1f}' + '{:6.2f}' * (count - 4)
    df_format(f, out_format, df)

