# -*- coding: utf-8 -*-
# @Time    : 2025/5/23 上午12:41
# @Author  : Monarch
# @File    : PCB行业化学品信息.py
# @Software: PyCharm

import pandas as pd
from sqlalchemy import create_engine
import os

os.chdir(r"D:\Work\PCB行业化学品")

engine = create_engine('mysql+pymysql://root:123456@47.122.26.141:3306/esocs')

df = pd.read_excel("2025年调查PCB行业企业填报数据分析（发群）.xlsx", sheet_name="160家企业填报数据")

df1 = pd.DataFrame()
ds = {
    'city': '设区市',
    'firmName': '单位名称',
    'productName': '产品名称',
    'useLink': '使用环节/部门',
    'name': 'MSDS名称',
    'cas': 'CAS号',
    'concentration': '调整后浓度/含量',
    'usage': '2024年使用量（，KG折纯）',
    'usageNet': '2024年使用量（折算）',
    'unit': '单位 L/KG',
    'type': '所属调查物质分类',
}

for i in ds:
    df1[i] = df[ds[i]]

df1['concentration'] = df1['concentration'].astype(float)
df1['usage'] = df1['usage'].astype(float)
df1['usageNet'] = df1['usage'] * df1['concentration']
df1['unit'] = df1['unit'].str.upper()

df1.to_sql(name='esocs', con=engine, if_exists='append', index=False)

