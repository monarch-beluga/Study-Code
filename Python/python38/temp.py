# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: temp.py
@function:
@modify:
"""

from Monarch.import_me_data import *
import os

os.chdir(r'H:\Monarch\Data\矢量数据')

types = ['DMNT', 'DMXT']

st_list = get_data_by_shp('gansu.shp', types=types, start_time='2020', end_time='2020-01-02', db='meteodata')




