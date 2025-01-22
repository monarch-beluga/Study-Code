# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import geopandas as gpd
import pandas as pd
from glob import glob

os.chdir(r"D:\Work\安义数据采集")


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

img_files = sorted(glob("facilityImage/*"), key=lambda name: int(name.split("\\")[1].split('.')[0]))
df1['facilityImg'] = img_files
df1.to_json("anyi_yjkj.json", indent=2, orient='records', force_ascii=False)


