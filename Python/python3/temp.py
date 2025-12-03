# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
from rasterio.transform import from_origin
import numpy as np
import netCDF4
from glob import glob


input_path = r'D:\Work\GOCI\nc'
output_path = r'D:\Work\GOCI\tif'

files = glob(os.path.join(input_path, '*.nc'))

nc_file = files[0]
src = netCDF4.Dataset(nc_file, 'r')
lat = src.groups['navigation_data'].variables['latitude'][:]


