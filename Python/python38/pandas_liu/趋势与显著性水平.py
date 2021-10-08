import os
import time
import multiprocessing
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression


def Write(file, data, ds, img_datatype):
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(
        r'E:/study/资料/数据/趋势与显著性水平/' + file,
        ds.RasterXSize,
        ds.RasterYSize,
        ds.RasterCount,
        img_datatype)
    out_ds.SetProjection(ds.GetProjection())
    out_ds.SetGeoTransform(ds.GetGeoTransform())
    for i in range(1, ds.RasterCount + 1):
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(data)
    out_ds.FlushCache()
    del out_ds


def fun(File1, File2, File3, File4, File5):
    start = time.time()
    file1 = r'E:/study/资料/数据/'
    ds = gdal.Open(file1 + File1)       # 打开文件
    im_width = ds.RasterXSize       # 列数
    im_height = ds.RasterYSize      # 行数
    im_bands = ds.RasterCount       # 波段数
    band1 = ds.GetRasterBand(1)
    img_datatype = band1.DataType
    data1 = np.full((39, im_height, im_width), 1.0)
    data2 = np.linspace(1980, 2019, 39)
    data3 = np.full((im_height, im_width), 1.0)
    data4 = np.full((im_height, im_width), 1.0)
    for year in range(1980, 2019):
        file2 = file1 + File2 + str(year) + File3
        ds = gdal.Open(file2)
        img_data = ds.ReadAsArray()     # 读取整幅图像转化为数组
        data1[year - 1980] = img_data

    for x in range(0, im_height):
        for y in range(0, im_width):
            x_data = data1[:, x, y]
            y_data = data2
            x_data = x_data.reshape(-1, 1)
            regr = LinearRegression()
            regr.fit(x_data, y_data)
            y_pred = regr.predict(x_data)
            r2score = r2_score(y_data, y_pred)
            pvalue = f_regression(x_data, y_data)[1][0]
            data3[x][y] = r2score
            data4[x][y] = pvalue
    Write(File4, data3, ds, img_datatype)
    Write(File5, data4, ds, img_datatype)
    end = time.time()
    print(end - start)


fun(r'prcp_year/PRCP1980SUM.tif', r'prcp_year/PRCP', r'SUM.tif', r'prcp趋势.tif', r'prcp显著性水平.tif')
# fun(r'tmax_year/TMAX1980MEAN.tif', r'tmax_year/TMAX', r'MEAN.tif', r'tmax趋势.tif', r'tmax显著性水平.tif')
# fun(r'tmean_year/TAVG1980_mean.tif', r'tmean_year/TAVG', r'_mean.tif', r'tmean趋势.tif', r'tmean显著性水平.tif')
# fun(r'tmin_year/TMIN1980MEAN.tif', r'tmin_year/TMIN', r'MEAN.tif', r'tmin趋势.tif', r'tmin显著性水平.tif')
