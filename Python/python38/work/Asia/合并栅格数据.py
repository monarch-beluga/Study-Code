# 时间分辨率上的合并
import rasterio
import os
import shutil
from 筛选栅格数据 import select_date


def merge_data(file_list, path_file, out):
    if not os.path.exists(out):
        os.makedirs(out)
    for year in range(time_start, time_end):
        Files = select_date(file_list, str(year), str(year+1), select_moth)
        if len(Files) %2 != 0:
            shutil.copy(path_file+Files[0], out+Files[0])
            del Files[0]
        for i in range(0, len(Files), 2):
            with rasterio.open(path_file + Files[i]) as src1:
                profile = src1.profile
                data1 = src1.read()[0]
            with rasterio.open(path_file + Files[i+1]) as src2:
                data2 = src2.read()[0]
            data3 = (data1 + data2) / 2.0
            with rasterio.open(out + Files[i], 'w', **profile) as src:
                src.write(data3.astype(rasterio.uint16), 1)


path = "E:/public/Central_Asia/MOD11A2/"
outpath = "E:/public/Central_Asia/MOD11A2-merge/"
files = os.listdir(path)
time_start = 2000
time_end = 2001
select_moth = ["07-01", "10-01"]
# files_select = select_date(files, time_start, time_end, select_moth)
merge_data(files, path, outpath)

