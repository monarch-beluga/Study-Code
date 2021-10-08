# -*- coding: utf-8 -*-

import arcpy
from glob import glob
from arcpy import env

# tif文件的存放位置
path = r"E:/Data/Remote sensing/work/"

# tif输出的位置
out_path = r'E:/public/'
env.workspace = out_path

file = 'NDVI01-a.tif'
out_file = 'NDVI-proj.tif'
proj = 'WGS_1984_UTM_Zone_50N.prj'
# files = glob(path+'*.tif')
#
# for file in files:
arcpy.ProjectRaster_management(in_raster=file, out_raster=out_file,
                               out_coor_system=proj, resampling_type='NEAREST',
                               cell_size="250")

