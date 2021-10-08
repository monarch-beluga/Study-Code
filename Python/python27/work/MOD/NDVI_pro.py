# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/28
@file: NDVI_pro.py
@function:
@modify:
"""

import arcpy
from glob import glob
import os
import time

out_path = r'E:/Data/NDVI_JX/'
os.chdir(out_path)
arcpy.env.workspace = out_path

roi = arcpy.FeatureSet(r'E:/Data/clip/JX.shp')
st = time.time()
i = 1
files = glob(r'*.tif')
s = len(files)
v = 'reult/'
proj = r'E:/Data/clip/WGS_1984_Albers.prj'
if not os.path.exists(v):
    os.makedirs(v)
for raster_f in files[1:]:
    pro_temp = arcpy.ProjectRaster_management(in_raster=raster_f,
                                              out_raster='porj_temp.tif',
                                              out_coor_system=proj,
                                              resampling_type='NEAREST',
                                              cell_size="30")
    clip_temp = arcpy.Clip_management(in_raster=pro_temp, out_raster='clip_temp.tif',
                                      in_template_dataset=roi)
    arcpy.Delete_management(pro_temp)
    out_file = v + raster_f.replace('tif', 'flt')
    arcpy.RasterToFloat_conversion(clip_temp, out_file)
    arcpy.Delete_management(clip_temp)
    i += 1
    p = time.time() - st
    t = p / i * s - p
    print '进度: {0}/{1}, 耗时:{2:.2f}s, 还需:{3:.2f}s'.format(i, s, p, t)


