import dbfread
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt

file = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/TAVG/TAVG_fenxi/TAVG_R2_mask'
data = ['Qinghai', 'Haibei', 'Yushudong', 'Guoluodong', 'Yushuxi', 'Huangnan', 'Tanggula',
        'Guoluoxi', 'Hainan', 'Haidong', 'Haixi']
ds = gdal.Open(file + '.tif')
data1 = ds.ReadAsArray()
data1[data1 == data1[0][0]] = np.nan
data2 = [np.std(data1[~np.isnan(data1)])]
data1 = [data1[~np.isnan(data1)].mean()]
table = dbfread.DBF(file + '.dbf')
for i in table:
    data1.append(i['MEAN'])
table = dbfread.DBF(file + '_std.dbf')
for i in table:
    data2.append(i['STD'])


class para:
    bar_width = 0.6
    bar_align = 'center'
    ticks_font = 'Times New Roman'
    xtick_direction = 'out'
    ytick_direction = 'in'
    frames = ['right', 'top']
    error_kw = {'ecolor': 'k', 'capsize': 2, 'elinewidth': 0.5}
    ylabel = 'Multiple correlation coefficient'
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format('R2_TAVG')
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
ax.bar(data, data1, yerr=data2,
       width=para.bar_width,
       align='center',
       color='',
       ec='k',
       error_kw=para.error_kw)
ax.set_ylabel(para.ylabel, para.ylabel_font)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

