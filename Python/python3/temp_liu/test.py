# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/12/27
@file: temp.py
@function:
@modify:
"""

from Monarch.import_me_data import *
import geopandas as gpd
import pandas as pd
import numpy as np
import time
import rasterio
from glob import glob
import os
from concurrent.futures.thread import ThreadPoolExecutor

# ============================================用户修改部分=====================================================
# -------------------本地数据目录配置------------------
# path = r'E:\public\sjy'                 # 数据所在目录
dem = r'dem.txt'                        # 高程数据(ASCII码栅格)
path = r'E:\Monarch\TAVG'
shp_roi = r'roi_prj.shp'                    # 选取的矢量站点的范围(其投影要与高程一致)

# ------------------数据库连接配置-------------------
# host = "103.46.128.21"                  # ip地址
host = "127.0.0.1"
# port = 29611                            # 端口
port = 3306
sql_name = "root"                       # 用户名称
pwd = "123456"                          # 用户密码
dbs = ["meteodata", "meteodata_extens"]                       # 需要查询的数据库, 国内使用meteodata, 国外使用meteodata_extens

# -----------------插值配置------------------------
types = ['MTEM']                # 插值的要素
out_pre = ['TAVG']
q = 0.8                                 # 数据完整性百分比
# types: list, 要获取的气象要素列表:
#     |APRE: 平均本站气压 | DMXP:日最高本站气压 | DMNP: 日最低本站气压 | MTEM: 平均气温 | DMXT: 日最高气温|
#     |DMNT: 日最低气温 | AVRH: 平均相对湿度 | MNRH: 最小相对湿度 | PREP: 降水量 | MEWS: 平均风速 |
#     |MXWS: 最大风速|DMWS: 最大风速的风向|EXWS: 极大风速|DEWS: 极大风速的风向|SOHR: 日照时数|
start_time = '2019-01-01'               # 插值起始时间
end_time = '2019-02-01'                 # 插值结束时间
sep_day = 1                             # 插值尺度(单位：日)

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
columns = []
knots = 0


def df_format(fp, f_mat, Data):
    for i in range(len(Data)):
        print(f_mat.format(*Data.loc[i].to_list()), file=fp)


def select_data():
    global knots
    if type(dbs) == str:
        gdf = creat_station_geopandas(dbs, sql_name, pwd, host, port, shp_roi)
    else:
        temp_geo = []
        for db in dbs:
            temp_geo.append(creat_station_geopandas(db, sql_name, pwd, host, port, shp_roi))
        gdf = gpd.GeoDataFrame(pd.concat(temp_geo), crs='EPSG:4326')
    geo = gpd.overlay(gdf, wgs_roi, 'intersection')[['Code', 'Station', 'Lat', 'Lon', 'elev', 'geometry']]
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
    print('data select success!!')
    # df = pd.read_csv(r'station_data.txt', header=0)
    df['date'] = df['Year'] * 10000 + df['Month'] * 100 + df['Day']
    for t in types:
        df.loc[(df[t] > 1000) | (df[t] < -100), t] = np.nan
    for t, out_t in zip(types, out_pre):
        if not os.path.exists(out_t):
            os.makedirs(out_t)
        data1 = df[['Station', 'date', t]]
        data1.set_index(['Station', 'date'], inplace=True)
        data1 = data1.unstack()
        data1 = data1.interpolate(method='linear', limit_direction='both', axis=1)
        columns.append(df["date"].unique())
        data1.columns = columns[0]
        geo1 = geo[geo['Code'].isin(data1.index)][['Code', 'X', 'Y', 'elev']].set_index('Code')
        data1 = pd.concat([data1, geo1], axis=1)
        data1.reset_index(inplace=True)
        data1.set_index(['index', 'X', 'Y', 'elev'], inplace=True)
        data1.reset_index(inplace=True)
        count = data1.shape[1] - 4
        knots = data1.shape[0]
        i = 0
        while count > 88:
            count -= 88
            with open(f'{out_t}/{out_t}_{i:04d}.dat', 'w') as f:
                out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * 88
                df_format(f, out_format, data1.iloc[:, i * 88:(i + 1) * 88])
            i += 1
        with open(f'{out_t}/{out_t}_{i:04d}.dat', 'w') as f:
            out_format = '{:11s}' + '{:12.2f}' * 2 + '{:10.3f}' + '{:10.2f}' * count
            df_format(f, out_format, data1.iloc[:, i * 88:])
    return columns


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


def create_selnot(t, f, dem_min, dem_max, pre):
    with open(f'{f}') as fp:
        sta_data = fp.readline().split()
    count_grd = len(sta_data) - 4
    climate_list = ['.not', '.rej']
    with open(f'{pre}/splina_{f[-8:-4]}.cmd', 'w') as fp:
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
        print(f'0\n{count_grd}\n0', file=fp)
        print(path + os.sep + f, file=fp)
        print('10000\n11', file=fp)
        print(f'(a11,2f12.2,f10.3,{count_grd}f10.2)', file=fp)
        for i in climate_list:
            print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}{i}', file=fp)
        print(f'{knots/2}', file=fp)
    print(f'{pre}/selnot_{f[-8:-4]}.cmd create success!!')


def create_splinb(t, f, dem_min, dem_max, pre):
    with open(f'{f}') as fp:
        sta_data = fp.readline().split()
    count_grd = len(sta_data) - 4
    climate_list = ['.flg', '.res', '.opt', '.sur', '.lis', '.cov']
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
        print('10000\n11', file=fp)
        print(f'(a11,2f12.2,f10.3,{count_grd}f10.2)', file=fp)
        print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}.not', file=fp)
        print("1000\n\n", file=fp)
        for i in climate_list:
            print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}{i}', file=fp)
        print('\n\n', file=fp)
    print(f'{pre}/splinb_{f[-8:-4]}.cmd create success!!')


def create_lapgrd(f, pre):
    outpath = ['RES', 'COV']
    for i in outpath:
        if not os.path.exists(pre + os.sep + i):
            os.makedirs(pre + os.sep + i)
    res_name = []
    cov_name = []
    a = int(f[-8:-4])
    count_grd = columns[0][a*88:(a+1)*88]
    for i, j in enumerate(count_grd):
        res_name.append(pre + os.sep + outpath[0] + os.sep + f'{pre}_{j}')
        # shutil.copy(dem.split('.')[0] + '.prj', res_name[i] + '.prj')
        cov_name.append(pre + os.sep + outpath[1] + os.sep + f'{pre}_{j}_COV')
        # shutil.copy(dem.split('.')[0] + '.prj', cov_name[i] + '.prj')
    with open(f'{pre}/lapgrd_{f[-8:-4]}.cmd', 'w') as fp:
        print(path + os.sep + pre + os.sep + f'climateVar_{f[-8:-4]}.sur', file=fp)
        print(' '.join([str(i) for i in range(1, len(count_grd) + 1)]), file=fp)
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

    for t, pre in zip(types, out_pre):
        fs = glob(pre+os.sep+'*.dat')
        # f = fs[0]
        for f in fs:
            if knots < 2000:
                create_splina(t, f, dem_min, dem_max, pre)
            else:
                create_selnot(t, f, dem_min, dem_max, pre)
                create_splinb(t, f, dem_min, dem_max, pre)
            create_lapgrd(f, pre)


def exec_cmd(cmd):
    print(cmd+' execute......')
    os.system(cmd)
    print(cmd+' execute success!!')


def execute_cmd():
    if knots < 2000:
        splina_files = glob(f'*{os.sep}splina*.cmd')
        splina_cmd = [f'splina<{f}>{f.replace(".cmd", ".log")}' for f in splina_files]
        with ThreadPoolExecutor(max_workers=80) as worker:
            worker.map(exec_cmd, splina_cmd)
    else:
        selnot_files = glob(f'*{os.sep}selnot*.cmd')
        selnot_cmd = [f'selnot<{f}>{f.replace(".cmd", ".log")}' for f in selnot_files]
        splinb_files = glob(f'*{os.sep}splinb*.cmd')
        splinb_cmd = [f'splinb<{f}>{f.replace(".cmd", ".log")}' for f in splinb_files]
        with ThreadPoolExecutor(max_workers=80) as worker:
            worker.map(exec_cmd, selnot_cmd)
            worker.map(exec_cmd, splinb_cmd)
    lapgrd_files = glob(f'*{os.sep}lapgrd*.cmd')
    lapgrd_cmd = [f'lapgrd<{f}>{f.replace(".cmd", ".log")}' for f in lapgrd_files]

    for cmd in lapgrd_cmd:
        exec_cmd(cmd)


zst = time.time()
select_data()
create_cmd()
execute_cmd()
print(f'Interpolation success!!, 总耗时:{time.time()-zst:.2f}s')




