# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:50:28 2020

@author: YeHui
"""
import time, os
from glob2 import glob as glb
from multiprocessing import Pool
import multiprocessing
from osgeo import gdal
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression

Ts = time.time()


class para:
    read_xpath = []
    read_ypath = [r'D:\f_work\C_workspace\Sanjy']
    write_path = r'D:\f_work\C_workspace\Sanjy'
    year_set = [2001, 2017]
    cond = [0, 2000]  # 数据有效范围
    xraster_type = []
    yraster_type = ['.flt']
    while_type = '.flt'
    f_coefs = ['NPP_coef']
    f_r2score = 'NPP_r2score'
    f_pvalue = 'NPP_pvalue'


# def read_raster(raster_f):
#     raster_type = raster_f.split('.')[-1]
#     if raster_type == 'flt':
#         raster_arr = np.fromfile(raster_f)
#     else:
#         ds = gdal.Open(raster_f)
#         raster_arr = ds.ReadAsArray()
#     return raster_arr

# read_path = para.read_xpath + para.read_ypath
# raster_type = para.xraster_type + para.yraster_type
# for path, Type in zip(read_path, raster_type):
def Read_data(Paths, Types):
    DAta = []
    for path, Type in zip(Paths, Types):
        for year in range(para.year_set[0], para.year_set[1] + 1):
            file = glb(path + os.sep + "*" + str(year) + "*" + Type)[0]
            ds = gdal.Open(file)
            img_data = ds.ReadAsArray()  # 读取整幅图像转化为数组
            img_data[np.isnan(img_data)] = para.cond[0] - 1
            img_data = img_data.reshape(-1, 1)  # 将数组转化为1行，自定义列的数组
            if year == para.year_set[0]:
                data = img_data
            else:
                data = np.hstack((data, img_data))
        DAta.append(data)
    DAta = np.array(DAta)
    return DAta


def linear_trend(datay, *datax):
    """
    :param datay:
    :param datax:
    :return: 返回趋势r2score和显著性水平pvalue
    """
    DATA = []
    for i, temp in enumerate(datax):
        temp = temp.reshape(-1, 1)
        if i == 0:
            x_data = temp
        else:
            x_data = np.hstack((x_data, temp))
    if (len(x_data[np.isnan(x_data)]) > 0) | (len(datay[np.isnan(datay)]) > 0):
        return np.full((i + 3), np.nan)
    else:
        regr = LinearRegression().fit(x_data, datay)
        for i in regr.coef_:
            DATA.append(i)
        y_pred = regr.predict(x_data)
        r2score = r2_score(datay, y_pred)
        pvalue = f_regression(datay.reshape(-1, 1), y_pred)[1][0]
        DATA.append(r2score)
        DATA.append(pvalue)
        DATA = np.array(DATA)
        return DATA


def write_raster(file, data, ds):
    """
    :param file: 输出tif文件名
    :param data: 写入的数组
    :param ds: raster properties
    """
    driver = gdal.GetDriverByName('GTiff')  # 明确写入数据驱动类型
    out_ds = driver.Create(
        para.write_path + file,  # tif文件所保存的路径
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


def zip1(iterablesx, iterablesy):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators1 = [iter(it) for it in iterablesx]
    iterators2 = [iter(it) for it in iterablesy]
    iterators = iterators2 + iterators1
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


if __name__ == '__main__':
    # 将数组转换成以象元数为行数，年份为列数的数组
    file = glb(para.read_ypath[0] + os.sep + '*' + str(para.year_set[0]) + '*' + para.yraster_type[0])
    ds = gdal.Open(file[0])
    img_x = ds.RasterXSize
    img_y = ds.RasterYSize
    if len(para.read_xpath) == 0:
        x_var_time = np.arange(para.year_set[0], para.year_set[1] + 1)
        P = ds.RasterXSize * ds.RasterYSize
        N = len(x_var_time)
        data_x = np.zeros((P, N))
        data_x = [data_x]
    else:
        data_x = Read_data(para.read_xpath, para.xraster_type)
    data_y = Read_data(para.read_ypath, para.yraster_type)
    data_x[(data_x > para.cond[0]) | (data_x <= para.cond[1])] = np.nan
    data_y[(data_y > para.cond[0]) | (data_y <= para.cond[1])] = np.nan
    map_argu = zip1(data_x, data_y)
    cores = multiprocessing.cpu_count()
    pool = Pool(cores)
    Regres_ = pool.starmap(linear_trend, map_argu)

    # save arrays for output files
    Regres_ = np.array(Regres_)
    num = len(Regres_[0])
    coef_arrs = []
    for i in range(num - 2):
        temp = Regres_[:, i].reshape(img_y, img_x)
        coef_arrs.append(temp)
    r2_arr = Regres_[:, num - 2].reshape(img_y, img_x)
    p_arr = Regres_[:, num - 1].reshape(img_y, img_x)
    if para.while_type == 'flt':
        for k, f_coef in enumerate(para.f_coefs):
            coef_arr = coef_arrs[k]
            coef_arr.astype('float32').tofile(f_coef)
        r2_arr.astype('float32').tofile(para.f_r2score)
        p_arr.astype('float32').tofile(para.f_pvalue)
    else:
        for k, f_coef in enumerate(para.f_coefs):
            coef_arr = coef_arrs[k]
            write_raster(f_coef, coef_arr, ds)
        write_raster(para.f_r2score, r2_arr, ds)
        write_raster(para.f_pvalue, p_arr, ds)

    Te = time.time()
    print(Te - Ts)
