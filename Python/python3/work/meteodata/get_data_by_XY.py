# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/11/02
@file: get_data_by_XY.py
@function:
@modify:
"""

from Monarch.import_me_data import *
import pymysql
import pandas as pd

host = "192.168.118.158"
pwd = "123456"
port = 3066
sql_name = "root"
database = "meteodata"
conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=database)

sql = "select `code`, `X`, `Y`,`stationName` from station where Y between 24 and 31 and X between 113 and 118.5"
station = pd.read_sql(sql, conn)
code_sta = station['code'].tolist()
types = ['DMNT', 'DMXT']
data = get_data_by_stations(code_sta, types, "2019-01-01", "2019-06-08", db=database, host=host, port=port,
                            time_merge=True)

conn.close()
