
import os
import shutil


path = r'E:/work/孟印缅/MYD11A2/'
# path2 = r'E:/work/孟印缅/MOD13A2/'
outpath1 = r'E:/work/孟印缅/MYD11-select/'
# outpath2 = r'E:/work/孟印缅/MOD13-select/'
file = os.listdir(path)
# File = os.listdir(path2)
# selects2 = [['_03_', '_04_'], ['_05_', '_06_'], ['_07_', '_08_', '_09_']]
selects1 = ['_03_', '_04_', '_05_', '_06_', '_07_', '_08_', '_09_']
for i in file:
    for select in selects1:
        # k = [j.strip('_') for j in select]
        # k = '_'.join(k)
        out = outpath1 + select + '/'
        if not os.path.exists(out):
            os.makedirs(out)
        if select in i:
            shutil.copy(path + i, out + i)
# for i in File:
#     for select in selects2:
#         k = [j.strip('_') for j in select]
#         k = '_'.join(k)
#         out = outpath2 + k + '/'
#         if not os.path.exists(out):
#             os.makedirs(out)
#         for j in select:
#             if j in i:
#                 shutil.copy(path2 + i, out + i)
