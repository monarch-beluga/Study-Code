
import rasterio
import numpy as np
import pandas as pd
import os

path = r'E:/work/孟印缅/LST_NDVI/'
outpath = r'E:/work/孟印缅/LST_NDVI-cf/'
moths = ['03_04/', '05_06/', '07_08_09/']

for moth in moths:
    Path = path + moth
    files = os.listdir(Path)
    out = outpath + moth
    if not os.path.exists(out):
        os.makedirs(out)
    for file in files:
        with rasterio.open(Path + file) as src:
            profile = src.profile
            data = src.read()[0]
            # data = pd.DataFrame(data)
            # data[data == profile.data["nodata"]] = np.nan
            # data = data.values
            # data = pd.DataFrame(data)
            data[(data != profile.data["nodata"]) & (data < 0) & (data > -50)] = -1
            data[(data != profile.data["nodata"]) & (data <= -50) & (data >= -75)] = -2
            data[(data != profile.data["nodata"]) & (data < -75)] = -3
            data[(data != profile.data["nodata"]) & (data > 0) & (data < 50)] = 1
            data[(data != profile.data["nodata"]) & (data >= 50) & (data <= 75)] = 2
            data[(data != profile.data["nodata"]) & (data > 75)] = 3
            # data = data.values
        with rasterio.open(out + file, "w", **profile) as src_write:
            src_write.write(data.astype(profile.data['dtype']), 1)
            # src_write.write(data.astype(profile.data['dtype']), 1)




