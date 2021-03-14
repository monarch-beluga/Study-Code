
from osgeo import gdal
import numpy as np
import sys

dat = []
f_raster = r'E:\study\资料\数据\sjy250m_dem\sjy250m_dem.tif'
ds = gdal.Open(f_raster)
im_width = ds.RasterXSize
im_height = ds.RasterYSize
xBSize = 128
yBSize = 128
for i in range(0, im_height, yBSize):
    if i + yBSize < im_height:
        numRows = yBSize
    else:
        numRows = im_height - i
    for j in range(0, im_width, xBSize):
        if j + xBSize < im_width:
            numCols = xBSize
        else:
            numCols = im_width - j
        data = np.full((1, numRows, numCols), 1)
        data = ds.ReadAsArray(j, i, numCols, numRows)
        dat.append(data)
# print(dat)
print(sys.getsizeof(dat))
print(sys.getsizeof(ds.ReadAsArray()))
