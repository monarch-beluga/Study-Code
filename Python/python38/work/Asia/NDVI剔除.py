# 剔除NDVI < 0.05的数据
import rasterio
import os
from concurrent.futures.thread import ThreadPoolExecutor
from 筛选栅格数据 import select_date


time_start = "2000"
time_end = "2016"
select_moth = ["03-01", "10-01"]
path = r'E:/public/Central_Asia/MOD13A2/'
outpath = r'E:/public/Central_Asia/MOD13A2-tichu/'

if not os.path.exists(outpath):
    os.makedirs(outpath)


def tichu(file):
    with rasterio.open(path+file) as read_src:
        data_read = read_src.read()[0].astype('float32')
        profile = read_src.profile
        data_read[((data_read < 500) & (data_read != -3000)) | (data_read == profile['nodata'])] = -3000
        profile['nodata'] = -3000
    with rasterio.open(outpath+file, 'w', **profile) as write_src:
        write_src.write(data_read.astype(profile['dtype']), 1)


File = os.listdir(path)
File_select = select_date(File, time_start, time_end, select_moth)
with ThreadPoolExecutor(max_workers=80) as executor:
    executor.map(tichu, File_select)


