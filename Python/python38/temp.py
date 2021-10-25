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
import os

path = r'H:\Monarch\Data\me_data'
os.chdir(path)

year = 1980

me_data_import(f'result/overseas_{year}.txt', year, 'meteodata_extens')


