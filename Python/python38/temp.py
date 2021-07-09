# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/05
@file: drive.py
@function:
@modify:
"""

import numpy as np
import rasterio
from glob import glob
import os
from scipy.optimize import leastsq
from concurrent.futures.thread import ThreadPoolExecutor

regularization = 0.0001
M = 9
path = r'E:\Data\shuju_clip'
files = glob(path+os.sep+'*.tif')
with rasterio.open(files[0]) as src:
    windows = [window for i, window in src.block_windows()]
    profile = src.profile
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)


def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    ret = np.append(ret, np.sqrt(0.5*regularization*np.square(p)))  # L2范数作为正则化项
    return ret


def fitting(x, y, x1):
    p_init = np.random.rand(M+1)
    p_lsq_regularization = leastsq(residuals_func_regularization, p_init, args=(x, y))

    y1 = fit_func(p_lsq_regularization[0], x1)
    return y1


def read(f):
    with rasterio.open(f) as src1:
        da = src1.read()[0].astype("float32")
        da = da.flatten()
    return da


window = windows[50]
data = []
for file in files:
    temp = read(file)
    data.append(temp)
data = np.array(data)
data = data.T











