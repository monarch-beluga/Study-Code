# -*- coding: utf-8 -*-
# @Time    : 2024/6/20 18:40
# @Author  : Monarch
# @File    : 04_draw_lake_change.py
# @Software: PyCharm

import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
import geopandas as gpd
from matplotlib.gridspec import GridSpec

config = {
    "font.family": 'serif',
    "font.size": 12,
    "mathtext.fontset": 'stix',
    "font.serif": 'Simsun',
}
rcParams.update(config)

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
out_path = "png_data"
if not os.path.exists(out_path):
    os.mkdir(out_path)

lakes = ['太湖', '梁子湖', '洞庭湖', '洪泽湖', '鄱阳湖', "巢湖"]
# lakes = ["巢湖"]
for lake in lakes:
    fig = plt.figure(figsize=(15, 15))
    grid = GridSpec(3, 3)
    for year in range(1990, 2021, 5):
        i = ((year - 1990) // 5) // 3
        j = ((year - 1990) // 5) % 3
        shp_file = f'inter_lake/{lake}_{year}.shp'
        shp = gpd.read_file(shp_file)
        ax = fig.add_subplot(grid[i, j])
        shp.plot(ax=ax, color="#00BFFF", )
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.set_title(f"{year}年{lake}水域", fontsize=16)
        ax.axis('off')

    csv_file = f'csv_data/{lake}_statistic.csv'
    lake_data = pd.read_csv(csv_file, encoding='gbk', index_col=0)
    X = lake_data.index.values
    y = lake_data['area'].values
    ax = fig.add_subplot(grid[2, 1:3])
    ax.set_title("1995 - 2020年" + f"{lake}水域面积变化", weight="bold", size=16)
    ax.set_xlabel('时间 $\mathrm{(year)}$', size=12)
    ax.set_ylabel('面积 $\mathrm{(km^2)}$', size=12)
    ax.tick_params("both", direction='in')
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    ax.plot(X, y, 'c-o', markersize=5, linewidth=1, label=lake)
    lim = y.max() - y.min()
    plt.ylim([y.min() - lim / 2, y.max() + lim / 2])
    fig.savefig(f'{out_path}/{lake}_lake_change.png', dpi=600, bbox_inches='tight')


