# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os
arcpy.CheckOutExtension("Spatial")

path = r'H:\Monarch\Work\clip'
os.chdir(path)
arcpy.env.workspace = path

shp = arcpy.FeatureSet('shp/polygon_JX.shp')
var = 'TMAX'
files = glob('{}/*.flt'.format(var))

if not os.path.exists('{}_out'.format(var)):
    os.mkdir('{}_out'.format(var))

for f_tif in files:
    out_file = '{}_out/'.format(var) + os.path.basename(f_tif)
    clip_temp = arcpy.Clip_management(in_raster=f_tif, out_raster='clip_temp.tif',
                                      in_template_dataset=shp, nodata_value=-9999)
    clip_r = arcpy.Raster(clip_temp) / 10
    arcpy.RasterToFloat_conversion(clip_r, out_file)
    arcpy.Delete_management(clip_temp)
    print f_tif, 'clip successful...'



