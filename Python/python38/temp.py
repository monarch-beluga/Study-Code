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
from work.meteodata.overseas_data import data_handle
import os

path = r'H:\Monarch\Data\me_data'
os.chdir(path)

me_data_import(f'result/overseas_{1981}.txt', 1981, 'meteodata_extens')
for year in range(1982, 2021):
    data_handle(year)
    me_data_import(f'result/overseas_{year}.txt', year, 'meteodata_extens')


