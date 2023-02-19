# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/18
@file:  LST_merge.py
"""

import numpy as np
from Monarch.tqdm_common import get_asyncio_bar
import rasterio
import os

os.chdir(r'Z:\ECA\temperature(初始)')
out_path = r'Z:\ECA\temperature(合并)'

sep = 16
files_dict = {}
for year in range(1982, 2000):
    if (year % 4 == 0 and year % 400 != 0) or (year % 400 == 0):
        days = 366
    else:
        days = 365
    file_name = ''
    for day in range(1, days+1):
        file = f'LST_{year}{day:03d}.tif'
        if day % sep == 1:
            file_name = file
            files_dict[file_name] = []
        if os.path.exists(file):
            files_dict[file_name].append(file)

bar_main = get_asyncio_bar('LST merge', len(files_dict), 'it')
bar = get_asyncio_bar(f'merge', 10, unit='it')
for out_file in files_dict:
    files = files_dict[out_file]
    if len(files) == 0 or os.path.exists(f'{out_path}/{out_file}'):
        bar_main.update(1)
        continue
    files_count = len(files)
    bar.set_description_str(f'{out_file} merge')
    bar.reset(files_count)
    with rasterio.open(files[0]) as src:
        profile = src.profile
        data_sum = src.read(1)
        data_com = (data_sum != src.nodata) & (~np.isnan(data_sum))
        data_count = np.zeros(data_sum.shape, dtype='float32')
        data_count[data_com] += 1
        data_sum[~data_com] = 0
        bar.update(1)

    for file in files[1:]:
        with rasterio.open(file) as src:
            data = src.read(1)
            data_com = (data != src.nodata) & (~np.isnan(data))
            data_count[data_com] += 1
            data[~data_com] = 0
            data_sum += data
            bar.update(1)

    bar.update(bar.total - bar.n)

    data_count[data_count == 0] = np.nan
    data_mean = data_sum / data_count

    with rasterio.open(f'{out_path}/{out_file}', 'w', **profile) as dst:
        dst.write(data_mean, 1)
    bar_main.update(1)

bar_main.update(bar_main.total - bar_main.n)
bar_main.close()
bar.close()


