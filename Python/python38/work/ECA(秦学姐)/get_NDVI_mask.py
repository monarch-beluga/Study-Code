# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/14
@file:  get_NDVI_mask.py
"""

from glob import glob
import os
import numpy as np
import rasterio
from Monarch.tqdm_common import get_asyncio_bar

path = r'Y:\ECA\NDVI初始\result'
os.chdir(path)

files = glob(r'NDVI*.tif')
files_count = len(files)

with rasterio.open(files[0]) as src:
    profile = src.profile
    data_sum = src.read(1)
    data_com = (data_sum != src.nodata) & (~np.isnan(data_sum))
    data_count = np.zeros(data_sum.shape, dtype='float32')
    data_count[data_com] += 1
    data_sum[~data_com] = 0

bar = get_asyncio_bar('NDVI mean', files_count-1, unit='it')

for file in files[1:]:
    with rasterio.open(file) as src:
        data = src.read(1)
        data_com = (data != src.nodata) & (~np.isnan(data))
        data_count[data_com] += 1
        data[~data_com] = 0
        data_sum += data
        bar.update(1)

bar.update(bar.total - bar.n)
bar.close()

data_count[data_count < files_count*0.8] = np.nan
data_mean = data_sum / data_count
data_mean[data_mean < 0.1] = np.nan
with rasterio.open('remove_mask_NDVI.tif', 'w', **profile) as dst:
    dst.write(data_mean, 1)



