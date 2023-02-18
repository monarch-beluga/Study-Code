#
import rasterio
import os
import numpy as np
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from 筛选栅格数据 import select_date

paths = ["E:/public/Central_Asia/MOD11A2-Interpolation/", r'E:/public/Central_Asia/MOD13A2-Interpolation/']
outpath = "E:/public/Central_Asia/extremum/05-06/"
time_start = "2000"
time_end = "2016"
select_moth = ["05-01", "07-01"]
file_writes = ["LST_Day_1km/", "NDVI/"]
extremum_q = [0.1, 0.9]

for i in file_writes:
    if not os.path.exists(outpath + i):
        os.makedirs(outpath + i)


def extremum(qs, input_path, file_write, btype=None):

    # q = 0.1
    # path = r'E:/temp/MOD11-merge/'
    # outpath = r'E:/temp/LST_Day_1km-NDVI/'
    # file_write = 'LST_Day_1km-%10.tif'
    File = os.listdir(input_path)
    File = select_date(File, time_start, time_end, select_moth)
    with rasterio.open(input_path + File[0]) as src:
        windows = [window for i, window in src.block_windows()]
        profile = src.profile
        if btype is not None:
            profile.data['dtype'] = btype
        if profile.data['nodata'] == -32768:
            profile.data['nodata'] = -3000

    def read_data(file, win):
        with rasterio.open(input_path + file) as src_read:
            temp = src_read.read(window=win)[0].astype("float32")
            temp[temp == profile.data['nodata']] = np.nan
        return temp

    src_writes = []
    for q in qs:
        src_write = rasterio.open(outpath + file_write + str(q) + '.tif', "w", **profile)
        src_writes.append(src_write)
    for window in windows:
        with ThreadPoolExecutor(max_workers=80) as worker:
            data = np.array([i for i in worker.map(read_data, File, [window]*len(File))])
        for q, src_write in zip(qs, src_writes):
            data_write = np.quantile(data, q, axis=0).reshape(window.height, window.width)
            src_write.write(data_write.astype(profile.data['dtype']), 1, window=window)
    for src_write in src_writes:
        src_write.close()
    # return data


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.map(extremum, [extremum_q]*len(paths), paths, file_writes)

