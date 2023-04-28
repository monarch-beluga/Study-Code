# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 16:37
# @Author  : Monarch
# @File    : get_class.shp.py
# @Software: PyCharm

import os
import geopandas as gpd

os.chdir(r'D:\Data\parper\data\datasets')

file = 'jx_landuse.shp'
gdf = gpd.read_file(file)
for i in range(6):
    out_file = file.replace(".shp", f"_{i+1}.shp")
    gdf_type = gdf[gdf['gridcode'] == i+1]
    gdf_type.to_file(out_file)
    print(i)


