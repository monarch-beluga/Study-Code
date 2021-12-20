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
import numpy as np
import pandas as pd

os.chdir(r'H:\Monarch\paper\Data\landuse\class\points')
files = glob('*.shp')
data = []
for i in files:
    df = gpd.read_file(i)
    df['CID'] = np.random.randint(1, 100, len(df))
    data.append(df)
crs = data[0].crs
data1 = gpd.GeoDataFrame(pd.concat(data))
data1 = data1.to_crs(crs)
data1.to_file('points.shp')
