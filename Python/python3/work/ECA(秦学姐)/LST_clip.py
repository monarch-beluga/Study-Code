# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 19:49
# @Author  : Monarch
# @File    : LST_clip.py
# @Software: PyCharm

import geopandas as gpd
from Monarch.raster_common import *
from Monarch.tqdm_common import get_asyncio_bar
from rasterio.mask import mask
import rasterio
from glob import glob
import os

os.chdir(r'Z:\ECA\temperature(合并)')

out_path = r'Z:\ECA\temperature(裁剪)'
if not os.path.exists(out_path):
    os.mkdir(out_path)

shp_file = r'H:\Monarch\Work\NDVI\roi.shp'
shp = gpd.read_file(shp_file)
geo = shp.geometry[0]
roi = [geo.__geo_interface__]

clip_file = r'H:\Monarch\Work\NDVI\clip.tif'
with rasterio.open(clip_file) as mask_src:
    clip_profile = mask_src.profile

files = glob('*.tif')

bar = get_asyncio_bar('LST clip', len(files), 'it')

for file in files:
    out_file = f'{out_path}/{file}'
    if os.path.exists(out_file):
        bar.update(1)
        continue
    with rasterio.open(file) as src:
        profile = src.profile
        bounds = src.bounds
        clip_data, clip_transform = mask(src, roi, all_touched=True, crop=True, nodata=-32768)

    profile.update({
        'nodata': -32768,
        'width': clip_data.shape[2],
        'height': clip_data.shape[1],
        'transform': clip_transform
    })

    prj_data, prj_profile = project_profile(profile, clip_profile['crs'], clip_data, 1000)

    with rasterio.open(out_file, 'w', **clip_profile) as dst:

        row_start, row_end, col_start, col_end = clip_to_raster(prj_profile, clip_profile, 1000)

        dst.write(prj_data[:, row_start:row_end, col_start:col_end])

    bar.update(1)

bar.update(bar.total - bar.n)
bar.close()



