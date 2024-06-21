# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 13:24
# @Author  : Monarch
# @File    : 01_get_main_lake.py
# @Software: PyCharm

import geopandas as gpd
import pandas as pd
import os
from glob import glob

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
out_path = "inter_lake"
if not os.path.exists(out_path):
    os.mkdir(out_path)

lakes = ['太湖', '梁子湖', '洞庭湖', '洪泽湖', '鄱阳湖', "巢湖"]

for year in range(1990, 2021, 5):
    inter_lakes = []
    for lake in lakes:
        lake_shp = glob(f"Lake/*{year}*/*.shp")[0]
        main_lake = f"MainLake/{lake}.shp"
        lake_gdf = gpd.read_file(lake_shp).to_crs('epsg:3857').explode(index_parts=False)
        m_lake_gdf = gpd.read_file(main_lake).to_crs('epsg:3857').buffer(500)
        inter_lake = lake_gdf[lake_gdf.intersects(m_lake_gdf.unary_union)]
        inter_lake = inter_lake.buffer(500)
        inter_lake = lake_gdf[lake_gdf.intersects(inter_lake.unary_union)].dissolve()
        inter_lake.to_file(f'inter_lake/{lake}_{year}.shp')
        inter_lakes.append(inter_lake)
    inter_lakes = gpd.GeoDataFrame(pd.concat(inter_lakes))
    inter_lakes['lake_name'] = lakes
    inter_lakes = inter_lakes[['lake_name', 'geometry']]
    inter_lakes.to_file(f"{out_path}/main_lakes_{year}.shp", encoding='utf-8')


