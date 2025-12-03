# -*- coding: utf-8 -*-
# @Time    : 2025/8/24 下午3:28
# @Author  : Monarch
# @File    : 企业救援队伍模板处理.py
# @Software: PyCharm

import os
import pandas as pd

os.chdir(r"D:\Work\pxvr\湘东工业园区VR数据表格-25.9.12")

in_file = r'05-救援队伍信息导入模板.xls'
out_file = r'qyjy.json'

df = pd.read_excel(in_file)
df1 = df[df['类型'] == '企业']

ds = {
    "firmName": "企业名称",
    "responsiblePersonName": "负责人",
    "contactNumber": '负责人电话',
    "responsiblePersonName2": "负责人2",
    "contactNumber2": "负责人电话2"
}

df2 = pd.DataFrame()

for i in ds:
    df2[i] = df1[ds[i]]

df2[df2 == "/"] = ""
df2.to_json(out_file, indent=2, orient='records', force_ascii=False)


