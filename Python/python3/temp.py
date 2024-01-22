# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

from Monarch import import_me_data

roi_shp = r'D:/Data/parper/data/shp/JX.shp'
types = ['MTEM']
start_time = '2010-01-01'
end_time = '2020-12-31'
db = 'meteodata'
host = '192.168.118.158'
df = import_me_data.get_data_by_shp(roi_shp, types, start_time, end_time, db=db, host=host)



