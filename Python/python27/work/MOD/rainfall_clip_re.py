# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/29
@file: rainfall_clip_re.py
@function:
@modify:
"""

import arcpy
from glob import glob
import os
import time

out_path = r'F:/rain_and_wind/'
os.chdir(out_path)
var = ['rainfall_factor', 'wind_factor']
arcpy.env.workspace = out_path
arcpy.env.parallelProcessingFactor = 0

roi = arcpy.FeatureSet(r'E:/Data/clip/JX.shp')

st = time.time()
i = 0
for v in var[:1]:
    files = glob(v + os.sep + r'*.flt')
    s = len(files) * 2
    if not os.path.exists(v+'_clip'):
        os.makedirs(v+'_clip')
    for raster_f in files[:1]:
        clip_temp = arcpy.Clip_management(in_raster=raster_f, out_raster='clip_temp.tif',
                                          in_template_dataset=roi)
        re_temp = arcpy.Resample_management(in_raster=clip_temp, out_raster='re_temp.tif',
                                            cell_size=30, resampling_type="NEAREST")
        arcpy.Delete_management(clip_temp)
        clip_temp1 = arcpy.Clip_management(in_raster=re_temp, out_raster='clip_temp.tif',
                                           in_template_dataset=roi)
        arcpy.Delete_management(re_temp)
        out_file = raster_f.replace(v, v+'_clip')
        arcpy.RasterToFloat_conversion(clip_temp1, out_file)
        arcpy.Delete_management(clip_temp1)
        p = time.time() - st
        t = p / (i + 1) * s - p
        print '进度: {0}/{1}, 耗时:{2:.2f}s, 还需:{3:.2f}s'.format(i + 1, s, p, t)
        i += 1


