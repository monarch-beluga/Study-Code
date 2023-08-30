# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 17:23
# @Author  : Monarch
# @File    : slope_calc.py
# @Software: PyCharm

import os
import numpy as np
from glob import glob
from scipy import stats
import rasterio


os.chdir(r'D:\Work\htt_test')
files = glob('*.tif')
out_file = 'slope.tif'
x = np.arange(len(files))


# slope计算函数
def get_slope(y):
    # 如果一个像元多年数据中有缺失值就直接返回nan
    if len(y[np.isnan(y)]) > 0:
        return np.nan
    slope = stats.linregress(x, y)[0]
    return slope


# 读取一个文件获取窗口信息和文件信息
with rasterio.open(files[0]) as src:
    windows = [window for ij, window in src.block_windows()]
    profile = src.profile

# slope文件创建
dst = rasterio.open(out_file, 'w', **profile)
# win = windows[100]
for win in windows:
    data = []
    # 数据读取
    for file in files:
        with rasterio.open(file) as src:
            f_data = src.read(1, window=win)
            # nan替换
            f_data[f_data == profile['nodata']] = np.nan
            data.append(f_data)
    # 多年数据合并
    data = np.array(data)
    # 计算slope
    slope_data = np.apply_along_axis(get_slope, axis=0, arr=data)
    # slope写入
    dst.write(slope_data, 1, window=win)

# 关闭slope文件
dst.close()

