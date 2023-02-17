# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/14
@file:  clip_NDVI.py
"""


from Monarch.raster_common import clip_to_raster
import os
from glob import glob
import rasterio

path = r'H:\Monarch\Work\NDVI'
os.chdir(path)

clip_file = r'clip.tif'
with rasterio.open(clip_file) as mask_src:
    clip_profile = mask_src.profile

files = glob(f'NDVI*.tif')
for file in files:
    outfile = file.replace('_t.tif', '.tif')
    with rasterio.open(outfile, 'w', **clip_profile) as dst:

        with rasterio.open(file) as src:
            src_profile = src.profile
            data = src.read()

        row_start, row_end, col_start, col_end = clip_to_raster(src_profile, clip_profile)

        dst.write(data[:, row_start:row_end, col_start:col_end])

