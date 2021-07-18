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
from arcpy.sa import *
from glob import glob
import time
import sys
import os

var = ['PRCP', 'TMIN', 'SSD', 'WIN', 'RHU', 'TMAX']
path = r'F:/sjy/'
out_path = r'F:/sjy_clip/'
arcpy.env.workspace = out_path
arcpy.env.parallelProcessingFactor = 0

roi = Raster(r'SRTM_Sanjy_250m.grd')
for v in var:
    raster_files = glob(path+'{0}/*.grd'.format(v))
    if not os.path.exists(out_path + v):
        os.makedirs(out_path + v)
    for raster_file in raster_files:
        temp = arcpy.Clip_management(in_raster=raster_file, out_raster='temp.tif', in_template_dataset=roi)
        out_file = raster_file.split('\\')[-1].replace('.grd', '.flt')
        arcpy.RasterToFloat_conversion(temp, out_path + v + os.sep + out_file)
        arcpy.Delete_management(temp)
        sys.stdout.write('\r{0}裁剪成功'.format(out_file))
        break
    break
