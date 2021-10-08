# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:53:40 2021

@author: 佩奇
"""

from netCDF4 import Dataset
import pandas as pd
import numpy as np 
import netCDF4 as nc
from osgeo import gdal
import os, time
import glob
from osgeo import osr
from netCDF4 import date2num , num2date, Dataset
path = r'I:\ear5\1'
outpath = r'I:\ear5\2'
fpaths = glob.glob(path  + '//' + '*.nc')
for fpath in fpaths:
    data1 = nc.Dataset(fpath)
    nc_info = data1.variables
    # print(data1.variables.keys())
    # for var in data1.variables.keys():
    #     data=data1.variables[var][:].data
        # print(var,data.shape)
    sd = data1.variables['t2m']
    lon = data1.variables['longitude'][:]
    lat = data1.variables['latitude'][:]
    with Dataset(fpath) as root:
        time1 = root.variables['time'][:]
        dates = num2date(time1, root.variables['time'].units)
        dates1 = pd.DataFrame(dates)
    # print(dates[1].strftime('%Y%m%d%H'))
    lonmin, latmax, lonmax, latmin = [lon.min(), lat.max(), lon.max(), lat.min()]
    l_lat = len(lat)
    l_lon = len(lon)
    lat_ce = (latmax - latmin)/(l_lat - 1)
    lon_ce = (lonmax - lonmin)/(l_lon - 1)
    year = int(fpath.split('\\')[-1].split('.')[0])
    if ((year%4==0) and (year%100!=0)) or (year % 400==0):
        
        day_t = 29
    else:
        day_t = 28
    ls = [31,day_t ,31,30,31,30,31,31,30,31,30,31]
    star = 0
    end = 0
    ct = 0
    for i in range(12):
        
        end += ls[i]*24
        t2m_arr = np.asarray(data1.variables['t2m'][star:end])
        arr = t2m_arr.sum(axis = 0)
        arr2 = arr / ls[i]
        arr3 = arr2 - 273.15 * 24
        arr4 = arr3/24
        ct +=1
        out_path = outpath + '\\'  +str(year) + "_" + str(ct)  +".tif"
        GDB = gdal.GetDriverByName('Gtiff')
        tif1 = GDB.Create(out_path, l_lon, l_lat, 1, gdal.GDT_Float32 )
        geotransform1 = [lonmin, lon_ce, 0, latmax, 0, -lat_ce]  #设置影像显示范围
        tif1.SetGeoTransform(geotransform1)  #      
        geo1 = osr.SpatialReference() #获取地理坐标系统信息，用于选取需要的地理坐标系统
        geo1.ImportFromEPSG(4326)    # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
        tif1.SetProjection(geo1.ExportToWkt())# 给新建图层赋予投影信息
        tif1.GetRasterBand(1).WriteArray(arr3)#写出数据
        tif1.FlushCache()
        tif1 = None
#       print('Finished')
        
        star = end
    print(year)
print('finished')
        
        
    # out_path = outpath + '\\' + str(year)
    # for year in range(1979, 2019):
    #     fpaths = glob.glob(path + '//' + f'*{year}*.tif')
    #     if ((year%4==0) and (year%100!=0)) or (year % 400==0):
    #         day_t = 29
    #     else:
    #         day_t = 28
    #     ls = [31,day_t ,31,30,31,30,31,31,30,31,30,31]
        
    
   
    
# path=r'D:\aaaa\prate.sfc.mon.mean.nc'
# out_path=r'D:\aaaa'
# data = nc.Dataset(path)
# nc_info = data.variables
# ndvi = data.variables['prate']  
# lon = data.variables['lon'][:]
# lat = data.variables['lat'][:]
# ndvi_arr = np.asarray(data.variables['prate']) 
# with Dataset(path) as root:
#     time1 = root.variables['time'][:]
#     dates = num2date(time1, root.variables['time'].units)
#     dates1 = pd.DataFrame(dates)
# print(dates[1].strftime('%Y%m%d%H'))
# lonmin, latmax, lonmax, latmin = [lon.min(), lat.max(), lon.max(), lat.min()]  #获取四个角信息
# #计算输出栅格数据分辨率
# l_lat = len(lat)
# l_lon = len(lon)
# lat_ce = (latmax - latmin)/(l_lat - 1)
# lon_ce = (lonmax - lonmin)/(l_lon - 1)
# for yr in range(1979, 2021):
#     for mon in range(0, 12):
#         for i in range(0, 503):    
#             fgrd1 = out_path + os.sep + 'prate_'  +str(yr) + '-' + str(mon) + '-'+  '01.tif'
#             arr1 = ndvi_arr[i,:,:]
#             GDB = gdal.GetDriverByName('Gtiff')
#             #.Create(dst_filename, wide, high, 1, gdalconst.GDT_Int16)
#             tif1 = GDB.Create(fgrd1, l_lon, l_lat, 1, gdal.GDT_Float32 )
#             #    tif2 = GDB.Create(out_tif2, l_lon, l_lat, 1, gdal.GDT_Float32 )#create tif file
#             # #[lon_topleft, lon_resolution, lat_skew, lat_topleft, lon_skew, lat_resolution] 仿射变换；二维坐标（x, y）到二维坐标（u, v）的线性变换  #Define the geotransform used to convert x/y pixel to lon/lat degree       
#             geotransform1 = [lonmin, lon_ce, 0, latmax, 0, -lat_ce]  #设置影像显示范围
#             tif1.SetGeoTransform(geotransform1)  #      
#             geo1 = osr.SpatialReference() #获取地理坐标系统信息，用于选取需要的地理坐标系统
#             geo1.ImportFromEPSG(4326)    # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
#             tif1.SetProjection(geo1.ExportToWkt())# 给新建图层赋予投影信息
#             tif1.GetRasterBand(1).WriteArray(arr1)#写出数据
#             tif1.FlushCache()
#             tif1 = None
#         print('Finished')