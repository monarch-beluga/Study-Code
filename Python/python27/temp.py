# -*- coding: utf-8 -*-

import arcpy
from glob import glob
import os
import time

out = r'F:/sjy/'
work_path = r'E:/public/sjy/'
os.chdir(work_path)
arcpy.env.workspace = work_path
paths = glob('*/result')
roi = arcpy.Raster(r'E:\Data\temp\SRTM_Sanjy_250m.grd')
i = 0
st = time.time()
for path in paths[1:]:
    out_path = out + path.split('\\')[0]
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    files = glob(path + '/*.grd')
    s = len(files)*len(paths[1:])
    for raster_f in files:
        clip_temp = arcpy.Clip_management(in_raster=raster_f, out_raster='temp.tif',
                                          in_template_dataset=roi, maintain_clipping_extent='MAINTAIN_EXTENT')
        out_file = out_path + os.sep + raster_f.split('\\')[-1].replace('grd', 'flt')
        arcpy.RasterToFloat_conversion(clip_temp, out_file)
        arcpy.Delete_management(clip_temp)
        i += 1
        p = time.time() - st
        t = p / i * s - p
        print '进度: {0}/{1}, 耗时:{2:.2f}s, 还需:{3:.2f}s'.format(i, s, p, t)




