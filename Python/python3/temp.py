# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import geopandas as gpd
import os
import pandas as pd


def polygon_to_coords_str(polygon):
    # 获取外环坐标
    return ";".join([f"{x},{y}" for x, y in polygon.exterior.coords])


os.chdir(r"D:\Work\lushan\庐山总矢量数据")

ls_xz_poly = gpd.read_file("庐山市乡镇_天地图_s1.shp")
exploded_gdf = ls_xz_poly.explode(index_parts=False).reset_index(drop=True)
# exploded_gdf.to_file("3庐山村镇.shp")
exploded_gdf["feature"] = exploded_gdf['geometry'].apply(polygon_to_coords_str)
df = exploded_gdf[["NAME", "feature"]]
df.columns = ["NAME", "feature"]
df.to_json("lushan_xz_fw.json", indent=2, orient='records', force_ascii=False)
# ls_xz_point = gpd.read_file("庐山镇驻地.shp")
# df = ls_xz_point[["NAME", "lon", "lat"]]
# df.to_json("lushan_xz_p.json", indent=2, orient='records', force_ascii=False)




