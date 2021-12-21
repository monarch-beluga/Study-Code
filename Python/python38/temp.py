# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

from Monarch.import_me_data import *
import geopandas as gpd
import pandas as pd
import numpy as np
import time
from datetime import datetime
import shutil
import rasterio
from glob import glob
import os
from concurrent.futures.thread import ThreadPoolExecutor

# ============================================用户修改部分=====================================================
# -------------------本地数据目录配置------------------
# path = r'E:\public\sjy'                 # 数据所在目录
dem = r'dem.txt'                        # 高程数据(ASCII码栅格)
path = r'H:\Monarch\temp'
shp_roi = r'roi.shp'                    # 选取的矢量站点的范围(其投影要与高程一致)

# ------------------数据库连接配置-------------------
# host = "103.46.128.21"                  # ip地址
host = "127.0.0.1"
# port = 29611                            # 端口
port = 3306
sql_name = "root"                       # 用户名称
pwd = "123456"                          # 用户密码
dbs = ["meteodata", "meteodata_extens"]                       # 需要查询的数据库, 国内使用meteodata, 国外使用meteodata_extens

# -----------------插值配置------------------------
types = ['MNRH']                # 插值的要素
out_pre = ['RHU']
q = 0.8                                 # 数据完整性百分比
# types: list, 要获取的气象要素列表:
#     |APRE: 平均本站气压 | DMXP:日最高本站气压 | DMNP: 日最低本站气压 | MTEM: 平均气温 | DMXT: 日最高气温|
#     |DMNT: 日最低气温 | AVRH: 平均相对湿度 | MNRH: 最小相对湿度 | PREP: 降水量 | MEWS: 平均风速 |
#     |MXWS: 最大风速|DMWS: 最大风速的风向|EXWS: 极大风速|DEWS: 极大风速的风向|SOHR: 日照时数|
start_time = '2018-01-01'               # 插值起始时间
end_time = '2020-12-31'                 # 插值结束时间
sep_day = 1                             # 插值尺度(单位：日)
process = 4                             # 插值时并行个数(最大值 = cup逻辑处理器个数 - 2)

# =======================================================================================================

# =======================================程序内置部分(不要修改)===============================================
os.chdir(path)
roi = gpd.read_file(shp_roi)
crs = roi.crs
wgs_roi = roi.to_crs('epsg:4326')
# with open(dem) as dem_f:
#     ncols, nrows, xmin, ymin, csize, ndata = [float(dem_f.readline().split()[-1]) for i in range(6)]
# xmax = xmin + csize * ncols
# ymax = ymin + csize * nrows


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print(f_mat.format(*Data.loc[i].to_list()), file=fp)


def select_data():
    if type(dbs) == str:
        gdf = creat_station_geopandas(dbs, sql_name, pwd, host, port, shp_roi)
    else:
        temp_geo = []
        for db in dbs:
            temp_geo.append(creat_station_geopandas(db, sql_name, pwd, host, port, shp_roi))
        gdf = gpd.GeoDataFrame(pd.concat(temp_geo)).to_crs('epsg:4326')
    geo = gpd.overlay(gdf, wgs_roi, 'intersection')[['Code', 'Station', 'Lat', 'Lon', 'elev', 'geometry']]
    geo.to_file(r'select_station.shp', encoding='utf-8')
    # geo = gpd.read_file(r'select_station.shp')
    print('station select success!!')
    geo = geo.to_crs(crs)
    geo['X'] = geo.geometry.x
    geo['Y'] = geo.geometry.y
    station = geo['Code'].tolist()
    if type(dbs) == str:
        df = get_data_by_stations(station, types, start_time, end_time, dbs, sql_name, pwd, host, port)
    else:
        temp_data = []
        for db in dbs:
            temp_data.append(get_data_by_stations(station, types, start_time, end_time, db, sql_name, pwd, host, port))
        df = pd.concat(temp_data)
    df.to_csv(r'station_data.txt', index=False, float_format='%.2f')
    # df = pd.read_csv(r'station_data.txt', header=0)
    print('data select success!!')
    # df = pd.read_csv(r'station_data.txt', header=0)
    df['date'] = df['Year'] * 10000 + df['Month'] * 100 + df['Day']
    for t in types:
        df.loc[(df[t] > 1000) | (df[t] < -100), t] = np.nan
    start_year = int(start_time[:4])
    end_year = int(end_time[:4]) + 1
    for t, out_t in zip(types, out_pre):
        if not os.path.exists(out_t):
            os.makedirs(out_t)
        data = df[['Station', 'date', t]]
        for year in range(start_year, end_year):
            data1 = data[data['date'] // 10000 == year]
            data1.set_index(['Station', 'date'], inplace=True)
            data1 = data1.unstack()
            data1.columns = [i // sep_day for i in range(len(data1.columns))]
            count = data1.shape[1]
            data1.drop(data1[data1.count(1) < count*q].index, inplace=True)
            data1 = data1.interpolate(method='linear', limit_direction='both', axis=1)
            geo1 = geo[geo['Code'].isin(data1.index)][['Code', 'X', 'Y', 'elev']].set_index('Code')
            data1 = pd.concat([data1, geo1], axis=1)
            data1.reset_index(inplace=True)
            data1.set_index(['index', 'X', 'Y', 'elev'], inplace=True)
            data1.reset_index(inplace=True)
            count = data1.shape[1]
            with open(f'{out_t}/{out_t}_{year:04d}.dat', 'w') as f:
                out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * (count - 4)
                df_format(f, out_format, data1)


select_data()

print('Interpolation success!!')

