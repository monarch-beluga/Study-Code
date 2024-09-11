# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import rasterio
import numpy as np
import pandas as pd

cut_fill_file = r"D:\Work\Problem\CutFill.tif"
out_file = os.path.splitext(cut_fill_file)[0] + '.csv'

with rasterio.open(cut_fill_file) as src:
    profile = src.profile
    data = src.read(1)

scale = profile['transform'][0]
data[data == profile['nodata']] = np.nan
cut_count = data[data < 0].shape[0]
fill_count = data[data > 0].shape[0]
zero_count = data[data == 0].shape[0]

cut_area = cut_count * scale * scale
fill_area = fill_count * scale * scale
zero_area = zero_count * scale * scale

cut_v = -(data[data < 0] * scale * scale).sum()
fill_v = (data[data > 0] * scale * scale).sum()

df = pd.DataFrame({
    "类型": ["不变", "挖方", "填方"],
    "像元数": [zero_count, cut_count, fill_count],
    "面积(平方米)": [zero_area, cut_area, fill_area],
    "体积(立方米)": [0, cut_v, fill_v]
})
df.to_csv(out_file, sep=',', index=False)
