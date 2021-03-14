# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:50:28 2020

@author: YeHui
"""
import datetime, os
from glob import glob as glb
from multiprocessing import Pool
import multiprocessing
from osgeo import gdal
import numpy as np
import pandas as pd
from scipy import stats
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.feature_selection import f_regression

Ts = datetime.datetime.now()
dir_rasters = r'D:\f_work\C_workspace\Sanjy'
dest_folder = dir_rasters
year_set = 2001, 2017
var_str = 'NPP'
cond = [0, 2000]  # 数据有效范围
raster_type = 'flt'
f_coef = dest_folder + os.sep + var_str + '_coef.' + raster_type
f_r2score = dest_folder + os.sep + var_str + '_r2score.' + raster_type
f_pvalue = dest_folder + os.sep + var_str + '_pvalue.' + raster_type

x_var_time = np.arange(year_set[0], year_set[1] + 1)  # 时间轴

N = len(x_var_time)  # time series for N years


# def read_raster(raster_f):  
#     raster_type = raster_f.split('.')[-1] 
#     if raster_type == 'flt':
#         raster_arr = np.fromfile(raster_f)
#     else:
#         ds = gdal.Open(raster_f)
#         raster_arr = ds.ReadAsArray()
#     return raster_arr
    
for i, year in enumerate(list(x_var_time)):
    file = glb(dir_rasters + os.sep + "*" + str(year) + "*." + raster_type)[0]
    ds = gdal.Open(file)
    img_data = ds.ReadAsArray()  # 读取整幅图像转化为数组
    img_data = img_data.reshape(1, -1)  # 将数组转化为1行，自定义列的数组
    if i == 0:
        # 影像数据基本情况 波段数、行、列等
        im_width = ds.RasterXSize  # 行
        im_height = ds.RasterYSize  # 列
        im_bands = ds.RasterCount  # 波段数
        band1 = ds.GetRasterBand(1)  # 波段的indice起始为1，不为0
        img_datatype = band1.DataType  # 数据类型
        data_y = np.zeros((N, im_height * im_width), dtype=float)  # 建立数组 N * P
        # continue
    data_y[i] = img_data


def linear_trend(map_argu):
    """
    :param y_data:
    :return: 返回趋势r2score和显著性水平pvalue
    """
    # list_uzip = list(zip(*map_argu))
    # data_x, data_y = np.array(list_uzip[0]), np.array(list_uzip([1]))
    data_x = x_var_time
    df = pd.DataFrame({"indepent": data_x, "depent": map_argu})  # 建立dataframe
    df = df.dropna()  # 删除nan值所在的行
    if df.count()[0] < N:  # 统计剩余值得数量，如果低于26，则这组数据的趋势和显著性水平按nan值处理
        return np.nan, np.nan, np.nan  # 返回nan值
    else:
        x = df["indepent"].values
        y = df["depent"].values
        OLS = stats.linregress(data1, data2)
        y_pred = regr.predict(x)
        coef = regr.coef_  # 回归系数 or slope
        r2score = r2_score(y, y_pred)  # 绝对相关系数
        pvalue = f_regression(x, y)[1][0]  # 显著性水平
        return coef, r2score, pvalue  # 返回趋势和显著性水平


def write_raster(file, data, ds):
    """
    :param file: 输出tif文件名
    :param data: 写入的数组
    :param ds: raster properties
    """
    driver = gdal.GetDriverByName('GTiff')  # 明确写入数据驱动类型
    out_ds = driver.Create(
        file,  # tif文件所保存的路径
        ds.RasterXSize,  # 行
        ds.RasterYSize,  # 列
        ds.RasterCount,  # 波段数
        ds.GetRasterBand(1).DataType)  # 数据类型
    out_ds.SetProjection(ds.GetProjection())  # 投影信息
    out_ds.SetGeoTransform(ds.GetGeoTransform())  # 仿射信息
    for i in range(1, ds.RasterCount + 1):  # 循环逐波段写入
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(data)  # 写入数据
    out_ds.FlushCache()
    del out_ds


if __name__ == '__main__':
    # 将数组转换成以象元数为行数，年份为列数的数组
    data_y = data_y.T
    data_y[np.where((data_y > cond[1]) | (data_y <= cond[0]))] = np.nan
    P = ds.RasterXSize * ds.RasterYSize
    cores = multiprocessing.cpu_count()
    pool = Pool(cores)
    Regres_ = pool.map(linear_trend, data_y)

    # save arrays for output files
    Regres_ = np.array(Regres_)
    coef_arr = Regres_[:, 0].reshape(im_height, im_width)
    r2_arr = Regres_[:, 1].reshape(im_height, im_width)
    p_arr = Regres_[:, 2].reshape(im_height, im_width)

    #
    if raster_type == 'flt':
        coef_arr.astype('float32').tofile(f_coef)
        r2_arr.astype('float32').tofile(f_r2score)
        p_arr.astype('float32').tofile(f_pvalue)
    else:
        write_raster(f_coef, coef_arr, ds)
        write_raster(f_r2score, r2_arr, ds)
        write_raster(f_pvalue, p_arr, ds)
        
    Te = datetime.datetime.now()
    print((Ts - Te).seconds)
