# -*- coding: utf-8 -*-

import arcpy
from glob import glob
from arcpy.sa import *
import os
arcpy.CheckOutExtension("Spatial")

path = r'D:\MCD_dow'
os.chdir(path)
arcpy.env.workspace = path

mask_data = arcpy.Raster('TAVG_2018001.flt')
proj = r'TAVG_2018001.prj'
var = 'TMAX'
files = glob('{}/*.tif'.format(var))
extraction_area = "OUTSIDE"
analysis_extent = "elevation"

if not os.path.exists('{}_out'.format(var)):
    os.mkdir('{}_out'.format(var))

for f_tif in files:
    out_file = '{}_out/'.format(var) + os.path.basename(f_tif).replace('.tif', '.flt')
    # f_raster = arcpy.Raster(f_tif)
    outExtractByMask = ExtractByMask(f_tif, mask_data)
    # outExtractByMask.save('clip_temp.tif')
    pro_temp = arcpy.ProjectRaster_management(in_raster=outExtractByMask,
                                              out_raster='porj_temp.tif',
                                              out_coor_system=proj,
                                              resampling_type='NEAREST',
                                              cell_size="1000")
    arcpy.Delete_management(outExtractByMask)
    arcpy.RasterToFloat_conversion(pro_temp, out_file)
    arcpy.Delete_management(pro_temp)
    print f_tif, 'clip successful...'
    break



