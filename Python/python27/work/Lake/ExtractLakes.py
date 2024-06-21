# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 10:02
# @Author  : Monarch
# @File    : ExtractLakes.py
# @Software: PyCharm


import arcpy
import os
from glob import glob

path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
arcpy.env.workspace = path
proj = arcpy.SpatialReference(3857)
arcpy.env.overwriteOutput = True

key = 'gdp'
for year in range(1995, 2021, 5):
    adf_file = "{0}/{0}{1}/{0}{1}".format(key, year)
    tif_file = "{0}/{0}_{1}.tif".format(key, year)
    pro_temp = arcpy.ProjectRaster_management(in_raster=adf_file,
                                              out_raster=tif_file,
                                              out_coor_system=proj,
                                              resampling_type='NEAREST',
                                              cell_size="1000")
