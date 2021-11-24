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
import os


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print(f_mat.format(*Data.loc[i].to_list()), file=fp)


# path = r'E:\public\sjy'
path = r'H:\Monarch\test'
select_mod = 1
shp_roi = r'roi.shp'
# host = "103.46.128.21"
host = "127.0.0.1"
pwd = "123456"
# port = 29611
port = 3306
sql_name = "root"
db = "meteodata"
types = ['MTEM', 'PREP']
start_time = '2019-09-01'
end_time = '2020-06-01'
sep_day = 8
dem = r'dem.txt'

os.chdir(path)

roi = gpd.read_file(shp_roi)
crs = roi.crs
wgs_roi = roi.to_crs('epsg:4326')


def select_data():
    gdf = creat_station_geopandas(db, sql_name, pwd, host, port, shp_roi)
    geo = gpd.overlay(gdf, wgs_roi, 'intersection')[['Code', 'Station', 'Lat', 'Lon', 'elev', 'geometry']]
    geo.to_file(r'select_station.shp', encoding='utf-8')
    print('station select success!!')
    geo['X'] = geo.geometry.x
    geo['Y'] = geo.geometry.y
    station = geo['Code'].tolist()

    df = get_data_by_stations(station, types, start_time, end_time, db, sql_name, pwd, host, port)
    df.to_csv(r'station_data.txt', index=False, float_format='%.2f')
    print('data select success!!')
    # df = pd.read_csv(r'station_data.txt', header=0)
    df['date'] = df['Year']*10000+df['Month']*100+df['Day']
    for t in types:
        df.loc[(df[t] > 1000) | (df[t] < -100)] = np.nan
    start_year = int(start_time[:4])
    end_year = int(end_time[:4])+1
    for t in types:
        data = df[['Station', 'date', t]]
        for year in range(start_year, end_year):
            data1 = data[data['date']//10000 == year]
            data1.set_index(['Station', 'date'], inplace=True)
            data1 = data1.unstack()
            data1.columns = [i // sep_day for i in range(len(data1.columns))]
            data1 = data1.interpolate(method='linear', limit_direction='both', axis=1)
            data1 = data1.T
            if t == 'PREP':
                data1 = data1.groupby(data1.index).sum().T
            else:
                data1 = data1.groupby(data1.index).mean().T
            geo1 = geo[geo['Code'].isin(data1.index)][['Code', 'X', 'Y', 'elev']].set_index('Code')
            data1 = pd.concat([data1, geo1], axis=1)
            data1.reset_index(inplace=True)
            data1.set_index(['index', 'X', 'Y', 'elev'], inplace=True)
            data1.reset_index(inplace=True)
            count = data1.shape[1]
            if not os.path.exists(t):
                os.makedirs(t)
            with open(f'{t}/{t}_{year:04d}.txt', 'w') as f:
                out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * (count - 4)
                df_format(f, out_format, data1)


# def read_dem():
with open(dem) as dem_f:
    dem_da = dem_f.readlines()
ncols, nrows, xmin, ymin, csize, ndata = [float(dem_da[i].split()[-1]) for i in range(6)]
xmax = xmin + csize * ncols
ymax = ymin + csize * nrows

t = types[0]
fs = os.listdir(t)
f = fs[0]

with open(f'{t}/splina_{f[-8:-4]}.cmd', 'w') as fp:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file=fp)
    if t == 'PREP':
        print(7, file=fp)
    else:
        print(5, file=fp)
    print('2\n1\n0\n0', file=fp)








