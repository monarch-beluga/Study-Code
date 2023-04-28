# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/15
@file:  mask_file_process.py
"""


def mask_raster(path, out_path, mask_file, com):
    from glob import glob
    import os
    import numpy as np
    import rasterio
    from Monarch.tqdm_common import get_asyncio_bar

    # path = r'Y:\ECA\NDVI初始'
    os.chdir(path)

    # out_path = r'Y:\ECA\NDVI_mask'
    if not os.path.exists(out_path):
        os.mkdir(out_path)

    # mask_file = r'remove_mask_NDVI.tif'
    with rasterio.open(mask_file) as mask_src:
        mask_data = mask_src.read(1)

    files = glob(f'{com}*.tif')
    files_count = len(files)

    bar = get_asyncio_bar(f'{com} mask', files_count, unit='it')

    for file in files:
        out_file = f'{out_path}/{file}'
        if not os.path.exists(out_file):
            with rasterio.open(file) as src:
                data = src.read(1)
                data[np.isnan(mask_data)] = np.nan
                profile = src.profile
            with rasterio.open(out_file, 'w', **profile) as dst:
                dst.write(data, 1)
        bar.update(1)

    bar.update(bar.total - bar.n)
    bar.close()

