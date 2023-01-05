# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

import rasterio
import os
import numpy as np

os.chdir(r'H:\Monarch\Work\土壤碳')

src = rasterio.open('SOC.tif')
profile = src.profile
windows = [window for ij, window in src.block_windows()]

polc0_src = rasterio.open('polc20191.tif', 'w', **profile)
polc2_src = rasterio.open('polc20193.tif', 'w', **profile)
polc6_src = rasterio.open('polc20197.tif', 'w', **profile)
polc7_src = rasterio.open('polc20198.tif', 'w', **profile)

for win in windows:
    insc = src.read(1, window=win)
    insc[insc == profile['nodata']] = np.nan

    polc0 = 0.05*0.2*insc
    polc2 = 0.2*insc
    polc6 = 0.4*insc
    polc7 = 0.4*insc

    polc0_src.write(polc0, 1, window=win)
    polc2_src.write(polc2, 1, window=win)
    polc6_src.write(polc6, 1, window=win)
    polc7_src.write(polc7, 1, window=win)

src.close()
polc0_src.close()
polc2_src.close()
polc6_src.close()
polc7_src.close()

