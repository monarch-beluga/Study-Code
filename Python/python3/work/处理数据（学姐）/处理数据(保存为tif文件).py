
import pandas as pd
import rasterio
import os
import numpy as np


def fun(q, path, outpath, file_write, btype=None):
    # q = 0.1
    # path = r'E:/temp/MOD11-merge/'
    # outpath = r'E:/temp/LST_Day_1km-NDVI/'
    # file_write = 'LST_Day_1km-%10.tif'
    File = os.listdir(path)
    with rasterio.open(path + File[0]) as src:
        windows = [window for i, window in src.block_windows()]
        profile = src.profile
        if btype is not None:
            profile.data['dtype'] = btype
        if profile.data['nodata'] != 0:
            profile.data['nodata'] = -3000
    src_write = rasterio.open(outpath + file_write, "w", **profile)
    for window in windows:
        data = []
        for j, i in enumerate(File):
            with rasterio.open(path + i) as src_read:
                temp = src_read.read(window=window)[0].astype(profile.data['dtype'])
                temp = pd.DataFrame(temp)
                temp[temp == profile.data['nodata']] = np.nan
                temp = temp.values
            data.append(temp)
        data = np.array(data)
        data_write = np.quantile(data, q, axis=0).reshape(window.height, window.width)
        if profile.data['nodata'] != 0:
            data_write[np.isnan(data_write)] = -3000
        else:
            data_write[np.isnan(data_write)] = 0
    # return data_write, profile
        src_write.write(data_write.astype(profile.data['dtype']), 1, window=window)
    src_write.close()


outpath1 = r'E:/temp/LST-NDVI/LST_Day_1km-NDVI/LST_Day_1km-NDVI-'
path1 = r'E:/temp/LST-NDVI/MOD13-select/'
Path = r'E:/temp/LST-NDVI/MOD11-merge/'
moth = ['03_04/', '05_06/', '07_08_09/']
for i in moth:
    fun(0.1, Path + i, outpath1 + '原格式/' + i, 'LST_Day_1km-%10.tif')
    fun(0.9, Path + i, outpath1 + '原格式/' + i, 'LST_Day_1km-%90.tif')
    fun(0.9, path1 + i, outpath1 + '原格式/' + i, 'NDVI-%90.tif')
    fun(0.1, path1 + i, outpath1 + '原格式/' + i, 'NDVI-%10.tif')
    # fun(0.1, Path + i, outpath1 + 'float/' + i, 'LST_Day_1km-%10.tif', 'float32')
    # fun(0.9, Path + i, outpath1 + 'float/' + i, 'LST_Day_1km-%90.tif', 'float32')
    # fun(0.9, path1 + i, outpath1 + 'float/' + i, 'NDVI-%90.tif', 'float32')
    # fun(0.1, path1 + i, outpath1 + 'float/' + i, 'NDVI-%10.tif', 'float32')
# data1 = fun(0.9, path1 + moth[0], outpath1 + '原格式/' + moth[0], 'NDVI-%90.tif')
