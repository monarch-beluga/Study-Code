# -*- coding: utf-8 -*-
# @Time    : 2025/2/9 上午8:24
# @Author  : Monarch
# @File    : 安义数据处理.py
# @Software: PyCharm

import os
import geopandas as gpd
import pandas
import pandas as pd
from glob import glob

os.chdir(r"D:\Work\安义数据采集\安义数据采集\安义化工集中区VR数据采集")


def shpToJson(in_file, out_file):
    gdf = gpd.read_file(in_file)
    gdf = gdf.to_crs(epsg=4326)
    gdf.to_file(out_file, driver="GeoJSON")


def yjkjExcelToJson(in_file, out_file):
    df = pd.read_excel(in_file)
    ds = {
        "name": "应急空间名称*",
        "firmName": "企业名称",
        "类型": "类型",
        "preLevel": "防控级别",
        "mainFuncName": "功能",
        "lng": "经度",
        "lat": "纬度",
        "范围数据（管道等提供）": "范围数据（管道等提供）",
        "可用容量(立方米)（应急池）": "可用容量(立方米)（应急池）",
        "备注": "备注",
    }

    df1 = pd.DataFrame()

    for i in ds:
        df1[i] = df[ds[i]]
    df1["type"] = df["类型"]
    df1["范围数据（管道等提供）"] = ""
    df1["备注"] = ""
    df1.loc[df1["type"].str[-1] == "池", "type"] = "1"
    df1.loc[df1["type"] == "水库", "type"] = "5"
    df1.loc[df1["type"] == "坑塘", "type"] = "6"
    df1.loc[df1["type"].str[-1] == "渠", "type"] = "7"
    df1.loc[df1["type"] == "桥梁", "type"] = "8"
    df1.loc[df1["type"] == "湿地", "type"] = "9"
    df1.loc[df1["type"] == "洼地", "type"] = "10"
    df1.loc[df1["type"] == "闸坝", "type"] = "11"
    df1.loc[df1["type"] == "泵站", "type"] = "2"
    df1.loc[df1["preLevel"] == "一级防控", "preLevel"] = "1"
    df1.loc[df1["preLevel"] == "二级防控", "preLevel"] = "2"
    df1.loc[df1["preLevel"] == "三级防控", "preLevel"] = "3"

    df1.to_json(out_file, indent=2, orient='records', force_ascii=False)


def qyfbExcelToJson(in_file, out_file):
    in_file = "安义工业园区-企业信息导入模板.xls"
    out_file = "anyi_qyfb.json"
    df = pd.read_excel(in_file)
    df1 = df.iloc[:, :-1]
    df1.columns = ["name", "lng", "lat", "地址", "行业类别", "应急联络人", "应急联络人电话", "主要产品", "企业范围数据（空间数据）", "企业简介", "企业图片（可以单独放，不用放表格中）"]
    df1[df1 == "/"] = ""
    df1[df1.isna()] = ""
    df1.to_json(out_file, indent=2, orient='records', force_ascii=False)


in_file = r"应急空间设施导入模板.xls"
df = pd.read_excel(in_file)
ds = {
    "id": "序号",
    "name": "应急空间名称*",
    "firmName": "企业名称",
    "类型": "类型",
    "preLevel": "防控级别",
    "mainFuncName": "功能",
    "lng": "经度",
    "lat": "纬度",
    "feature": "范围数据（管道等提供）",
    "capacity": "可用容量(立方米)（应急池）",
    "备注": "备注",
}

df1 = pd.DataFrame()

for i in ds:
    df1[i] = df[ds[i]]

df1["type"] = df["类型"]
df1["范围数据（管道等提供）"] = ""
df1["备注"] = ""
df1.loc[df1["type"] == "事故应急池", "type"] = 6
df1.loc[df1["type"] == "初期雨水池", "type"] = 7
df1.loc[df1["type"] == "污水处理站", "type"] = 8
df1.loc[df1["type"] == "坑塘", "type"] = 9
df1.loc[df1["type"] == "桥梁", "type"] = 13
df1.loc[df1["type"] == "闸坝", "type"] = 10
df1.loc[df1["type"] == "人工渠", "type"] = 11
df1.loc[df1["type"] == "水库", "type"] = 12
df1.loc[df1["type"] == "湿地", "type"] = 17
df1.loc[df1["type"] == "管道", "type"] = 18

ds1 = {
    "江远科技有限公司": "江西江远材料科技有限公司",
    "江远材料公司": "江西江远材料科技有限公司",
    "信达航科有限公司": "江西信达航科新材料科技有限公司",
    "晶安高科技有限公司": "江西晶安高科技股份有限公司",
    "金德锂有限公司": "江西金德锂新能源科技有限公司",
    "金德锂技有限公司": "江西金德锂新能源科技有限公司",
    "安德力有限公司": "江西安德力高新科技有限公司",
    "万华环保有限公司": "江西万华环保材料有限公司",
    "中迅农化有限公司": "江西中迅农化有限公司",
    "华晟化工有限公司": "江西华晟化工有限公司",
    "亚龙美氟有限公司": "江西亚龙美氟科技有限公司",
    "亚染科技有限公司": "江西省亚染科技有限公司",
    "园区": "园区",
    "园区污水处理厂": "园区污水处理厂",
    "东阳镇政府": "东阳镇政府",
    "万埠镇政府": "万埠镇政府"
}

df1["firmName"] = df1["firmName"].apply(lambda x: ds1[x])

df1.loc[df1["preLevel"] == "一级防控", "preLevel"] = "1"
df1.loc[df1["preLevel"] == "二级防控", "preLevel"] = "2"
df1.loc[df1["preLevel"] == "三级防控", "preLevel"] = "3"
df1.loc[df1["preLevel"] == "四级防控", "preLevel"] = "4"

df2 = pd.read_json("anyi_yjkj.json")
df3 = df2.loc[:90]
df1["feature"] = df3["feature"]
df1["facilityImg"] = df3["facilityImg"]

df1.to_json("anyi_yjkj1.json", indent=2, orient='records', force_ascii=False)

# os.chdir(r"D:\Work\安义数据采集\安义数据采集\安义化工集中区VR数据采集")

# in_file = r"安义化工集中区-救援队伍信息导入模板.xls"
# df = pd.read_excel(in_file)
#
# df1 = df.loc[df['类型'] == '园区', :]
# series1 = df1['组名称'].value_counts()
# df2 = pd.DataFrame({'type': series1.index, "num": series1.values})
# df2.to_json("anyi_yqjy_StatisticData.json", indent=2, orient='records', force_ascii=False)


# df1 = pd.read_excel("安义工业园区-企业信息导入模板.xls", index_col=0)
# df2 = pd.read_excel("安义化工集中区-企业风险源导入模板.xls", index_col=0)
#
# df = pd.concat([df1, df2], axis=1)
# df3 = df[['经度', '纬度', '合成材料制造', '风险源名称*', "环境风险等级"]]
# df4 = df3[df3['风险源名称*'] != "/"]
# df4.reset_index(inplace=True)
# columns = ['name', 'lon', 'lat', 'materialName', "riskSourcesName", "riskLevel"]
# df4.columns = columns
# df4.to_json("anyi_rs.json", indent=2, orient='records', force_ascii=False)
#
# series1 = df4['riskLevel'].value_counts()
# df5 = pd.DataFrame({'name': series1.index, "value": series1.values})
# df5.to_json("anyi_rs_StatisticData.json", indent=2, orient='records', force_ascii=False)




