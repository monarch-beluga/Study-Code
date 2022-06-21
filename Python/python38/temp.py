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
from datetime import timedelta

start_time = datetime.strptime("2021-06", "%Y-%m")
end_time = datetime.strptime("2021-08", "%Y-%m")

sep = 5
s_time = start_time
e_time = start_time+timedelta(days=sep)

while e_time < end_time:
    print(s_time.strftime("%Y-%m-%d"), e_time.strftime("%Y-%m-%d"))
    s_time = e_time
    e_time += timedelta(days=sep)



