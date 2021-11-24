# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

# 最终的ECA处理
import work.Asia.eca as eca
from concurrent.futures.thread import ThreadPoolExecutor
from glob import glob
import rasterio
import numpy as np
import os
from work.Asia.筛选栅格数据 import select_date
import time

paths = [r"H:/Monarch/Data/TAVG/", r'H:/Monarch/Data/NDVI/']
outpath = "H:/Monarch/Data/ECA/05-06/"
time_start = "1982"
time_end = "2016"
select_moth = ["05-01", "06-01"]
path_judgments = ["H:/Monarch/Data/05-06/TAVG/", "H:/Monarch/Data/05-06/NDVI/"]
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





def read_data(file):
    with rasterio.open(file) as src:
        profile = src.profile
        temp = src.read()[0].astype("float32")
        temp[temp == profile.data['nodata']] = np.nan
    return temp


def process_data(judgment_src, files_src):
    judgments_data_min = read_data(judgment_src[0])
    judgments_data_max = read_data(judgment_src[1])
    j = 0
    for temp in map(read_data, files_src):
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
        profile.data['dtype'] = 'float32'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    profile.data["nodata"] = -3000
    judgment_src_s = []
    files_src_s = []
    for judgment_path, path in zip(path_judgments, paths):
        judgment_files = glob(judgment_path + '*.tif')
        files = glob(path + '*.tif')
        files = select_date(files, time_start, time_end, select_moth)
        judgment_src_s.append(judgment_files)
        files_src_s.append(files)
    print("open-----end")
    return profile, judgment_src_s, files_src_s


def ECA_process(judgment_src_s, files_src_s):
    data1_min, data1_max = process_data(judgment_src_s[0], files_src_s[0])
    data2_min, data2_max = process_data(judgment_src_s[1], files_src_s[1])
    with ThreadPoolExecutor(max_workers=80) as worker_temp:
        data_min = np.array([i for i in worker_temp.map(Eca, data1_min, data2_min, data2_max)]).reshape(profile['height'], profile['width'])
        data_max = np.array([i for i in worker_temp.map(Eca, data1_max, data2_min, data2_max)]).reshape(profile['height'], profile['width'])
    return data_min, data_max
    # return height, width


profile, judgment_src_s, files_src_s = open_src()
data_W = ECA_process(judgment_src_s, files_src_s)
data1_min, data1_max = process_data(judgment_src_s[0], files_src_s[0])
data2_min, data2_max = process_data(judgment_src_s[1], files_src_s[1])
# for data_W, window in zip(map(ECA_process,
#                                [judgment_src_s] * len(windows),
#                                [files_src_s] * len(windows),
#                                windows,
#                                [i for i in range(len(windows))],
#                                [len(windows)]*len(windows)),
#                           windows):
#
#     for data_w, write_src in zip(data_W, write_src_s):
#         # print(data_w)
#         data_w *= 100
#         data_w[np.isnan(data_w)] = -3000
#         write_src.write(data_w.astype(profile.data['dtype']), 1, window=window)
# with ThreadPoolExecutor(max_workers=30) as worker:
#     worker.map(close_file, write_src_s)
#     for files_src, judgment_src in zip(files_src_s, judgment_src_s):
#         worker.map(close_file, files_src)
#         worker.map(close_file, judgment_src)





