# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/11/25
@file: HDF5_read.py
@function:
@modify:
"""

import h5py
from osgeo import gdal
import numpy as np
from glob import glob
import os


def Write(file, data, prj, tr):
    driver = gdal.GetDriverByName('GTiff')
    Size = data.shape
    out_ds = driver.Create(
        file,
        Size[1],
        Size[0],
        1,
        gdal.GDT_Float32)

    out_ds.SetProjection(prj)
    out_ds.SetGeoTransform(tr)
    for i in range(1, 2):
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(data)
    out_ds.FlushCache()
    del out_ds


os.chdir(r'E:\Work\HDF5\GF_LAIDATA')
files = glob('*.h5')
for f_name in files:
    with h5py.File(f_name, 'r') as f:
        prj = f.attrs['ProjectionStr'].decode('utf-8')
        tsf = [float(i) for i in f.attrs['ProjectionPara'].decode('utf-8').split(',')]
        for i in f.keys():
            for j in f[i].keys():
                if not os.path.exists(f'result_{j}'):
                    os.mkdir(f'result_{j}')
                data = np.array(f[i][j])
                out_name = f"result_{j}/{'_'.join(f_name.split('.')[:-1])}.tif"
                Write(out_name, data, prj, tsf)
                print(out_name, "export success ！！！")



