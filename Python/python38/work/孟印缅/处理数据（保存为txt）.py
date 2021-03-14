
import pandas as pd
import rasterio
import os
import numpy as np


def fun(q, path, outpath, file_write):
    # q = 0.1
    # path = r'E:/temp/MOD11-merge/'
    # outpath = r'E:/temp/LST_Day_1km-NDVI/'
    # file_write = 'LST_Day_1km-%10.tif'
    File = os.listdir(path)
    with rasterio.open(path + File[0]) as src:
        profile = src.profile
        if profile.data['nodata'] != 0:
            profile.data['nodata'] = -3000
    data = []
    for j, i in enumerate(File):
        with rasterio.open(path + i) as src_read:
            temp = src_read.read()[0]
            temp = pd.DataFrame(temp)
            temp[temp == profile.data['nodata']] = np.nan
            temp = temp.values
        data.append(temp)
    data = np.array(data)
    data_write = np.quantile(data, q, axis=0).reshape(profile.data["height"], profile.data["width"])
    if profile.data['nodata'] != 0:
        data_write[np.isnan(data_write)] = -3000
    else:
        data_write[np.isnan(data_write)] = 0
    np.savetxt(outpath + file_write, data_write)


outpath1 = r'E:/temp/LST-NDVI/LST_Day_1km-NDVI/LST_Day_1km-NDVI-'
path1 = r'E:/temp/LST-NDVI/MOD13-select/'
Path = r'E:/temp/LST-NDVI/MOD11-merge/'
moth = ['03_04/', '05_06/', '07_08_09/']
for i in moth:
    fun(0.1, Path + i, outpath1 + 'txt/' + i, 'LST_Day_1km-%10.txt')
    fun(0.9, Path + i, outpath1 + 'txt/' + i, 'LST_Day_1km-%90.txt')
    fun(0.9, path1 + i, outpath1 + 'txt/' + i, 'NDVI-%90.txt')
    fun(0.1, path1 + i, outpath1 + 'txt/' + i, 'NDVI-%10.txt')
