# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : get_mask.py
# @Software: PyCharm

import numpy as np
import rasterio

LST_mask_file = r''
NDVI_mask_file = r''
out_mask_file = r''

with rasterio.open(LST_mask_file) as lst_src:
    profile = lst_src.profile
    lst_mask = lst_src.read(1)

with rasterio.open(NDVI_mask_file) as ndvi_src:
    ndvi_mask = ndvi_src.read(1)

mask = lst_mask + ndvi_mask
mask[np.isnan(mask)] = profile['nodata']

with rasterio.open(out_mask_file, 'w', **profile) as dst:
    dst.write(mask, 1)
