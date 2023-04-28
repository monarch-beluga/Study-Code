# -*- coding: utf-8 -*-
# @Time    : 2023/4/22 22:28
# @Author  : Monarch
# @File    : get_point.py
# @Software: PyCharm

import os
from glob import glob
import geopandas as gpd
import pandas as pd

os.chdir(r'D:\Data\parper\data\datasets')
class_type = ['裸土地', '建设用地', '水田', '林地', '草地', '水体']

data = []
files = glob('point*.shp')
for i in range(len(files)):
    shp = files[i]
    gdf = gpd.read_file(shp)[:1000]
    gdf['CID'] = list(range(1000))
    gdf.insert(1, 'TDLYMC', class_type[i])
    gdf.insert(1, 'TDLYDM', i+1)
    data.append(gdf)
point = pd.concat(data).to_crs('epsg:4326')
point.to_file('landuse_point.shp', encoding='utf-8')

