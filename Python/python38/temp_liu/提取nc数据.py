# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:16:24 2020

@author: JJDre
"""

# import time
# from dateutil.parser import parse
# from datetime import datetime
import numpy as np
import os
import netCDF4 as nc
import pandas as pd
# from shutil import copyfile as cp
from osgeo import gdal, osr
# import sys

path = 'B:/RCP/'
dis = ['RCP26_daily', 'RCP45_daily', 'RCP60_daily', 'RCP85_daily']  #
full = []
for d in dis:
    inpath = path + d + '/daily'
    inpath = os.path.abspath(inpath)
    print(inpath + '##################################################################')
    for root, dirs, files in os.walk(inpath):
        # print(root)
        # print(dirs)
        # print(files)
        for file in files:
            filepath = os.path.join(root, file)
            originc = filepath.replace('\\', '/')
            ofile = file.replace(str(file), d + "_chuli.tif")
            # print(file)
            try:
                NC_DS1 = nc.Dataset(str(originc))
            except BaseException:
                print(originc)
                full.append(d + file)
                f = pd.DataFrame(full)
                f.to_csv(r'B:/RCP/cuowu_nc.csv')
            else:
                # print('ok')

                NC_DS = nc.Dataset(originc)
                # print(1)
                # print(NC_DS,type(NC_DS)) # 了解NC_DS的数据类型，<class 'netCDF4._netCDF4.Dataset'>
                # print(NC_DS.variables) # 了解变量的基本信息
                # z =  xr.open_dataset(originc)
                # print(z['time'])
                # zz = z.variables['time'][:].data
                var = NC_DS.variables['time']
                initial_time = nc.num2date(
                    var, units=var.units, only_use_cftime_datetimes=True)
                p = pd.DataFrame(initial_time)
                # y = pd.Series(range(len(initial_time)), index=xr.CFTimeIndex(initial_time))

                # print(NC_DS.variables['time'])
                # print(NC_DS.variables['pre']) # 了解pre的基本信息
                Lat = NC_DS.variables['lat'][:]
                Lon = NC_DS.variables['lon'][:]

                PRE = NC_DS.variables['pre'][:]
                PRE = np.array(PRE).astype(float)
                # print(PRE[0, :],PRE[0, :].shape)
                PRE[np.where(PRE == 9.96921e+36)] = -9999

                TMIN = NC_DS.variables['tmin'][:]
                TMIN = np.array(TMIN).astype(float)
                TMIN[np.where(TMIN == 9.96921e+36)] = -9999

                TMAX = NC_DS.variables['tmax'][:]
                TMAX = np.array(TMAX).astype(float)
                TMAX[np.where(TMAX == 9.96921e+36)] = -9999

                TMEAN = NC_DS.variables['tmean'][:]
                TMEAN = np.array(TMEAN).astype(float)
                TMEAN[np.where(TMEAN == 9.96921e+36)] = -9999

                LonMin, LatMax, LonMax, LatMin = [
                    Lon.min(), Lat.max(), Lon.max(), Lat.min()]
                N_Lat = len(Lat)
                N_Lon = len(Lon)
                Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
                Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)

                for i in range(len(var[:])):
                    s = p.iloc[i:i + 1, 0:]
                    if len(str(s)) == 45:
                        s1 = str(s)[26:36]
                    else:
                        s1 = str(s)[28:38]
                    print(s1)
                    s1 = s1.replace(' ', '_')
                    # print(s1)
                    pre = PRE[i, :]
                    # print(pre,pre.shape)
                    tmin = TMIN[i, :]
                    # print(tmin,tmin.shape)
                    tmax = TMAX[i, :]
                    tmean = TMEAN[i, :]
                    outfile1 = 'PRE_' + s1 + '_' + ofile
                    outpath1 = path + d + "/PRE"
                    outfile2 = 'TMIN_' + s1 + '_' + ofile
                    outpath2 = path + d + "/TMIN"
                    outfile3 = 'TMAX_' + s1 + '_' + ofile
                    outpath3 = path + d + "/TMAX"
                    outfile4 = 'TMEAN_' + s1 + '_' + ofile
                    outpath4 = path + d + "/TMEAN"

                    out_tif_PRE_P = os.path.join(
                        outpath1, outfile1).replace(
                        '\\', '/')
                    out_tif_TMIN_P = os.path.join(
                        outpath2, outfile2).replace(
                        '\\', '/')
                    out_tif_TMAX_P = os.path.join(
                        outpath3, outfile3).replace(
                        '\\', '/')
                    out_tif_TMEAN_P = os.path.join(
                        outpath4, outfile4).replace(
                        '\\', '/')
# 写入数据
                    out_tif_PRE = gdal.GetDriverByName('Gtiff').Create(
                        out_tif_PRE_P, N_Lon, N_Lat, 1, gdal.GDT_Float32)
                    out_tif_TMIN = gdal.GetDriverByName('Gtiff').Create(
                        out_tif_TMIN_P, N_Lon, N_Lat, 1, gdal.GDT_Float32)
                    out_tif_TMAX = gdal.GetDriverByName('Gtiff').Create(
                        out_tif_TMAX_P, N_Lon, N_Lat, 1, gdal.GDT_Float32)
                    out_tif_TMEAN = gdal.GetDriverByName('Gtiff').Create(
                        out_tif_TMEAN_P, N_Lon, N_Lat, 1, gdal.GDT_Float32)
                    geotransform = (LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res)
                    out_tif_PRE.SetGeoTransform(geotransform)
                    out_tif_TMIN.SetGeoTransform(geotransform)
                    out_tif_TMAX.SetGeoTransform(geotransform)
                    out_tif_TMEAN.SetGeoTransform(geotransform)
                    # 获取地理坐标系统信息，用于选取需要的地理坐标系统
                    srs = osr.SpatialReference()
                    # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
                    srs.ImportFromEPSG(4326)

                    out_tif_PRE.SetProjection(srs.ExportToWkt())
                    out_tif_TMIN.SetProjection(srs.ExportToWkt())
                    out_tif_TMAX.SetProjection(srs.ExportToWkt())
                    out_tif_TMEAN.SetProjection(
                        srs.ExportToWkt())  # 给新建图层赋予投影信

                    out_tif_PRE.GetRasterBand(1).WriteArray(pre)
                    out_tif_TMIN.GetRasterBand(1).WriteArray(tmin)
                    out_tif_TMAX.GetRasterBand(1).WriteArray(tmax)
                    out_tif_TMEAN.GetRasterBand(1).WriteArray(
                        tmean)  # 将数据写入内存，此时没有写入硬盘

                    out_tif_PRE.FlushCache()  # 将数据写入硬盘
                    out_tif_TMIN.FlushCache()  # 将数据写入硬盘
                    out_tif_TMAX.FlushCache()  # 将数据写入硬盘
                    out_tif_TMEAN.FlushCache()  # 将数据写入硬盘

                    out_tif_PRE = None  # 注意必须关闭tif文件
                    out_tif_TMIN = None  # 注意必须关闭tif文件
                    out_tif_TMAX = None  # 注意必须关闭tif文件
                    out_tif_TMEAN = None  # 注意必须关闭tif文件
                    # print(outfile1)
                    # print(outfile2)
                    # print(outfile3)
                    # print(outfile4)


print('结束了提取')
