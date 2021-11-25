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
from datetime import timedelta
import shutil
import rasterio
from glob import glob
import os


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print(f_mat.format(*Data.loc[i].to_list()), file=fp)


path = r'E:\public\sjy'
# path = r'H:\Monarch\test'
select_mod = 1
shp_roi = r'roi.shp'
host = "103.46.128.21"
# host = "127.0.0.1"
pwd = "123456"
port = 29611
# port = 3306
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
    # geo = gpd.read_file(r'select_station.shp')
    print('station select success!!')
    geo = geo.to_crs(crs)
    geo['X'] = geo.geometry.x
    geo['Y'] = geo.geometry.y
    station = geo['Code'].tolist()

    df = get_data_by_stations(station, types, start_time, end_time, db, sql_name, pwd, host, port)
    df.to_csv(r'station_data.txt', index=False, float_format='%.2f')
    # df = pd.read_csv(r'station_data.txt', header=0)
    print('data select success!!')
    # df = pd.read_csv(r'station_data.txt', header=0)
    df['date'] = df['Year']*10000+df['Month']*100+df['Day']
    for t in types:
        df.loc[(df[t] > 1000) | (df[t] < -100)] = np.nan
    start_year = int(start_time[:4])
    end_year = int(end_time[:4])+1
    for t in types:
        if not os.path.exists(t):
            os.makedirs(t)
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
            with open(f'{t}/{t}_{year:04d}.dat', 'w') as f:
                out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * (count - 4)
                df_format(f, out_format, data1)


# select_data()
# def read_dem():
with open(dem) as dem_f:
    ncols, nrows, xmin, ymin, csize, ndata = [float(dem_f.readline().split()[-1]) for i in range(6)]
xmax = xmin + csize * ncols
ymax = ymin + csize * nrows


def create_splina(t, f, dem_min, dem_max):
    with open(f'{f}') as fp:
        sta_data = fp.readline().split()
    count_grd = len(sta_data) - 4
    climate_list = ['.res', '.opt', '.sur', '.lis', '.cov']
    with open(f'{t}/splina_{f[-8:-4]}.cmd', 'w') as fp:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file=fp)
        if t == 'PREP':
            print(7, file=fp)
        else:
            print(5, file=fp)
        print('2\n1\n0\n0', file=fp)
        x = 1
        if crs.axis_info[0].unit_name == 'metre':
            x = 1
        elif crs.axis_info[0].unit_name == 'degree':
            x = 5
        print(f'{xmin - 10 * csize} {xmax + 10 * csize} 0 {x}', file=fp)
        print(f'{ymin - 10 * csize} {ymax + 10 * csize} 0 {x}', file=fp)
        print(f'{dem_min} {dem_max} 1 1', file=fp)
        print('1000.00', file=fp)
        print(f'0\n2\n{count_grd}\n0\n1\n1', file=fp)
        print(path + os.sep + f, file=fp)
        print('3000\n11', file=fp)
        print(f'(a11,2f12.2,f10.3,{count_grd}f10.2)', file=fp)
        for i in climate_list:
            print(path + os.sep + t + os.sep + f'climateVar_{f[-8:-4]}{i}', file=fp)
        print('\n\n', file=fp)
    print(f'splina_{f[-8:-4]}.cmd create success!!')


def create_cmd():
    with rasterio.open(dem) as src:
        dem_data = src.read(1)
        dem_min = dem_data.min()
        dem_max = dem_data.max()
        del dem_data
    # t = types[0]
    for t in types:
        fs = glob(t+os.sep+'*.dat')
        # f = fs[0]
        for f in fs:
            create_splina(t, f, dem_min, dem_max)


# create_cmd()
outpath = ['RES', 'COV']
t = types[0]
fs = glob(t+os.sep+'*.dat')
f = fs[0]
with open(f'{f}') as fp:
    sta_data = fp.readline().split()
count_grd = len(sta_data) - 4
for i in outpath:
    if not os.path.exists(t+os.sep+i):
        os.makedirs(t+os.sep+i)
date_start_moth = datetime.strptime(start_time, "%Y-%m-%d")
res_name = []
cov_name = []
for i in range(count_grd):
    date = (date_start_moth+timedelta(days=sep_day*i)).date()
    res_name.append(t+os.sep+outpath[0]+os.sep+f'RES_{date}')
    shutil.copy(dem.split('.')[0]+'.prj', res_name[i]+'.prj')
    cov_name.append(t+os.sep+outpath[1]+os.sep+f'COV_{date}')
    shutil.copy(dem.split('.')[0]+'.prj', cov_name[i]+'.prj')
with open(f'{t}/lapgrd_{f[-8:-4]}.cmd', 'w') as fp:
    print(path+os.sep+t+os.sep+f'climateVar_{f[-8:-4]}.sur', file=fp)
    print(' '.join([str(i) for i in range(1, count_grd+1)]), file=fp)
    print('1', file=fp)
    print(path+os.sep+t+os.sep+f'climateVar_{f[-8:-4]}.cov', file=fp)
    print('2\n\n1\n1', file=fp)
    print(f'{xmin} {xmax} {csize}', file=fp)
    print('2', file=fp)
    print(f'{ymin} {ymax} {csize}', file=fp)
    print('0\n2', file=fp)
    print(path+os.sep+dem, file=fp)
    print('2\n-9999.0', file=fp)
    for i in res_name:
        print(path+os.sep+i+'.grd', file=fp)
    print(f'({ncols:.0f}f10.2)', file=fp)
    print('2\n-9999.0', file=fp)
    for i in cov_name:
        print(path+os.sep+i+'.grd', file=fp)
    print(f'({ncols:.0f}f10.2)', file=fp)



