# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/15
@file:  NDVI_mean.py
"""

from glob import glob
import os
import numpy as np
import rasterio
from Monarch.tqdm_common import get_asyncio_bar

path = r'Y:\ECA\NDVI_mask'
os.chdir(path)

out_path = r'Y:\ECA\NDVI_mean'
if not os.path.exists(out_path):
    os.mkdir(out_path)

files_t = [glob(f'NDVI{i}*.tif') for i in range(1982, 2022)]
n_files = [[j[i] for j in files_t] for i in range(23)]

for i, files in enumerate(n_files):
    outfile = f'{out_path}/NDVI{i * 16 + 1:03d}.tif'
    if os.path.exists(outfile):
        continue
    files_count = len(files)

    with rasterio.open(files[0]) as src:
        profile = src.profile
        data_sum = src.read(1)
        data_com = (data_sum != src.nodata) & (~np.isnan(data_sum))
        data_count = np.zeros(data_sum.shape, dtype='float32')
        data_count[data_com] += 1
        data_sum[~data_com] = 0

    bar = get_asyncio_bar(f'NDVI{i * 16 + 1:03d}.tif', files_count - 1, unit='it')

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

    data_count[data_count == 0] = np.nan
    data_mean = data_sum / data_count

    with rasterio.open(outfile, 'w', **profile) as dst:
        dst.write(data_mean, 1)


