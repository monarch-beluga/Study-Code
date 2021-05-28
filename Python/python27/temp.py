# -*- coding: utf-8 -*-

import arcpy

from arcpy import env

from arcpy.sa import *

# tif文件的存放位置
env.workspace = r"E:\Data\test\result"

# 点数据图层
inPointFeatures = r"E:\Data\test\zdjwd\zdjwd1t.shp"

inRasterList = arcpy.ListRasters()

arcpy.CheckOutExtension("Spatial")

ExtractMultiValuesToPoints(inPointFeatures, inRasterList, "NONE")
