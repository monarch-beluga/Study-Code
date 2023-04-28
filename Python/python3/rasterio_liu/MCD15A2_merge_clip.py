# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 16:27
# @Author  : Monarch
# @File    : MCD15A2_merge_clip.py
# @Software: PyCharm

from glob import glob
import os
from rasterio.merge import merge
import rasterio
import numpy as np
from Monarch.raster_common import project_profile, clip_to_raster

os.chdir(r'D:\Work\mcd15a2')

out_path = 'MCD15A2_flt'
if not os.path.exists(out_path):
    os.mkdir(out_path)

proj = r'FPAR_2018001.flt'
with rasterio.open(proj) as src:
    clip_profile = src.profile
    dst_crs = src.crs

year = 2018
for i in range(1, 366, 8):
    files = glob(f'MCD15A2_tif/*{year}{i:03d}*.tif')

    src_files_to_mosaic = []
    for tif_f in files:
        src = rasterio.open(tif_f)
        src_files_to_mosaic.append(src)

    mosaic, out_trans = merge(src_files_to_mosaic)

    profile = src_files_to_mosaic[0].meta.copy()
    profile.update({
        "driver": "GTiff",
        'transform': out_trans,
        'width': mosaic.shape[2],
        'height': mosaic.shape[1],
        'compress': 'lzw'
    })

    dst_data, dst_profile = project_profile(profile, dst_crs, mosaic, 1000)
    dst_data = dst_data.astype('float32')
    dst_data[dst_data > 100] = np.nan
    dst_data /= 100
    dst_data[np.isnan(dst_data)] = clip_profile['nodata']
    row_start, row_end, col_start, col_end = clip_to_raster(dst_profile, clip_profile, 1000)

    with rasterio.open(f'{out_path}/Fpar_{year}{i:03d}.flt', 'w', **clip_profile) as dst:
        dst.write(dst_data[:, row_start:row_end, col_start:col_end])
    print(f'{out_path}/Fpar_{year}{i:03d}.flt export success !!!')
    break



