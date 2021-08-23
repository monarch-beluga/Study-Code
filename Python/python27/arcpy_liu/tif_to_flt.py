# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/26
@file: tif_to_flt.py
@function:
@modify:
"""

from glob import glob
import arcpy
import time

files = glob(r'F:/NDVI/*.tif')
arcpy.env.workspace = r'F:/NDVI_flt/'

s = len(files)
st = time.time()
for i, f in enumerate(files):
    arcpy.RasterToFloat_conversion(f, f.split('\\')[-1].replace('tif', 'flt'))
    p = time.time() - st
    t = p / (i+1) * s - p
    print '进度: {0}/{1}, 耗时:{2:.2f}s, 还需:{3:.2f}s'.format(i+1, s, p, t)

