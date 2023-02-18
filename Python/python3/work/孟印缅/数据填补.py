
import pandas as pd
import rasterio
import shutil
import os
import numpy as np
from concurrent.futures.process import ProcessPoolExecutor

path2 = r'E:/work/孟印缅/MYD11-select/'
path1 = r'E:/work/孟印缅/MOD11-select/'
outpath = r'E:/work/孟印缅/MOD11-filling/'

moth = [['_03_', '_04_'], ['_05_', '_06_'], ['_07_', '_08_', '_09_']]


def fun(select):
    s = [jj.strip('_') for jj in select]
    s = '_'.join(s)
    out = outpath + s + '/'
    if not os.path.exists(out):
        os.makedirs(out)
    for i in select:
        Path1 = path1 + i + '/'
        Path2 = path2 + i + '/'
        File1 = os.listdir(Path1)
        File2 = os.listdir(Path2)
        for j in range(2003, 2020):
            file1 = []
            for k in File1:
                if str(j) in k:
                    file1.append(k)
            file2 = []
            for k in File2:
                if str(j) in k:
                    file2.append(k)
            for f1, f2 in zip(file1, file2):
                with rasterio.open(Path1 + f1) as src1:
                    profile1 = src1.profile
                    data1 = src1.read()[0]
                    data1 = pd.DataFrame(data1)
                    data1[data1 == profile1.data['nodata']] = np.nan
                    # data1 = data1.values
                with rasterio.open(Path2 + f2) as src2:
                    profile2 = src2.profile
                    data2 = src2.read()[0]
                    data2 = pd.DataFrame(data2)
                    data2[data2 == profile2.data['nodata']] = np.nan
                    # data2 = data2.values
                data1[np.isnan(data1)] = data2
                data1 = data1.values
                with rasterio.open(out + f1, 'w', **profile1) as src:
                    src.write(data1.astype(rasterio.uint16), 1)


# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         executor.map(fun, moth)
#     print("end")


for select in moth:
    s = [jj.strip('_') for jj in select]
    s = '_'.join(s)
    out = outpath + s + '/'
    for i in select:
        Path = path1 + i + '/'
        File = os.listdir(Path)
        for j in range(2000, 2003):
            file = []
            for k in File:
                if str(j) in k:
                    file.append(k)
            for f in file:
                shutil.copy(Path + f, out + f)


