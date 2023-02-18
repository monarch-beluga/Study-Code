# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/09/15
@file: 采矿权.py
@function:
@modify:
"""

import pandas as pd
import pypyodbc as mdb
import shapefile

# 文件路径
a = r'E:\Data\temp\原始数据和处理数据匹配不上的.xlsx'
p_path = r'E:\Data\temp\20210907mdb\采矿权.mdb'
shp = r'E:\Data\temp\补充.shp'

# mdb数据库连接
connStr = r'Driver={Microsoft Access Driver (*.mdb)}; DBQ=%s; Database=bill;' % p_path
conn = mdb.win_connect_mdb(connStr)
# 创建shp文件
w = shapefile.Writer(shp, shapeType=5)
w.field('FIRST_ID')
w.field('name', 'C', '100')
# 读取excel中的矿山名称
df = pd.read_excel(a, sheet_name='我们数据缺失')
df = df['矿山名称']
l = df.tolist()
b = str(l)
# 查询数据
dfTable = pd.read_sql("SELECT `矿山名称`,`区域坐标2000` FROM `采矿申请登记` where `矿山名称` in ({})".format(b[1:-1]), conn)
# 循环写入shp矢量
for m in range(len(df)):
    c = dfTable.iloc[m]['区域坐标2000']
    name = dfTable.iloc[m]['矿山名称']
    d = c.split(',')
    i = 1
    s = []
    # 解析坐标
    for n in range(int(d[0])):
        a2 = []
        d1 = int(d[i])
        i += 1
        for j in range(d1):
            a1 = []
            i += 1
            a1.append(float(d[i+1]))
            a1.append(float(d[i]))
            i += 2
            a2.append(a1)
        s.append(a2)
        i += 4
    # 写入面要素
    w.poly(s)
    w.record(f'{m}', name)

# shp文件关闭
w.close()
