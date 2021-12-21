# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/11/25
@file: temp.py
@function:
@modify:
"""
# 模块导入
import numpy as np
import netCDF4 as nc
from osgeo import gdal, osr, ogr
import os
import glob


# 单个nc数据ndvi数据读取为多个tif文件，并将ndvi值化为-1-1之间
def NC_to_tiffs(data, Output_folder, t):
    nc_data_obj = nc.Dataset(data)
    Lon = nc_data_obj.variables['XLONG'][:]
    Lat = nc_data_obj.variables['XLAT'][:]
    ndvi_arr = np.asarray(nc_data_obj.variables[t])  # 将ndvi数据读取为数组
    # ndvi_arr_float = ndvi_arr.astype(float)/10000 #将int类型改为float类型,并化为-1 - 1之间

    # 影像的左上角和右下角坐标
    LonMin, LatMax, LonMax, LatMin = [Lon.min(), Lat.max(), Lon.max(), Lat.min()]

    # 分辨率计算
    N_Lat, N_Lon = Lon.shape
    Lon_Res = (LonMax - LonMin) / (float(N_Lon) - 1)
    Lat_Res = (LatMax - LatMin) / (float(N_Lat) - 1)

    for i in range(len(ndvi_arr[:])):
        # 创建.tif文件
        driver = gdal.GetDriverByName('GTiff')
        out_tif_name = Output_folder + '\\' + data.split('\\')[-1].split('.')[0] + '_' + str(i + 1) + '.tif'
        out_tif = driver.Create(out_tif_name, N_Lon, N_Lat, 1, gdal.GDT_Float32)

        # 设置影像的显示范围
        # -Lat_Res一定要是-的
        geotransform = (LonMin, Lon_Res, 0, LatMax, 0, -Lat_Res)
        out_tif.SetGeoTransform(geotransform)

        # 获取地理坐标系统信息，用于选取需要的地理坐标系统
        srs = osr.SpatialReference()
        srs.ImportFromEPSG(4326)  # 定义输出的坐标系为"WGS 84"，AUTHORITY["EPSG","4326"]
        out_tif.SetProjection(srs.ExportToWkt())  # 给新建图层赋予投影信息

        # 数据写出
        out_tif.GetRasterBand(1).WriteArray(ndvi_arr[i])  # 将数据写入内存，此时没有写入硬盘
        out_tif.FlushCache()  # 将数据写入硬盘
        out_tif = None  # 注意必须关闭tif文件


def main():
    path = r'E:\Data\temp\nc'
    out = '_tif'
    os.chdir(path)
    folder1 = os.listdir()
    folder2 = os.listdir(folder1[0])
    for i in folder1:
        if not os.path.exists(i+out):
            os.mkdir(i+out)
        for j in folder2:
            out_path = f'{i}{out}/{j}'
            if not os.path.exists(out_path):
                os.mkdir(out_path)
    # 读取所有nc数据
            data_list = glob.glob(f'{i}/{j}/*.nc')

            for data in data_list:
                NC_to_tiffs(data, out_path, j)
                print(data + '-----转tif成功')

    print('----转换结束----')


main()


