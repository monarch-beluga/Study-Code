# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:25:01 2020

@author: whis
"""
import os,rasterio
import numpy as np
# import numpy as np
fpath = r'E:/study/资料/数据/IM'


for year in range(1980, 2018+1):
    prcp = r'E:/study/资料/数据/prcp_year' + os.sep + 'PRCP' + str(year) + 'SUM.tif'
    Et = r'E:/study/资料/数据/Qinghai0425' + os.sep + 'ET' + str(year) + '.flt'
    with rasterio.open(prcp) as p:
        dat_p = p.read()
        meta = p.meta
        # p.shape
        print('a')
    with rasterio.open(Et) as e:
        dat_e = e.read().reshape(1, 902, 1219)
        # meta =e.meta
        
        print('b')
    # # Im = 100*(np.divide(p,e)-1)
    meta.update(dtype=rasterio.float32)
    i = 100*((np.true_divide(dat_p, dat_e)) - 1)
    np.where(i> 9999, -9999, i)
    print(i)
    # IM = 100*(i - 1)
    #  ImOunt = fpath + os.sep + 'IM' + str(year) + '.tif'
    with rasterio.open(fpath + os.sep + 'IM' + str(year) + '.flt', 'w', **meta) as IMout:
         IMout.write(i.astype(rasterio.float32))
    # IM.save(fpath + os.sep + 'IM' + str(year) + '.tif')
print('over')