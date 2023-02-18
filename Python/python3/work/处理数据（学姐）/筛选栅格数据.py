
import os
import shutil

path = r'E:/temp/LST-NDVI/MOD11A2/'
path2 = r'E:/temp/LST-NDVI/MOD13A2/'
outpath1 = r'E:/temp/LST-NDVI/MOD11-select/'
outpath2 = r'E:/temp/LST-NDVI/MOD13-select/'
file = os.listdir(path)
File = os.listdir(path2)
selects = [['_03_', '_04_'], ['_05_', '_06_'], ['_07_', '_08_', '_09_']]
for i in file:
    for select in selects:
        k = [j.strip('_') for j in select]
        k = '_'.join(k)
        out = outpath1 + k + '/'
        if not os.path.exists(out):
            os.makedirs(out)
        for j in select:
            if j in i:
                shutil.copy(path + i, outpath1 + k + '/' + i)
for i in File:
    for select in selects:
        k = [j.strip('_') for j in select]
        k = '_'.join(k)
        out = outpath2 + k + '/'
        if not os.path.exists(out):
            os.makedirs(out)
        for j in select:
            if j in i:
                shutil.copy(path2 + i, outpath2 + k + '/' + i)
