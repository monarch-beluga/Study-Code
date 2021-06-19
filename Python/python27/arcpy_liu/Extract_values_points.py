# -*- coding: utf-8 -*-

import arcpy
from glob import glob
from arcpy import env
from arcpy.sa import *

# tif文件的存放位置
path = r'E:/Data/temp/tifdata/'

# 输出的位置
env.workspace = path

arcpy.CheckOutExtension("Spatial")

points = 'E:/Data/temp/points.shp'

files = glob(path + '*.tif')
List = [[i.split('\\')[-1]] for i in files]

ExtractMultiValuesToPoints(points, List, "NONE")




