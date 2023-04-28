# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 16:26
# @Author  : Monarch
# @File    : mosaic_tif.py
# @Software: PyCharm

import arcpy
from glob import glob
import os

path = r"D:/Data/parper/landuse_tif/"
arcpy.env.workspace = path
outpath = r"D:/Data/parper/landuse_tif/"
os.chdir(path)

files = glob('*.tif')
out_file = 'jx_landuse.tif'
arcpy.MosaicToNewRaster_management(files, path, out_file)


