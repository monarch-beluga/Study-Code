# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/01/29
@file: 栅格合并.py
@function:
@modify:
"""

import rasterio
import os
from glob import glob
import pandas as pd
import numpy as np

os.chdir(r'E:\Work\result_npp')
lp = pd.read_csv('line_pixel.txt')
lp['line'] = lp['line_end'] - lp['line_start'] + 1
with rasterio.open('NPP2018001.flt', 'r') as src:
    profile = src.profile
if not os.path.exists('Result'):
    os.mkdir('Result')
flt_files = [glob(f'result{i}/*.flt') for i in range(1, 31)]
for j in range(len(flt_files[0])):
    data = []
    for i in range(30):
        with rasterio.open(flt_files[i][j], 'r') as src:
            temp = src.read(1).reshape(lp['line'][i], lp['pixels'][i])
        data.append(temp)
    data_flt = np.concatenate(data, axis=0)
    out_name = flt_files[0][j].split("\\")[-1]
    with rasterio.open(f'Result/{out_name}', 'w', **profile) as w_src:
        w_src.write(data_flt, 1)

