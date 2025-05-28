# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r"D:\Work\PCB行业化学品")

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/esocs')

df = pd.read_excel("PCB行业企业清单 - 副本.xlsx", sheet_name="Sheet1")

df1 = pd.DataFrame()
df1['name'] = df['企业名称']
df1['pwd'] = "123456"
df1['permissions'] = 'ordinary'
df1.to_sql(name='users', con=engine, if_exists='append', index=False)

