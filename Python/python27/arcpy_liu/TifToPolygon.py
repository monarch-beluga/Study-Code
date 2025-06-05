# -*- coding: utf-8 -*-
# @Time    : 2025/6/1 上午10:31
# @Author  : Monarch
# @File    : TifToPolygon.py
# @Software: PyCharm

import os
import arcpy
from arcpy import env
from glob import glob

os.chdir(r"D:\Work\lsg\dom")
env.workspace = r"D:\Work\lsg\dom"

files = glob("snic/*.tif")

for inRaster in files:
    outPolygons = "snic_shp/" + os.path.basename(inRaster).split(".")[0] + ".shp"
    field = "VALUE"
    arcpy.RasterToPolygon_conversion(inRaster, outPolygons, "NO_SIMPLIFY", field)
