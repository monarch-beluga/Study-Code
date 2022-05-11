# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""
from datetime import datetime

year = 2015
month = [['03', '05']]
y_time = datetime.strptime(f'{year}', "%Y")
s_time = datetime.strptime(f'{year}-{month[0][0]}', "%Y-%m")
e_time = datetime.strptime(f'{year}-{month[0][1]}', "%Y-%m")
