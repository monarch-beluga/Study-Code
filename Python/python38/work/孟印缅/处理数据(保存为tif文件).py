
import pandas as pd
import rasterio
import os
import numpy as np
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

outpath1 = r'E:/work/孟印缅/LST_Day_1km-NDVI-'
path1 = r'E:/work/孟印缅/MOD13-select/'
Path = r'E:/work/孟印缅/MOD11-Interpolation/'
moth = ['03_04/', '05_06/', '07_08_09/']


def linear(x):
    for y1, y in enumerate(x):
        if np.isnan(y).sum() > len(y) / 3.0:
            da = y
        else:
            y = pd.DataFrame(y)
            da = y.interpolate(method='linear', limit_direction='both')
        x[y1] = np.array(da).flatten()
    return x


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
        for i in File:
            with rasterio.open(path + i) as src_read:
                temp = src_read.read(window=window)[0].astype(profile.data['dtype'])
                # temp = pd.DataFrame(temp)
                temp[temp == profile.data['nodata']] = np.nan
                # temp = temp.values
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
    # return data


def Mon(i):
    out = outpath1 + '原格式/' + i
    if not os.path.exists(out):
        os.makedirs(out)
    fun(0.1, Path + i, out, 'LST_Day_1km-%10.tif')
    fun(0.9, Path + i, out, 'LST_Day_1km-%90.tif')
    fun(0.9, path1 + i, out, 'NDVI-%90.tif')
    fun(0.1, path1 + i, out, 'NDVI-%10.tif')
    # fun(0.1, Path + i, outpath1 + 'float/' + i, 'LST_Day_1km-%10.tif', 'float32')
    # fun(0.9, Path + i, outpath1 + 'float/' + i, 'LST_Day_1km-%90.tif', 'float32')
    # fun(0.9, path1 + i, outpath1 + 'float/' + i, 'NDVI-%90.tif', 'float32')
    # fun(0.1, path1 + i, outpath1 + 'float/' + i, 'NDVI-%10.tif', 'float32')


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(Mon, moth)

# out = outpath1 + '原格式/' + '05_06/'
# if not os.path.exists(out):
#     os.makedirs(out)
# a = fun(0.1, Path + '05_06/', out, 'LST_Day_1km-%10.tif')

