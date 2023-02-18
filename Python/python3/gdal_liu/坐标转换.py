# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/11
@file: 坐标转换.py
@function:
@modify:
"""

import pandas as pd
from pyproj import CRS
import pyproj

f_st = r'E:\public\Data\ghcnd-stations.txt'
f_prj = r'E:\public\Data\WGS_1984_Albers.prj'
data = []
with open(f_st) as fp:
    for i in fp.readlines():
        data.append(i.split()[:4])
with open(f_prj) as fp:
    prj_str = fp.readline()
df = pd.DataFrame(data)
df.columns = ['station', 'lat', 'lon', 'elev']
df1 = df.set_index('station')
cs1 = CRS.from_string('epsg:4326')
cs2 = CRS.from_string(prj_str)
df1 = df1.reset_index()
transformer = pyproj.Transformer.from_crs(cs1, cs2)
df1.lat, df1.lon = transformer.transform(df1.lat.values, df1.lon.values)
df2 = pd.read_csv(r'E:\public\数据\数据库入库数据\station.txt', header=None)
df2.columns = ['station', 'lat', 'lon', 'elev', 'st_name', 'reg']
df1['st_name'] = 'null'
df1['reg'] = 'null'
df3 = pd.concat([df1, df2])

df3.drop_duplicates(subset=['station'], keep='first', inplace=True)

df3.to_csv(r'E:\public\Data\station.txt', header=False, index=False)

