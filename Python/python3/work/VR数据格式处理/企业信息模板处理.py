# -*- coding: utf-8 -*-
# @Time    : 2025/8/24 下午12:32
# @Author  : Monarch
# @File    : 企业信息模板处理.py
# @Software: PyCharm

import os
import pandas as pd
import numpy as np

os.chdir(r"D:\Work\pxvr\湘东工业园区VR数据表格-25.9.12")

in_file = r"02-企业信息导入模板.xls"
out_file = r'qyfb.json'

df = pd.read_excel(in_file)
ds = {
    "name": "企业名称",
    "lng": '经度',
    "lat": '纬度',
    "地址": "地址",
    "行业类别": "合成材料制造",
    "应急联络人": "应急联络人",
    "应急联络人电话": '应急联络人电话',
    "主要产品": "主要产品",
    "feature": "企业范围数据（空间数据）",
    "企业简介": "企业简介",
    "企业图片（可以单独放，不用放表格中）": "企业图片（可以单独放，不用放表格中）",
    "备注": '备注'
}
df1 = pd.DataFrame()

for i in ds:
    df1[i] = df[ds[i]]

df1[df1 == "/"] = ""
df1[df1.isna()] = ""
# df1.to_json(out_file, indent=2, orient='records', force_ascii=False)



