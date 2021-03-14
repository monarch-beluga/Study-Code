
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from glob2 import glob

ds1 = gdal.Open(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\PRCP\PRCP_std_80-18\PRCP_std_80-18.tif')
mask = ds1.ReadAsArray()
mask[mask == mask[0][0]] = np.nan


class para1(object):
    Folder_path = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/IM/'
    File_extension = '.flt'
    ini_year = 1980
    end_year = 2018


path = para1.Folder_path
for year in range(para1.ini_year, para1.end_year + 1):
    file = glob(path + '*' + str(year) + '*' + para1.File_extension)
    ds = gdal.Open(file[0])
    temp = ds.ReadAsArray()
    temp[np.isnan(mask)] = np.nan
    if year == para1.ini_year:
        im_width = ds.RasterXSize
        im_height = ds.RasterYSize
        data2 = np.full((im_height, im_width), 0.0)
    data2 += temp
data2 = data2[~np.isnan(data2)]
data2 = data2 / (para1.end_year + 1 - para1.ini_year)
data = np.array(['arid', 'semiarid', 'dry subhumid', 'moist subhumid', 'humid1',
                 'humid2', 'humid3', 'humid4', 'perhumid'])
data1 = np.array([len(data2[(data2 <= -66.7) & (data2 >= -100)]),
                  len(data2[(data2 > -66.7) & (data2 <= -33.3)]),
                  len(data2[(data2 <= 0) & (data2 > -33.3)]),
                  len(data2[(data2 > 0) & (data2 <= 20)]),
                  len(data2[(data2 > 20) & (data2 <= 40)]),
                  len(data2[(data2 > 40) & (data2 <= 60)]),
                  len(data2[(data2 > 60) & (data2 <= 80)]),
                  len(data2[(data2 > 80) & (data2 <= 100)]),
                  len(data2[data2 > 100]),
                  ])
data1 = data1 / len(data2[data2 >= -100]) * 100
a = np.where(data1 == 0)
data = np.delete(data, a)
data1 = np.delete(data1, a)


class para:
    bar_width = 0.6
    bar_align = 'center'
    ticks_font = 'Times New Roman'
    xtick_direction = 'out'
    ytick_direction = 'in'
    frames = ['right', 'top']
    ylabel = 'Area percent (%)'
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format('Area_IM')
    dpi = 300


fig, ax = plt.subplots(1, 1)
ax.set_xticklabels(data, rotation=-30, fontsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontname(para.ticks_font)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='x', direction=para.xtick_direction)
ax.tick_params(axis='y', direction=para.ytick_direction)
ax.bar(data, data1,
       width=para.bar_width,
       align='center',
       color='',
       ec='k')
ax.set_ylabel(para.ylabel, para.ylabel_font)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')



