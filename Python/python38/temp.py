# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

from glob import glob
import rasterio
from rasterio_liu import prj_transform
import os

os.chdir(r'Y:\ECA\NDVI初始')

prj_file = r'Y:\ECA\project\PRCP_2018001.flt'
with rasterio.open(prj_file) as src:
    crs = src.crs

if not os.path.exists(r'result'):
    os.mkdir('result')

i = 0
files = glob(r'*.tif')
for file in files:
    if os.path.exists(f'result/{file}'):
        i += 1
        continue
    dst_data, profile = prj_transform.project_transform(file, crs, 1000)
    if file[:4] == 'temp':
        profile['dtype'] = 'float32'
        dst_data = dst_data.astype(profile['dtype'])
        dst_data[dst_data != profile['nodata']] /= 10000
    with rasterio.open(f'result/{file}', 'w', **profile) as dst_src:
        dst_src.write(dst_data)
    i += 1
    print(f'{i} {file} 投影转换成功！！！')

