# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 13:24
# @Author  : Monarch
# @File    : 02_zonal_statistics.py
# @Software: PyCharm

from rasterstats import zonal_stats
import os
import pandas as pd
import geopandas as gpd

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
out_path = "csv_data"
if not os.path.exists(out_path):
    os.mkdir(out_path)

lakes = ['太湖', '梁子湖', '洞庭湖', '洪泽湖', '鄱阳湖', "巢湖"]
data = pd.DataFrame()
data['lake_name'] = lakes
for lake in lakes:
    for year in range(1990, 2021, 5):
        shp_file = f"inter_lake/{lake}_{year}.shp"
        shp = gpd.read_file(shp_file)
        data[f'area_{year}'] = shp.area / 1000000
        shp_buff = shp.buffer(5000)

        for key in ['TAVG', 'PRCP', 'pop', 'gdp']:
            raster_file = f'{key}/{key}_{year}.tif'
            zonal_method = pd.DataFrame(zonal_stats(shp_buff, raster_file, stats='sum'))
            data[f'{key}_{year}'] = zonal_method['sum'] / (shp.buffer(5000).area / 1000000)

    data.to_csv(f'{out_path}/{lake}_zonal_statistics.csv', encoding='gbk')



