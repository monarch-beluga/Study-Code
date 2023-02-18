# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/01/04
@file: station_chuli.py
@function:
@modify:
"""

import pandas as pd
import os

os.chdir(r'E:\Work\气象数据20210518\说明文档')
# types = ['PRS', 'PRE', 'TEM', 'RHU', 'SSD', 'WIN']
df = pd.read_excel(r'附件2.国家级地面气象观测站站点基本信息全表（2016）.xls', header=2, index_col=0).iloc[:-1, :-1]
df.loc[df['纬度'].str[-1] == 'S', '纬度'] = '-' + df.loc[df['纬度'].str[-1] == 'S', '纬度'].str[:-1]
df.loc[df['经度'].str[-1] == 'W', '经度'] = '-' + df.loc[df['经度'].str[-1] == 'W', '经度'].str[:-1]
df.loc[df['经度'].str[-1] == 'E', '经度'] = df.loc[df['经度'].str[-1] == 'E', '经度'].str[:-1]
df['区站号'] = df['区站号'].apply(lambda x: f'CH0000{int(x)}')
df['经度'] = df['经度'].apply(lambda x: format(float(x)/100, '.2f'))
df['纬度'] = df['纬度'].apply(lambda x: format(float(x)/100, '.2f'))
df1 = df[['区站号', '经度', '纬度', '观测场拔海高度（米）', '站名', '省份']]

