# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os
import time

out_path = r'E:\Data\paper'
os.chdir(out_path)
arcpy.env.workspace = out_path

shp_file = glob(r'data_shp\*.shp')

st = time.time()
for i in range(2, len(shp_file)):
    arcpy.FeatureToRaster_conversion(shp_file[i].decode('GBK'), 'TDLYME', 'data_tif/JX_%02d.tif' % (i+1), 10)
    print i+1, '消耗:', time.time()-st
print '转换成功！！！'

