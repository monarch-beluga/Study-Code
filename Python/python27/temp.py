# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os

path = r'H:\Monarch\Work\土壤碳'.decode('utf-8')
os.chdir(path)
arcpy.env.workspace = path

files = glob('polc*.tif')

for f_tif in files:
    out_file = f_tif.replace('tif', 'flt')
    arcpy.RasterToFloat_conversion(f_tif, out_file)

