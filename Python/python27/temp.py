# -*- coding: utf-8 -*-


import arcpy
from arcpy.sa import *
from glob import glob
import os

out_path = r'E:/Data/clip/reult/'
var = ['PRCP', 'TMIN', 'SSD', 'WIN', 'RHU', 'TMAX']
arcpy.env.workspace = out_path

roi = arcpy.FeatureSet(r'E:/Data/clip/JX.shp')

for v in var[:1]:
    files = glob(r'E:/Data/clip/{0}/reult/RES_*.grd'.format(v))
    if not os.path.exists(out_path + v):
        os.makedirs(out_path + v)
    for raster_f in files:
        clip_temp = arcpy.Clip_management(in_raster=raster_f, out_raster='clip_temp.tif', in_template_dataset=roi)
        re_temp = arcpy.Resample_management(in_raster=clip_temp, out_raster='re_temp.tif',
                                            cell_size=30, resampling_type="NEAREST")
        arcpy.Delete_management(clip_temp)
        out_file = raster_f.split('\\')[-1].replace('.grd', '.flt')
        arcpy.RasterToFloat_conversion(re_temp, out_path + v + os.sep + out_file)
        arcpy.Delete_management(re_temp)


