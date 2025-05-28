# -*- coding: utf-8 -*-
# @Time    : 2025/5/21 下午2:43
# @Author  : Monarch
# @File    : PCB行业化学品CAS.py
# @Software: PyCharm

import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r"D:\Work\PCB行业化学品")

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/esocs')

ds = {
    "基本信息调查": "基本环境信息",
    "详细调查": "详细调查信息",
    "重点管控": "重点管控信息",
    "公约类物质": "公约履约信息"
}

key = "基本信息调查"
df = pd.read_excel("2-化学物质环境信息统计调查物质清单-内部参考.xlsx", sheet_name=key)
df1 = pd.DataFrame()
df1['name'] = df['名称']
df1['cas'] = df['CAS/流水号']
df1['type'] = ds[key]

key = "详细调查"
df2 = pd.DataFrame()
df = pd.read_excel("2-化学物质环境信息统计调查物质清单-内部参考.xlsx", sheet_name=key)
df2['name'] = df['名称']
df2['cas'] = df['CAS']
df2['type'] = ds[key]

key = "重点管控"
df3 = pd.DataFrame()
df = pd.read_excel("2-化学物质环境信息统计调查物质清单-内部参考.xlsx", sheet_name=key)
df3['name'] = df['名称']
df3['cas'] = df['CAS']
df3['type'] = ds[key]

key = "公约类物质"
df4 = pd.DataFrame()
df = pd.read_excel("2-化学物质环境信息统计调查物质清单-内部参考.xlsx", sheet_name=key)
df4['name'] = df['名称']
df4['cas'] = df['CAS号']
df4['type'] = ds[key]

df = pd.concat([df1, df2, df3, df4])
df5 = df.drop_duplicates("cas")
df5.reset_index(drop=True, inplace=True)
df5.to_sql(name='csl', con=engine, if_exists='append', index=False)



