# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os

path = r'D:\Data\parper\data\datasets'
os.chdir(path)
arcpy.env.workspace = path

files = glob('jx*.shp')
for shp in files:
    point_file = 'point_' + shp
    arcpy.CreateRandomPoints_management(path, point_file, shp, "", 1)



