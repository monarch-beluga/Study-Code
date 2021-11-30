# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import geopandas as gpd
import os
from glob import glob
import pandas as pd

os.chdir(r'G:\arcgis1\package\jx_landuse\commondata\datasets')
shp_files = glob('*.shp')

data = []
for shp in shp_files:
    if shp == 'jx_landuse_2017_13.shp':
        continue
    gdf = gpd.read_file(shp)
    data.append(gdf)
data1 = gpd.GeoDataFrame(pd.concat(data))


