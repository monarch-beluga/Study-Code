
import pandas as pd
import rasterio
import os
from glob import glob
import numpy as np
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

outpath = r'E:/work/孟印缅/MOD11-Interpolation/'
path = r'E:/work/孟印缅/MOD11-merge/'
moths = ['03_04/', '05_06/', '07_08_09/']
Out = []
PATH = []

for moth in moths:
    Path = path + moth
    PATH.append(Path)
    out = outpath + moth
    if not os.path.exists(out):
        os.makedirs(out)
    Out.append(out)


def linear(x):
    for y1, y in enumerate(x):
        if (np.isnan(y).sum()) > (len(y) / 1.5):
            da = y
        else:
            y = pd.DataFrame(y)
            da = y.interpolate(method='linear', limit_direction='both')
        x[y1] = np.array(da).flatten()
    return x


def read(f):
    with rasterio.open(f) as src:
        profile = src.profile
        da = src.read()[0]
        # da = pd.DataFrame(da)
        da[da == profile.data['nodata']] = np.nan
        # da = da.values
    return da, profile


def writer1(data_writer, f, profile):
    with rasterio.open(f, 'w', **profile) as src:
        src.write(data_writer.astype(rasterio.uint16), 1)


def fun(Path, out):
    File = glob(Path + '*.*')
    data = []
    profiles = []
    with ThreadPoolExecutor(max_workers=20) as worker:
        for i in worker.map(read, File):
            data.append(i[0])
            profiles.append(i[1])
    data = np.array(data).transpose(1, 2, 0)
    outfile = [''.join([out, i.split('\\')[-1]]) for i in File]
    with ThreadPoolExecutor(max_workers=15) as worker:
        data = np.array([x for x in worker.map(linear, data)])
    data = data.transpose(2, 0, 1)

    with ThreadPoolExecutor(max_workers=15) as worker:
        worker.map(writer1, data, outfile, profiles)


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(fun, PATH, Out)







