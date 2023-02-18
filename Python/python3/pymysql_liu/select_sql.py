# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/22
@file: select_sql.py
@function:
@modify:
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine

conn = pymysql.connect(host='192.168.1.116', password='123456', port=3306, user='root')

sql = "select * from meteodata.all2018 where Station='CH000051828'"
df = pd.read_sql(sql, conn)

