# -*- coding: utf-8 -*-
# @Time    : 2025/3/1 下午8:40
# @Author  : Monarch
# @File    : 多边形检索poi.py
# @Software: PyCharm

import requests
import time
import pandas as pd
import geopandas as gpd


def geometry_to_string(geom):
    # 提取多边形的外环坐标
    coords = list(geom.exterior.coords)
    # 将坐标转换为字符串，并用 '|' 分割
    coord_str = '|'.join([f"{x},{y}" for x, y in coords])
    return coord_str


shp_file = r"D:\Work\get_poi\roi.shp"
gdf = gpd.read_file(shp_file)
gdf['geometry_str'] = gdf['geometry'].apply(geometry_to_string)
region = gdf['geometry_str'][0]

types = '140000'

key_file = r'D:\System\高德地图Key\Key.txt'
with open(key_file) as fp:
    key = fp.readline()

# 每页最多25条记录
page_size = 25
page_num = 1
pois = []
out_file = f'D:/Work/get_poi/roi_{types}.csv'
u = "https://restapi.amap.com/v5/place/polygon?polygon={0}&types={1}&key={2}&page_size={3}&page_num={4}"
for page_num in range(1, 101):
    url = u.format(region, types, key, page_size, page_num)
    response = requests.get(url)
    data = response.json()
    pois += data['pois']
    count = data['count']
    time.sleep(0.5)
    print(page_num, ":", count)
    if count != 25:
        break
df = pd.DataFrame(pois)
df.to_csv(out_file, index=False)


