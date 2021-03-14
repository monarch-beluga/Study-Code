
import rasterio
import shutil
import numpy as np
import pandas as pd
import os

path = r'E:/temp/LST-NDVI/MOD11-select/'
outpath = r'E:/temp/LST-NDVI/MOD11-merge/'
moth = ['03_04', '05_06', '07_08_09']
for i in moth:
    Path = path + i + '/'
    File = os.listdir(Path)
    for j in range(2000, 2016):
        file = []
        for k in File:
            if str(j) in k:
                file.append(k)
        out = outpath + k + '/'
        if not os.path.exists(out):
            os.makedirs(out)
        if len(file) % 2 != 0:
            shutil.copy(Path + file[-1], out + file[-1])
            del file[-1]
        for k in range(0, len(file), 2):
            with rasterio.open(Path + file[k]) as src1:
                profile = src1.profile
                data1 = src1.read()[0]
            with rasterio.open(Path + file[k+1]) as src2:
                data2 = src2.read()[0]
                data2 = pd.DataFrame(data2)
                data2[data2 == profile.data['nodata']] = np.nan
                data2 = data2.values
            data3 = (data1 + data2) / 2.0
            with rasterio.open(out + file[k], 'w', **profile) as src:
                src.write(data3.astype(rasterio.uint16), 1)







