# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

# from PyEMD import EEMD
# from concurrent.futures.thread import ThreadPoolExecutor
# import time
# import numpy as np
#
# s = 1980
# e = 2018
# T = np.array(list(range(s, e + 1)))
# m = 1000
# x0 = np.random.rand(m, 39)
# eemd = EEMD(100, 0.01)
#
#
# def eemd_data(y):
#     y4 = eemd.eemd(y, T, -1)
#     y5 = y4[-1]
#     y6 = y5 - y5[0]
#     y7 = np.diff(y6)
#     y8 = y7.mean()
#     # print(y8)
#     return y8


# if __name__ == "__main__":
#     st = time.time()
#     with ThreadPoolExecutor(max_workers=30) as pool:
#         ts = np.array([i for i in pool.map(eemd_data, x0)])
#     mn = ts.mean()
#     sd = ts.std()
#     print(time.time()-st)


from Monarch.import_me_data import *
import pymysql
import pandas as pd

host = "103.46.128.21"
pwd = "123456"
port = 29611
sql_name = "root"
database = "meteodata"
conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=database)

sql = "select `code`, `X`, `Y`,`stationName` from station where Y between 24 and 31 and X between 113 and 118.5"
station = pd.read_sql(sql, conn)
code_sta = station['code'].tolist()
types = ['DMNT', 'DMXT']
data = get_data_by_stations(code_sta, types, "2017", "2019", db=database, host=host, port=port)
