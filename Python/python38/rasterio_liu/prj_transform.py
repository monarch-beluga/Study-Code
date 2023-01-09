# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/1/9
@file:  prj_transform.py
"""

import rasterio
from rasterio.enums import Resampling
from rasterio.warp import calculate_default_transform, reproject
import numpy as np


def project_transform(in_raster, dst_crs, pixel_size=None, nodata=None, compress='lzw'):
    """

    Args:
        in_raster: 输入栅格文件路径
        dst_crs: 转换的投影
        pixel_size: 像元大小, 默认为None
        nodata: nodata无效值, 默认为-3.402823e+038
        compress: 压缩方式, 默认为 lzw


    Returns:
        dst_data: 转换投影后的栅格数据
        profile: 转换投影后的栅格数据源信息，用于栅格输出

    """
    if pixel_size:
        resolution = (pixel_size, pixel_size)
    else:
        resolution = None
    with rasterio.open(in_raster) as src:
        profile = src.profile
        src_crs = src.crs
        src_transform = src.transform
        src_nodata = profile['nodata']

        if not nodata:
            if src_nodata:
                nodata = src_nodata
            else:
                nodata = -3.402823e+038

        dst_transform, dst_width, dst_height = calculate_default_transform(
            src.crs,
            dst_crs,
            src.width,
            src.height,
            resolution=resolution,
            *src.bounds
        )
        profile.update({
            'nodata': nodata,
            'crs': dst_crs,
            'transform': dst_transform,
            'width': dst_width,
            'height': dst_height,
            'compress': compress
        })

        dst_data = np.empty((src.count, dst_height, dst_width), dtype=profile['dtype'])
        data = src.read()
        reproject(
            source=data,
            src_crs=src_crs,
            src_transform=src_transform,
            src_nodata=src_nodata,

            destination=dst_data,
            dst_transform=profile['transform'],
            dst_crs=dst_crs,
            dst_nodata=profile['nodata'],

            resampling=Resampling.average,
            num_threads=4
        )
    return dst_data, profile
