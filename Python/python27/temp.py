# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os
import time

out_path = r'H:\Monarch\paper\Data\landuse'
os.chdir(out_path)
arcpy.env.workspace = out_path

shp_file = glob(r'G:\arcgis1\package\jx_landuse\commondata\datasets\*.shp')

st = time.time()
for i, shp_f in enumerate(shp_file[:1]):
    arcpy.FeatureToRaster_conversion(shp_f, 'TDLYDM', 'JX_%02d.tif' % (i+1), 10)
    print i+1, '消耗:', time.time()-st
print '转换成功！！！'

