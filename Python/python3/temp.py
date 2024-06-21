# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import rasterio
import os
from glob import glob
import numpy as np

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)

with rasterio.open('gdp/gdp_1995.tif') as src:
    profile = src.profile
    data = src.read()
data[data != profile['nodata']] /= 10
with rasterio.open('gdp/gdp_1995.tif', 'w', **profile) as dst:
    dst.write(data)
