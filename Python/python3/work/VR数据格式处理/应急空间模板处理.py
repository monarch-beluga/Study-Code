# -*- coding: utf-8 -*-
# @Time    : 2025/8/25 下午10:41
# @Author  : Monarch
# @File    : 应急空间模板处理.py
# @Software: PyCharm

import os
import pandas as pd
from glob import glob

os.chdir(r"D:\Work\pxvr")

in_file = r'应急空间设施导入模板.xlsx'
out_file = r'yjkj.json'

images = glob("facilityImage/*")
images_id = [int(os.path.basename(i).split('.')[0]) for i in images]
df = pd.read_excel(in_file)
ds = {
    "id": "序号",
    "name": "应急空间名称",
    "firmName": "企业名称",
    "类型": "类型",
    "preLevel": "防控级别",
    "mainFuncName": "功能",
    "lng": "经度",
    "lat": "纬度",
    "capacity": "容量(立方米)",
    '备注': "备注"
}
df1 = pd.DataFrame()

for i in ds:
    df1[i] = df[ds[i]]
df1['feature'] = None

df1['type'] = df1['类型']
df1.loc[df1["type"] == "事故应急池", "type"] = 6
df1.loc[df1["type"] == "初期雨水收集池", "type"] = 7
df1.loc[df1["type"] == "临时筑坝点", "type"] = 8
df1.loc[df1["type"] == "坑塘", "type"] = 9
df1.loc[df1["type"] == "闸坝", "type"] = 10
df1.loc[df1["type"] == "湿地", "type"] = 11
df1.loc[df1["type"] == "桥梁", "type"] = 12
df1.loc[df1['type'] == '管道', "type"] = 13

df1.loc[df1["preLevel"] == "一级", "preLevel"] = "1"
df1.loc[df1["preLevel"] == "二级", "preLevel"] = "2"
df1.loc[df1["preLevel"] == "三级", "preLevel"] = "3"
df1.loc[df1["preLevel"] == "四级", "preLevel"] = "4"

df2 = pd.DataFrame({'image': images}, index=images_id)
df1.set_index('id', inplace=True)
df1['facilityImage'] = df2['image']
df1.reset_index(inplace=True)

df1.to_json(out_file, indent=2, orient='records', force_ascii=False)

series1 = df1['类型'].value_counts()
df2 = pd.DataFrame({'name': series1.index, "value": series1.values})
df2.to_json("yjkj_StatisticData.json", indent=2, orient='records', force_ascii=False)


