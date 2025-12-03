# -*- coding: utf-8 -*-
# @Time    : 2025/8/24 下午2:48
# @Author  : Monarch
# @File    : 园区救援队伍模板处理.py
# @Software: PyCharm

import os
import pandas as pd

os.chdir(r"D:\Work\pxvr\湘东工业园区VR数据表格-25.9.12")

in_file = r'05-救援队伍信息导入模板.xls'
out_file = r'yqjy.json'

df = pd.read_excel(in_file)
df1 = df[df['类型'] == '园区']

ds = {
    "rescueTeamName": "组名称",
    "rescueTeamDuties": "组职务",
    "parkPositions": "负责人",
    "responsiblePersonName": "职务",
    "contactNumber": '负责人电话'
}

df2 = pd.DataFrame()

for i in ds:
    df2[i] = df1[ds[i]]

df2[df2 == "/"] = ""
df2.to_json(out_file, indent=2, orient='records', force_ascii=False)

series1 = df2['rescueTeamName'].value_counts()
df3 = pd.DataFrame({'type': series1.index, "num": series1.values})
df3.to_json("yqjy_StatisticData.json", indent=2, orient='records', force_ascii=False)



