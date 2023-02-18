
import numpy as np
from osgeo import gdal
from scipy import stats
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


data3 = []
data4 = []
path = para1.Folder_path
for year in range(para1.ini_year, para1.end_year + 1):
    file = glob(path + '*' + str(year) + '*' + para1.File_extension)
    ds = gdal.Open(file[0])
    temp = ds.ReadAsArray()
    temp[np.isnan(mask)] = np.nan
    data2 = temp[~np.isnan(temp)]
    data1 = np.array([data2[(data2 <= -66.7) & (data2 > -100)].mean(),
                      data2[(data2 > -66.7) & (data2 <= -33.3)].mean(),
                      data2[(data2 <= 0) & (data2 > -33.3)].mean(),
                      data2[(data2 > 0) & (data2 <= 20)].mean(),
                      data2[(data2 > 20) & (data2 <= 40)].mean(),
                      data2[(data2 > 40) & (data2 <= 60)].mean(),
                      data2[(data2 > 60) & (data2 <= 80)].mean(),
                      data2[(data2 > 80) & (data2 <= 100)].mean(),
                      ])
    data3.append(data1)
    data4.append(year)
data = ['arid', 'semiarid', 'dry subhumid', 'moist subhumid', 'humid1', 'humid2', 'humid3', 'humid4']
data2 = np.array(data3).T
data3 = []
for i in range(8):
    OLS = stats.linregress(data4, data2[i])
    data3.append(OLS[0])
data1 = np.array(data3)


class para:
    bar_width = 0.6
    bar_align = 'center'
    ticks_font = 'Times New Roman'
    xtick_direction = 'out'
    ytick_direction = 'in'
    frames = ['right', 'top']
    ylabel = 'Slope of IM'
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format('Area_slope_IM')
    dpi = 300


fig, ax = plt.subplots(1, 1)
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
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



