# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os
import time

path = r'H:\Monarch\paper\Data\landuse\class'
os.chdir(path)
arcpy.env.workspace = path
out_path = 'points'

shp_files = glob("*.shp")
for f in shp_files:
    arcpy.CreateRandomPoints_management(out_path, 'p_'+f.decode('gbk'), f.decode('gbk'), "", 10, 20)
    print 'p_'+f.decode('gbk')+'export success !!!'

