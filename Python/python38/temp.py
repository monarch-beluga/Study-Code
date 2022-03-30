# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: data_year_to_day.py
@function:
@modify:
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import os

path = r'D:\meteodata'
os.chdir(path)

station = gpd.read_file('select_station.shp')
station = station.iloc[:, :5]
station = station.dropna()
station.to_csv('station.txt', index=False)
