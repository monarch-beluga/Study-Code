# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import geopandas as gpd
import pandas as pd
from glob import glob


def polygon_to_coords_str(polygon):
    # 获取外环坐标
    return ";".join([f"{x},{y},120" for x, y, z in polygon.exterior.coords])


os.chdir(r"D:\Work\安义数据采集\企业")

gdf = gpd.read_file("化工集中区企业分布_shape_pro.shp")

gdf["feature"] = gdf.geometry.apply(polygon_to_coords_str)

gdf["area"] = gdf.geometry.area

df = gdf[["feature", "area", "O_Name"]]
df["area"] /= 10000

df.to_json("anyi_qyfw.json", double_precision=6, indent=2, orient='records', force_ascii=False)

