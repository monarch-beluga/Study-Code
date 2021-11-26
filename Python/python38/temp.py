# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

import rasterio

with rasterio.open(r'E:\public\数据\reult\dem.txt') as src:
    profile = src.profile
    data = src.read(1)




