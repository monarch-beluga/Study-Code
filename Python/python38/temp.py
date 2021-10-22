# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import pandas as pd
import pymysql
import geopandas as gpd
from Monarch.import_me_data import *
import os

path = r'H:\Monarch\Data\矢量数据'
os.chdir(path)

sql_name = 'root'
pwd = '123456'
host = 'localhost'
port = 3306
db = 'meteodata'
start_year = 1980
end_year = 2021
types = ['DMXT', 'DMNT', 'MTEM', 'AVRH', 'PREP', 'MEWS', 'SOHR']
conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=db)
roi_shp = r'省级行政区.shp'
gfd = creat_station_geopandas('meteodata')
roi_df = gpd.read_file(roi_shp)
roi_df1 = roi_df[roi_df['NAME'] == '甘肃']
geo = gpd.overlay(gfd, roi_df1, 'intersection')
stations = geo['Code'].tolist()
stations.append(gfd[gfd['Station'] == '祁 连']['Code'].values[0])
# sta_df = pd.DataFrame(gfd[gfd['Code'].isin(stations)].iloc[:, :5])
# sta_df.to_csv(r'H:\Monarch\Data\station.txt', sep=',', header=True, index=False)
# for year in range(start_year, end_year):
#     sql = f'select Station, Year, Month, Day, {",".join(types)} from all{year} where ' \
#           f'Station in ({str(stations).strip("[]")})'
#     df = pd.read_sql(sql, conn)
#     if year == start_year:
#         data = df
#     else:
#         data = pd.concat([data, df])
#     print("进度:{0}/{1}".format(year-start_year+1, end_year-start_year), end="\r")

# data.to_csv(r'H:\Monarch\Data\gsqh.txt', sep=',', header=True, index=False)
data = get_data_by_shp(roi_df1, types, "2001", "2002", "meteodata")
