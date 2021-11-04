# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: temp.py
@function:
@modify:
"""

import numpy as np
from PyEMD import EEMD
import time
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.pool import Pool
from scipy.stats import norm
from glob import glob
import os
import rasterio
from rasterio.windows import Window


# def read_data(f, win):
#     with rasterio.open(f) as f_re:
#         f_data = f_re.read(1, window=win).reshape(-1, 1)
#     return f_data

s_year = 1980
e_year = 2018
T = np.array([i for i in range(s_year, e_year + 1)])
eemd = EEMD(100, 0.01)


def eemd_data(y):
    y4 = eemd.eemd(y, T, -1)
    y5 = y4[-1, :]
    y6 = y5 - y5[0]
    y7 = np.diff(y6)
    ye = y7.mean()
    return ye


# def emd_sig_test(n, y8s):
#     m = 1000
#     x0 = np.random.rand(m, n)
#     if __name__ == '__emd_sig_test__':
#         with Pool(4) as pool:
#             ts = np.array(pool.starmap(eemd_data, x0))
#     mn = ts.mean()
#     sd = ts.std()
#     p1 = norm.cdf(y8s, mn, sd)
#     return mn, sd, p1

# def eemd_data()


# path = r'H:\Monarch\Data\Annual\Annual_RESdyn'
# os.chdir(path)
#
# gpp_files = glob('GPP*.flt')
# x_max = 9000
# x_min = 0

# with rasterio.open(gpp_files[0], 'r') as src:
#     windows = [window for ij, window in src.block_windows()]
#     profile = src.profile
#     nodata = src.nodata

# window = Window(0, 0, 4998, 204)
# with ThreadPoolExecutor(max_workers=20) as worker:
#     gpp_re = worker.map(read_data, gpp_files, [window]*len(gpp_files))
# gpp_data = np.concatenate(list(gpp_re), axis=1)

# y1 = gpp_data[654]
# y2 = y1[(y1 >= x_min) & (y1 <= x_max)]
# nd = y1.size
# ns = y2.size
# y_max = y2.max()
# y_min = y2.min()

if __name__ == '__main__':
    st = time.time()
    m = 1000
    x0 = np.random.rand(m, 39)
    with Pool(6) as pool:
        ts = np.array(pool.map(eemd_data, x0))
    rand_mn = ts.mean()
    rand_sd = ts.std()
    rand_p = norm.cdf(0.05, rand_mn, rand_sd)
    print(time.time() - st)
    # print(ts)
# if (ns == nd) and y_max > y_min:
#     y8 = eemd_data(y2)
#     yn = (y2 - y_min) / (y_max - y_min)
#     yn8 = eemd_data(yn)
# else:
#     y8 = -9999
#     yn8 = -9999
#     p = -9999


