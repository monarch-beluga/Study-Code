# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

from datetime import datetime
from Monarch.raster_common import *
from Monarch.tqdm_common import get_asyncio_bar
import rasterio
from glob import glob
import os

os.chdir(r'Y:\ECA\Temperature(初始)')

out_path = r'Z:\ECA\temperature(裁剪)'

prj_file = r'H:\Monarch\Work\NDVI\clip.tif'
with rasterio.open(prj_file) as prj_src:
    prj_profile = prj_src.profile


for year in range(2000, 2022):
    start = datetime.strptime(f'{year}', '%Y')
    files = glob(f'{year}*.tif')
    bar = get_asyncio_bar(f'LST to prj {year}', len(files), unit='it')
    for file in files:
        date = datetime.strptime(f'{file.split(".")[0]}', '%Y_%m_%d')
        out_file = f'{out_path}/LST_{year}{(date - start).days+1:03d}.tif'

        if os.path.exists(out_file):
            bar.update(1)
            continue

        dst_data, dst_profile = project_transform(file, prj_profile['crs'], 1000, 'float32')

        dst_data[dst_data == dst_profile['nodata']] = np.nan
        dst_data = dst_data * 0.02 - 273.15
        dst_data[np.isnan(dst_data)] = dst_profile['nodata']
        with rasterio.open(out_file, 'w', **dst_profile) as dst:
            dst.write(dst_data)
        bar.update(1)

    bar.update(bar.total - bar.n)
    bar.close()



