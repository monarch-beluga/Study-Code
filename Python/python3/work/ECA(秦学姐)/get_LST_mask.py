# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:17
# @Author  : Monarch
# @File    : get_LST_mask.py.py
# @Software: PyCharm

import os
from glob import glob
import numpy as np
import rasterio
from Monarch.tqdm_common import get_asyncio_bar

os.chdir(r'D:\Work\ECA\temperature(合并)')

files = glob('*.tif')

files_count = len(files)
t_min = 7500 * 0.02 - 273.15
t_max = 65535 * 0.02 - 273.15

file = files[0]
with rasterio.open(files[0]) as src:
    profile = src.profile
    data_sum = src.read(1)
    data_com = (data_sum != src.nodata) & (~np.isnan(data_sum)) & (data_sum > t_min) & (data_sum < t_max)
    data_count = np.zeros(data_sum.shape, dtype='float32')
    data_count[data_com] += 1
    data_sum[~data_com] = 0


bar = get_asyncio_bar('LST mean', files_count-1, unit='it')

for file in files[1:]:
    with rasterio.open(file) as src:
        data = src.read(1)
        data_com = (data != src.nodata) & (~np.isnan(data)) & (data > t_min) & (data < t_max)
        data_count[data_com] += 1
        data[~data_com] = 0
        data_sum += data
        bar.update(1)

bar.update(bar.total - bar.n)
bar.close()

data_count[data_count < files_count*0.8] = np.nan
data_mean = data_sum / data_count
data_mean[np.isnan(data_mean)] = profile['nodata']
with rasterio.open('remove_mask_LST.tif', 'w', **profile) as dst:
    dst.write(data_mean, 1)


