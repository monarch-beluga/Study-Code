# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

from pyhdf.SD import SD
import numpy as np
from Monarch.tqdm_common import get_asyncio_bar
import rasterio
from glob import glob
import os

os.chdir(r'Z:\ECA\GLASS_temperature')

out_path = r'Z:\ECA\temperature(初始)'
prj_file = r'Y:\ECA\Temperature(初始)\2000_02_18.tif'
with rasterio.open(prj_file) as src:
    profile = src.profile


# for year in range(1982, 2000):
#     files = glob(f'{year}/*.hdf')
#     files_count = len(files)
#
#     bar = get_asyncio_bar(f'LST hdf to tif in {year}', files_count, unit='it')

# for i, file in enumerate(files):
file = r'1990\\GLASS08B22.V40.A1990333.2020106.hdf'
out_file = f'{out_path}/LST_{file.split(".")[-3][1:]}.tif'
# if os.path.exists(out_file):
#     bar.update(1)
#     continue
hdf_obj = SD(file)
# lst = hdf_obj.select('LST')[:, :].astype('float32')
# lon = hdf_obj.select('Longitude')[:]
# lat = hdf_obj.select('Latitude')[:]
#
# lon_min, lat_max, lon_max, lat_min = [lon.min(), lat.max(), lon.max(), lat.min()]
# l_lat = len(lat)
# l_lon = len(lon)
# lat_ce = (lat_max - lat_min)/(l_lat - 1)
# lon_ce = (lon_max - lon_min)/(l_lon - 1)
#
# lst[lst == 0] = np.nan
# lst = lst*0.02 - 273.15
#
# transform = [lon_ce, 0, lon_min, 0, -lat_ce, lat_max]
# profile.update({
#             'dtype': 'float32',
#             'nodata': -32768,
#             'transform': transform,
#             'width': l_lon,
#             'height': l_lat,
#             'compress': 'lzw'
#         })
#
# with rasterio.open(out_file, 'w', **profile) as dst:
#     dst.write(lst, 1)
# bar.update(1)

# bar.update(bar.total - bar.n)
# bar.close()


