# -*- coding: utf-8 -*-
# @Time    : 2025/12/9 下午6:05
# @Author  : Monarch
# @File    : 庐山老年人数据处理.py
# @Software: PyCharm

import pandas as pd
import geopandas as gpd
import numpy as np
from math import radians, cos, sqrt


class LatLonOffset:
    """
    经纬度偏移工具类
    """
    # 地球半径（米）
    EARTH_RADIUS = 6371000  # 平均地球半径

    @staticmethod
    def meters_to_degrees(lat, meters):
        """
        将米转换为纬度和经度方向的度数

        参数：
        lat: 纬度（用于计算经度转换）
        meters: 距离（米）

        返回：
        (delta_lat, delta_lon): 纬度和经度的变化量（度）
        """
        # 纬度变化：1度纬度 ≈ 111,111米（恒定）
        delta_lat = meters / 111111

        # 经度变化：1度经度 ≈ 111,111 * cos(lat) 米
        lat_rad = radians(lat)
        delta_lon = meters / (111111 * abs(cos(lat_rad)))

        return delta_lat, delta_lon

    @staticmethod
    def offset_point(lat, lon, distance_m, angle_deg):
        """
        根据距离和角度偏移一个点

        参数：
        lat, lon: 原始经纬度（度）
        distance_m: 偏移距离（米）
        angle_deg: 偏移角度（0=北，90=东，180=南，270=西）

        返回：
        (new_lat, new_lon): 偏移后的经纬度
        """
        # 将角度转换为弧度
        angle_rad = radians(angle_deg)

        # 计算纬度和经度的变化量
        delta_lat_m = distance_m * np.cos(angle_rad)
        delta_lon_m = distance_m * np.sin(angle_rad)

        # 转换为度数
        delta_lat = delta_lat_m / 111111

        lat_rad = radians(lat)
        delta_lon = delta_lon_m / (111111 * abs(cos(lat_rad)))

        new_lat = lat + delta_lat
        new_lon = lon + delta_lon

        return new_lat, new_lon

def offset_latlng_duplicates(df, lat_col='lat', lon_col='lon',
                             min_offset=100, max_offset=300, seed=None):
    """
    对重合的经纬度点进行随机偏移（100-300米）

    参数：
    df: 包含经纬度的DataFrame
    lat_col, lon_col: 纬度和经度列名
    min_offset, max_offset: 最小和最大偏移距离（米）
    seed: 随机种子
    """
    if seed is not None:
        np.random.seed(seed)

    df = df.copy()
    result_df = df.copy()

    # 创建精度为6位小数的坐标键（约0.1米精度）
    coord_key = df.apply(
        lambda row: f"{row[lat_col]:.6f},{row[lon_col]:.6f}",
        axis=1
    )

    # 统计坐标出现次数
    coord_counts = coord_key.value_counts()
    duplicate_coords = coord_counts[coord_counts > 1].index

    for coord_str in duplicate_coords:
        lat, lon = map(float, coord_str.split(','))

        # 找到所有具有这个坐标的行
        duplicate_indices = df[coord_key == coord_str].index

        for i, idx in enumerate(duplicate_indices):
            if i == 0:  # 第一个点保持不变
                continue

            # 随机距离和角度
            distance_m = np.random.uniform(min_offset, max_offset)
            angle_deg = np.random.uniform(0, 360)

            # 计算偏移后的经纬度
            new_lat, new_lon = LatLonOffset.offset_point(
                lat, lon, distance_m, angle_deg
            )

            result_df.at[idx, lat_col] = new_lat
            result_df.at[idx, lon_col] = new_lon

    return result_df

df = pd.read_excel(r"D:\Work\lushan\11月特困分散供养人数.xlsx", header=0, index_col=0)
df_offset = offset_latlng_duplicates(df, lat_col='X2', lon_col='X1',
                                    min_offset=800, max_offset=1500,
                                    seed=925)
df_offset.rename(columns={
    'X2': 'lat',
    'X1': 'lon',
    '人员属性（糖尿病、高血压病、慢阻肺病、重精、结核病、一般人群）': "人员属性",
    '包挂卫生院医务人员联系方式（姓名、电话）': '包挂卫生院医务人员联系方式',
    '乡村医生联系方式（姓名、电话）': '乡村医生联系方式'
    }, inplace=True)
df_offset[df_offset.isna()] = ""
df_offset.to_json(r"D:\Work\lushan\older_xx.json", indent=2, orient='records', force_ascii=False)




