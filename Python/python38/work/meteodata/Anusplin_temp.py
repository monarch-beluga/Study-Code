# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/12/27
@file: Anusplin_temp.py
@function:
@modify:
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# ============================================用户修改部分=====================================================
# -------------------本地数据目录配置------------------
# path = r'E:\public\sjy'                 # 数据所在目录
path = input('输入数据所在目录：')
dem = r'dem.txt'                        # 高程数据(ASCII码栅格)
# path = r'H:\Monarch\test'
shp_roi = r'roi.shp'                    # 选取的矢量站点的范围(其投影要与高程一致)

# ------------------数据库连接配置-------------------
host = "103.46.128.21"                  # ip地址
# host = "127.0.0.1"
port = 29611                            # 端口
# port = 3306
sql_name = "root"                       # 用户名称
pwd = "123456"                          # 用户密码
dbs = "meteodata"                       # 需要查询的数据库, 国内使用meteodata, 国外使用meteodata_extens

# -----------------插值配置------------------------
types = ['MTEM', 'PREP']                # 插值的要素
out_pre = ['TAVG', 'PRCP']
q = 0.8                                 # 数据完整性百分比
# types: list, 要获取的气象要素列表:
#     |APRE: 平均本站气压 | DMXP:日最高本站气压 | DMNP: 日最低本站气压 | MTEM: 平均气温 | DMXT: 日最高气温|
#     |DMNT: 日最低气温 | AVRH: 平均相对湿度 | MNRH: 最小相对湿度 | PREP: 降水量 | MEWS: 平均风速 |
#     |MXWS: 最大风速|DMWS: 最大风速的风向|EXWS: 极大风速|DEWS: 极大风速的风向|SOHR: 日照时数|
start_time = '2019-05-01'               # 插值起始时间
end_time = '2020-07-31'                 # 插值结束时间
sep_day = 4                             # 插值尺度(单位：日)

# =======================================================================================================

# =======================================程序内置部分(不要修改)===============================================
os.chdir(path)
df = pd.read_csv(r'station_data.txt', header=0)
df['date'] = df['Year'] * 10000 + df['Month'] * 100 + df['Day']
df['unique'] = df['date'].apply(lambda x:
                              (datetime.strptime(str(x), "%Y%m%d")-datetime.strptime(str(x//10000), "%Y")).days)
df['unique'] = df['unique'] - df.groupby('Year')['unique'].transform('min')
df['unique'] = df['Year'] * 1000 + df['unique']
for t in types:
    df.loc[(df[t] > 1000) | (df[t] < -100), t] = np.nan
# for t, out_t in zip(types, out_pre):
#     if not os.path.exists(out_t):
#         os.makedirs(out_t)
t = types[0]
pre = out_pre[0]
data = df[['Station', 'unique', t]]
data.set_index(['Station', 'unique'], inplace=True)
data1 = data.unstack()
data1.columns = data1.columns.levels[1]
count = data1.shape[1]
data1.drop(data1[data1.count(1) < count*q].index, inplace=True)
data1 = data1.interpolate(method='linear', limit_direction='both', axis=1).T
data1.index = (data1.index // 1000) * 1000 + (data1.index % 1000) // sep_day
if t == 'PREP':
    data1 = data1.groupby(data1.index).sum().T
else:
    data1 = data1.groupby(data1.index).mean().T
data1.to_csv(f'{pre}0000.txt')
