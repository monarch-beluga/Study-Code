# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/11/25
@file: anusplin_use.py
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

# ============================================用户修改部分=====================================================
# -------------------本地数据目录配置------------------
path = r'E:\public\sjy'                 # 数据所在目录
dem = r'dem.txt'                        # 高程数据(ASCII码栅格)
# path = r'H:\Monarch\test'
shp_roi = r'roi.shp'                    # 选取的矢量站点的范围(其投影要与高程一致)

# ------------------数据库连接配置-------------------
host = "103.46.128.21"                  # ip地址
# host = "127.0.0.1"
port = 29611                            # 端口
# port = 3306
sql_name = "root"                       # 用户名称
pwd = "123456"                          # 用户密码
dbs = "meteodata"                       # 需要查询的数据库, 国内使用meteodata, 国外使用meteodata_extens

# -----------------插值配置------------------------
types = ['MTEM', 'PREP']                # 插值的要素
out_pre = ['TAVG', 'PRCP']
q = 0.8                                 # 数据完整性百分比
# types: list, 要获取的气象要素列表:
#     |APRE: 平均本站气压 | DMXP:日最高本站气压 | DMNP: 日最低本站气压 | MTEM: 平均气温 | DMXT: 日最高气温|
#     |DMNT: 日最低气温 | AVRH: 平均相对湿度 | MNRH: 最小相对湿度 | PREP: 降水量 | MEWS: 平均风速 |
#     |MXWS: 最大风速|DMWS: 最大风速的风向|EXWS: 极大风速|DEWS: 极大风速的风向|SOHR: 日照时数|
start_time = '2019-01-01'               # 插值起始时间
end_time = '2019-02-31'                 # 插值结束时间
sep_day = 8                             # 插值尺度(单位：日)

# =======================================================================================================

# =======================================程序内置部分(不要修改)===============================================
os.chdir(path)
roi = gpd.read_file(shp_roi)
crs = roi.crs
wgs_roi = roi.to_crs('epsg:4326')
with open(dem) as dem_f:
    ncols, nrows, xmin, ymin, csize, ndata = [float(dem_f.readline().split()[-1]) for i in range(6)]
xmax = xmin + csize * ncols
ymax = ymin + csize * nrows


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
        gdf = gpd.GeoDataFrame(pd.concat(temp_geo))
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
    years = df['Year'].unique()
    # start_year = int(start_time[:4])
    # end_year = int(end_time[:4]) + 1
    for t, out_t in zip(types, out_pre):
        if not os.path.exists(out_t):
            os.makedirs(out_t)
        data = df[['Station', 'date', t]]
        for year in years:
            data1 = data[data['date'] // 10000 == year]
            data1.set_index(['Station', 'date'], inplace=True)
            data1 = data1.unstack()
            data1.columns = [i // sep_day for i in range(len(data1.columns))]
            count = data1.shape[1]
            data1.drop(data1[data1.count(1) < count*q].index, inplace=True)
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
            with open(f'{out_t}/{out_t}_{year:04d}.dat', 'w') as f:
                out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * (count - 4)
                df_format(f, out_format, data1)


def create_splina(t, f, dem_min, dem_max, pre):
    with open(f'{f}') as fp:
        sta_data = fp.readline().split()
    count_grd = len(sta_data) - 4
    climate_list = ['.res', '.opt', '.sur', '.lis', '.cov']
    with open(f'{pre}/splina_{f[-8:-4]}.cmd', 'w') as fp:
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
            print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}{i}', file=fp)
        print('\n\n', file=fp)
    print(f'{pre}/splina_{f[-8:-4]}.cmd create success!!')


def create_lapgrd(f, pre):
    outpath = ['RES', 'COV']
    with open(f'{f}') as fp:
        sta_data = fp.readline().split()
    count_grd = len(sta_data) - 4
    for i in outpath:
        if not os.path.exists(pre + os.sep + i):
            os.makedirs(pre + os.sep + i)
    if f[-8:-4] == start_time[:4]:
        date_start_moth = datetime.strptime(start_time, "%Y-%m-%d")
    else:
        date_start_moth = datetime.strptime(f'{f[-8:-4]}-01-01', "%Y-%m-%d")
    res_name = []
    cov_name = []
    date = datetime.strptime(f'{f[-8:-4]}', '%Y')
    day = (date_start_moth - date).days+1
    for i in range(count_grd):
        res_name.append(pre + os.sep + outpath[0] + os.sep + f'{pre}_{f[-8:-4]}{day:03d}')
        shutil.copy(dem.split('.')[0] + '.prj', res_name[i] + '.prj')
        cov_name.append(pre + os.sep + outpath[1] + os.sep + f'{pre}_{f[-8:-4]}{day:03d}_COV')
        shutil.copy(dem.split('.')[0] + '.prj', cov_name[i] + '.prj')
        day += sep_day
    with open(f'{pre}/lapgrd_{f[-8:-4]}.cmd', 'w') as fp:
        print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}.sur', file=fp)
        print(' '.join([str(i) for i in range(1, count_grd + 1)]), file=fp)
        print('1', file=fp)
        print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}.cov', file=fp)
        print('2\n\n1\n1', file=fp)
        print(f'{xmin} {xmax} {csize}', file=fp)
        print('2', file=fp)
        print(f'{ymin} {ymax} {csize}', file=fp)
        print('0\n2', file=fp)
        print(path + os.sep + dem, file=fp)
        print('2\n-9999.0', file=fp)
        for i in res_name:
            print(path + os.sep + i + '.grd', file=fp)
        print(f'({ncols:.0f}f10.2)', file=fp)
        print('2\n-9999.0', file=fp)
        for i in cov_name:
            print(path + os.sep + i + '.grd', file=fp)
        print(f'({ncols:.0f}f10.2)', file=fp)
    print(f'{pre}/lapgrd_{f[-8:-4]}.cmd create success!!')


def create_cmd():
    with rasterio.open(dem) as src:
        profile = src.profile
        dem_data = src.read(1)
        dem_min = dem_data[dem_data != profile['nodata']].min()
        dem_max = dem_data[dem_data != profile['nodata']].max()
        del dem_data
    # t = types[0]
    for t, pre in zip(types, out_pre):
        fs = glob(pre+os.sep+'*.dat')
        # f = fs[0]
        for f in fs:
            create_splina(t, f, dem_min, dem_max, pre)
            create_lapgrd(f, pre)


def exec_cmd(cmd):
    print(cmd+' execute......')
    os.system(cmd)
    print(cmd+' execute success!!')


def execute_cmd():
    splina_files = glob(f'*{os.sep}splina*.cmd')
    lapgrd_files = glob(f'*{os.sep}lapgrd*.cmd')
    for f in splina_files:
        exec_cmd(f'splina<{f}>{f.replace(".cmd", ".log")}')
    for f in lapgrd_files:
        exec_cmd(f'lapgrd<{f}>{f.replace(".cmd", ".log")}')


select_data()
create_cmd()
execute_cmd()
print('Interpolation success!!')

