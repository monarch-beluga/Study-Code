# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/6
@file:  clip_taster.py
"""

import os
from glob import glob
import time
from Monarch.raster_common import *
from Monarch.tqdm_common import get_asyncio_bar

start = time.time()
os.chdir(r'D:\MCD_dow')

clip_file = 'TAVG_2018001.flt'
with rasterio.open(clip_file) as mask_src:
    clip_profile = mask_src.profile

Vars = ['SNR', 'SSRD']

for var in Vars:

    if not os.path.exists(f'{var}_out'):
        os.mkdir(f'{var}_out')
    files = glob(f'{var}/*.tif')

    bar = get_asyncio_bar(f'clip {var} raster', len(files))

    for file in files:

        outfile = f'{var}_out/{os.path.basename(file).replace(".tif", ".flt")}'

        if os.path.exists(outfile):
            bar.update(1)
            continue

        with rasterio.open(outfile, 'w', **clip_profile) as dst:

            if var == 'Fpar':
                with rasterio.open(file) as src:
                    src_profile = src.profile
                    data = src.read()
            else:
                data, src_profile = re_raster_to_file(file, 1000)

            row_start, row_end, col_start, col_end = clip_to_raster(src_profile, clip_profile)

            dst.write(data[:, row_start:row_end, col_start:col_end])
        bar.update(1)

    bar.update(bar.total - bar.n)
    bar.close()

t_con = time.time() - start
print(f'总耗时:{int(t_con / 3600):02d}h{int(t_con % 3600 / 60):02d}m{t_con % 3600 % 60:.2f}s')

