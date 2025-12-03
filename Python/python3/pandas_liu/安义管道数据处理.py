# -*- coding: utf-8 -*-
# @Time    : 2025/5/3 上午10:25
# @Author  : Monarch
# @File    : 安义管道数据处理.py
# @Software: PyCharm

import os
import geopandas as gpd
import pandas as pd
from glob import glob

os.chdir(r"D:\Work\安义数据采集\安义数据采集\安义化工集中区VR数据采集")

def line_to_coords_string(line):
    return ";".join([f"{x},{y},40" for x, y, z in line.coords])


def polygon_to_coords_str(polygon):
    # 获取外环坐标
    return ";".join([f"{x},{y},120" for x, y, z in polygon.exterior.coords])

gdf = gpd.read_file(r"D:\Work\安义数据采集\安义数据采集\雨水矢量\园区雨水管_track.shp")

gdf['coords_str'] = gdf['geometry'].apply(line_to_coords_string)

gdf1 = pd.DataFrame()
gdf1["name"] = gdf["O_Name"]
gdf1["firmName"] = "园区"
gdf1["类型"] = "管道"
gdf1["preLevel"] = "3"
gdf1["mainFuncName"] = "转输"
gdf1["lng"] = "\\"
gdf1["lat"] = "\\"
gdf1["feature"] = gdf['coords_str']
gdf1["capacity"] = "\\"
gdf1["备注"] = ""
gdf1["type"] = 13
gdf1["范围数据（管道等提供）"] = ""
gdf1["speed"] = 8
gdf1.to_json("anyi_sjgd1.json", indent=2, orient='records', force_ascii=False)


