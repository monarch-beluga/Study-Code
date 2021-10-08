# 最终的ECA处理
import eca as eca
from concurrent.futures.thread import ThreadPoolExecutor
from glob import glob
import rasterio
import numpy as np
import os
from 筛选栅格数据 import select_date
import time

paths = ["E:/public/Central_Asia/MOD11A2-Interpolation/", r'E:/public/Central_Asia/MOD13A2-Interpolation/']
outpath = "E:/public/Central_Asia/ECA/05-06/"
time_start = "2000"
time_end = "2016"
select_moth = ["05-01", "07-01"]
path_judgments = ["E:/public/Central_Asia/extremum/05-06/LST_Day_1km/", "E:/public/Central_Asia/extremum/05-06/NDVI/"]
out_files = [r'LST_min.tif', r'LST_max.tif']
st = time.time()


def Eca(dataA, dataB, dataC):
    if ((np.isnan(dataA).sum() + np.isnan(dataB).sum()) > 0) or (len(dataA[dataA == 1]) != len(dataB[dataB == 1])) or \
            (len(dataA[dataA == 1]) < len(dataA) // 10):
        data1 = np.nan
    else:
        data1 = eca.ECA(dataA, dataB, delT=0)[0]
    if ((np.isnan(dataA).sum() + np.isnan(dataC).sum()) > 0) or (len(dataA[dataA == 1]) != len(dataC[dataC == 1])) or \
            (len(dataA[dataA == 1]) < len(dataA) // 10):
        data2 = np.nan
    else:
        data2 = eca.ECA(dataA, dataC, delT=0)[0]
    if np.isnan(data1) and np.isnan(data2):
        return np.nan
    elif np.isnan(data1):
        return data2
    elif np.isnan(data2):
        return data1
    if data1 < data2:
        return data2
    else:
        return -data1


def open_file(file):
    return rasterio.open(file)


def close_file(src):
    src.close()


def read_data(src, win):
    profile = src.profile
    temp = src.read(window=win)[0].astype("float32")
    temp[temp == profile.data['nodata']] = np.nan
    return temp


def process_data(judgment_src, files_src, win):
    judgments_data_min = read_data(judgment_src[0], win)
    judgments_data_max = read_data(judgment_src[1], win)
    j = 0
    for temp in map(read_data, files_src, [win]*len(files_src)):
        data_max = np.array(temp)
        data_min = np.array(temp)
        data_min[~np.isnan(data_min)] = 0
        data_max[~np.isnan(data_max)] = 0
        data_max[temp > judgments_data_max] = 1
        data_min[temp < judgments_data_min] = 1
        data_min = data_min.reshape(-1, 1)
        data_max = data_max.reshape(-1, 1)
        # temp = temp.reshape(-1, 1)
        if j == 0:
            data1 = data_min
            data2 = data_max
            # data3 = temp
        else:
            data1 = np.hstack([data1, data_min])
            data2 = np.hstack([data2, data_max])
            # data3 = np.hstack([data3, temp])
        j += 1
    return data1, data2


def open_src():
    judgment = os.listdir(path_judgments[1])
    with rasterio.open(path_judgments[1] + judgment[0]) as src_temp:
        profile = src_temp.profile
        windows = [window for i, window in src_temp.block_windows()]
        profile.data['dtype'] = 'float32'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    profile.data["nodata"] = -3000
    judgment_src_s = []
    files_src_s = []
    write_src_s = []
    for write_file in out_files:
        src_write = rasterio.open(outpath + write_file, 'w', **profile)
        write_src_s.append(src_write)

    for judgment_path, path in zip(path_judgments, paths):
        judgment_files = glob(judgment_path + '*.tif')
        judgment_src = [i for i in map(open_file, judgment_files)]
        files = glob(path + '*.tif')
        files = select_date(files, time_start, time_end, select_moth)
        with ThreadPoolExecutor(max_workers=30) as worker:
            files_src = [src for src in worker.map(open_file, files)]
        judgment_src_s.append(judgment_src)
        files_src_s.append(files_src)
    print("open-----end")
    return profile, judgment_src_s, files_src_s, windows, write_src_s


def ECA_process(judgment_src_s, files_src_s, window, j, N):
    height = window.height
    width = window.width
    data1_min, data1_max = process_data(judgment_src_s[0], files_src_s[0], window)
    data2_min, data2_max = process_data(judgment_src_s[1], files_src_s[1], window)
    with ThreadPoolExecutor(max_workers=80) as worker_temp:
        data_min = np.array([i for i in worker_temp.map(Eca, data1_min, data2_min, data2_max)]).reshape(height, width)
        data_max = np.array([i for i in worker_temp.map(Eca, data1_max, data2_min, data2_max)]).reshape(height, width)
    p = round((j + 1) * 100 / N, 2)
    duration = round(time.time() - st, 2)
    remaining = round(duration * 100 / (0.01 + p) - duration, 2)
    print("进度:{0}%，已耗时:{1}s，预计剩余时间:{2}s".format(p, duration, remaining), end="\r")
    return data_min, data_max
    # return height, width


profile, judgment_src_s, files_src_s, windows, write_src_s = open_src()
for data_W, window in zip(map(ECA_process,
                               [judgment_src_s] * len(windows),
                               [files_src_s] * len(windows),
                               windows,
                               [i for i in range(len(windows))],
                               [len(windows)]*len(windows)),
                          windows):
    for data_w, write_src in zip(data_W, write_src_s):
        # print(data_w)
        data_w *= 100
        data_w[np.isnan(data_w)] = -3000
        write_src.write(data_w.astype(profile.data['dtype']), 1, window=window)
with ThreadPoolExecutor(max_workers=30) as worker:
    worker.map(close_file, write_src_s)
    for files_src, judgment_src in zip(files_src_s, judgment_src_s):
        worker.map(close_file, files_src)
        worker.map(close_file, judgment_src)
