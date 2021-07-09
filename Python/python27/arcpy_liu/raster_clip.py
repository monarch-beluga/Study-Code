# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/08
@file: raster_clip.py
@function:
@modify:
"""

import arcpy
from glob import glob
import os

arcpy.env.workspace = r'E:\Data\shuju_clip'
raster_files = glob(r'E:\Data\suju\*tif')
roi = r'E:\Data\roi\CRX_prj.shp'

for raster_file in raster_files:
    arcpy.Clip_management(in_raster=raster_file,
                          out_raster=raster_file.split('\\')[-1],
                          in_template_dataset=roi,
                          clipping_geometry=True)
    print raster_file.split('\\')[-1]+'裁剪成功'
