# 数据的缺失值处理，这个时计算 极端时件 前的操作
import pandas as pd
import rasterio
import os
import numpy as np
from concurrent.futures.thread import ThreadPoolExecutor
from 筛选栅格数据 import select_date

outpath = r'E:/public/Central_Asia/MOD13A2-Interpolation/'
path = r"E:/public/Central_Asia/MOD13A2-tichu/"
time_start = "2000"
time_end = "2016"
select_moth = ["07-01", "10-01"]

files = os.listdir(path)
files = select_date(files, time_start, time_end, select_moth)
with rasterio.open(path + files[0]) as src:
    windows = [window for i, window in src.block_windows()]
    profile = src.profile
if not os.path.exists(outpath):
    os.makedirs(outpath)


def linear(x):
    for y1, y in enumerate(x):
        if (np.isnan(y).sum()) > (len(y) / 1.5):
            da = y
        else:
            y = pd.DataFrame(y)
            da = y.interpolate(method='linear', limit_direction='both')
        x[y1] = np.array(da).flatten()
    return x


def read(file):
    with rasterio.open(path+file) as src1:
        da = src1.read()[0].astype("float32")
        da[da == profile.data['nodata']] = np.nan
    return da


def writer_data(write_f, data_write):
    with rasterio.open(outpath+write_f, "w", **profile) as write_src:
        write_src.write(data_write.astype(profile.data["dtype"]), 1)


with ThreadPoolExecutor(max_workers=40) as worker:
    data = [i for i in worker.map(read, files)]
data = np.array(data).transpose(1, 2, 0)
with ThreadPoolExecutor(max_workers=80) as worker:
    data = np.array([x for x in worker.map(linear, data)])
data = data.transpose(2, 0, 1)
with ThreadPoolExecutor(max_workers=40) as worker:
    worker.map(writer_data, files, data)

