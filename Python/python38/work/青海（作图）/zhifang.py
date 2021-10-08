
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt

ds = gdal.Open(r'E:/Public/JiangJun/标准流程数据/shuju_chuli/IM_jisuan/IM_fenxi/IM_slope2_mask.tif')
data = ds.ReadAsArray()
data = data[~np.isnan(data)]


class para:
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    xtick_direction = 'out'
    ytick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    ylabel = 'Frequency (%)'
    xlabel = 'IM_slope'
    frames = ['right', 'top']
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format('Frequency_IM_slope')
    dpi = 300


fig, ax = plt.subplots(1, 1)
labels = ax.get_xticklabels() + ax.get_yticklabels()
ax.set_xlabel(para.xlabel, para.xlabel_font)
ax.set_ylabel(para.ylabel, para.ylabel_font)
for label in labels:
    label.set_fontname(para.ticks_font)
    label.set_size(para.ticks_size)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='x', direction=para.xtick_direction)
ax.tick_params(axis='y', direction=para.ytick_direction)
ax.hist(data, bins=50, density=1, ec="black", alpha=0.7)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')



