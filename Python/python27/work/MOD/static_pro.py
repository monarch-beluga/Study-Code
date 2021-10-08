# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/30
@file: static_pro.py
@function:
@modify:
"""

import os
from glob import glob
import arcpy
import time

path = r'F:/静态数据/'.decode('utf-8')
os.chdir(path)
files = glob('*/*.flt') + glob('*/*.bil') + glob('*/*.pix')
roi = arcpy.FeatureSet(r'E:/Data/clip/JX.shp')
roi1 = arcpy.FeatureSet(r'E:/Data/clip/roi_prj.shp')
arcpy.env.workspace = path
proj = r'E:/Data/clip/WGS_1984_Albers.prj'

st = time.time()
i = 0
s = len(files)
for raster_f in files:
    raster = arcpy.Raster(raster_f)
    clip_temp = arcpy.Clip_management(in_raster=raster, out_raster='clip_temp.tif',
                                      in_template_dataset=roi1)
    re_temp = arcpy.arcpy.ProjectRaster_management(in_raster=clip_temp,
                                                   out_raster='porj_temp.tif',
                                                   out_coor_system=proj,
                                                   resampling_type='NEAREST',
                                                   cell_size="30")
    arcpy.Delete_management(clip_temp)
    clip_temp1 = arcpy.Clip_management(in_raster=re_temp, out_raster='clip_temp.tif',
                                       in_template_dataset=roi)
    arcpy.Delete_management(re_temp)
    out_file = raster_f.split('.')[0] + '_cilp.flt'
    arcpy.RasterToFloat_conversion(clip_temp1, out_file)
    arcpy.Delete_management(clip_temp1)
    arcpy.Delete_management(raster)
    p = time.time() - st
    t = p / (i + 1) * s - p
    print '进度: {0}/{1}, 耗时:{2:.2f}s, 还需:{3:.2f}s'.format(i + 1, s, p, t)
    i += 1

