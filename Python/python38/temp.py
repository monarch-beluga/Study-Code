# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import os
import geopandas as gpd
import pandas as pd

os.chdir(r'E:\public\Data')

Ch_sta = gpd.read_file(r'ChinaStations.shp')
Fort_sta = gpd.read_file(r'ForeignStations.shp')
total_sta = gpd.GeoDataFrame(pd.concat([Ch_sta, Fort_sta]))


