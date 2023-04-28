# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 10:16
# @Author  : Monarch
# @File    : 国内外数据合并.py
# @Software: PyCharm

import pandas as pd
import geopandas as gpd
import os

os.chdir(r'D:\Work\ECA')

out_path = r'站点数据'
if not os.path.exists(out_path):
    os.mkdir(out_path)

station = []
for year in range(1980, 2022):
    df1 = pd.read_csv(f'国内站点(合并)/{year}.txt')
    df2 = pd.read_csv(f'国外站点(合并)/{year}.txt')
    df = pd.concat([df1, df2])
    df.drop_duplicates(subset='Station', keep='first', inplace=True)
    df.to_csv(f'{out_path}/{year}.txt', float_format='%.3f', index=False)
    station.append(df[['Station', 'X', 'Y']])

ss = pd.concat(station).drop_duplicates(subset='Station', keep='first')
geo = gpd.points_from_xy(ss['X'], ss['Y'], crs='epsg:4326')
ps = gpd.GeoDataFrame(ss, crs='epsg:4326', geometry=geo)
ps.to_file(f'{out_path}/Station.shp')
