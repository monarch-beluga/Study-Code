# -*- coding: utf-8 -*-
# @Time    : 2023/3/25 0:19
# @Author  : Monarch
# @File    : Tavg_select_Station.py
# @Software: PyCharm

import pandas as pd
from glob import glob
import geopandas as gpd
import os

os.chdir(r'D:\Work\ECA\站点TAVG数据')

shp = r'D:\Work\ECA\NDVI\roi.shp'
roi = gpd.read_file(shp).to_crs('epsg:4326')

point_shp = 'Station.shp'
points = gpd.read_file(point_shp).to_crs('epsg:4326')

select_ps = gpd.overlay(points, roi, 'intersection')
select_ps.to_file('select_Station.shp')

station = select_ps['Station'].to_list()

files = glob('*.txt')
df = pd.read_csv(files[0], index_col=0)
df_Station = df[df.index.isin(station)]
for file in files[1:]:
    df = pd.read_csv(file, index_col=0)
    df = df[df.index.isin(station)].iloc[:, 2:]
    df_Station = pd.concat([df_Station, df], axis=1)

df_Station.to_csv('tavg_station.txt', float_format='%.3f')

