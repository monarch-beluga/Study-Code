
from osgeo import gdal
import numpy as np
from glob2 import glob
from scipy import stats
import matplotlib.pyplot as plt

ds1 = gdal.Open(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\PRCP\PRCP_std_80-18\PRCP_std_80-18.tif')
mask = ds1.ReadAsArray()
mask[mask == mask[0][0]] = np.nan


class para1(object):
    Folder_path = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/IM/'
    File_extension = '.flt'
    ini_year = 1980
    end_year = 2018


path = para1.Folder_path
data1 = []
data2 = []
for year in range(para1.ini_year, para1.end_year + 1):
    file = glob(path + '*' + str(year) + '*' + para1.File_extension)
    ds = gdal.Open(file[0])
    temp = ds.ReadAsArray()
    temp[np.isnan(mask)] = np.nan
    temp_mean = temp[~np.isnan(temp)].mean()
    data2.append(temp_mean)
    data1.append(year)
data1 = np.array(data1)
data2 = np.array(data2)
OLS = stats.linregress(data1, data2)
symbol = '+'
if OLS[1] < 0:
    symbol = '-'
y_pred = OLS[0] * data1 + OLS[1]
s = format(OLS[0], '.2f')
r = format(OLS[2], '.2f')
d = format(abs(-OLS[1]), '.2f')
n = data1.size


class para(object):
    Line1_type = '-o'
    Line1_color = 'k'
    Line2_type = '-'
    Line2_color = 'k'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    frames = ['right', 'top']
    Legend_x = 1984.5
    Legend_y = -53.5
    Legend_l = 2
    bbox_to_anchor = [0.2, 0.3]
    Line1_label = 'IM'
    Line2_label = 'y = {0} x {1} {2}\n(R = {3} , n = {4} , P < 0.01)'.format(s, symbol, d, r, n)
    ylabel = 'IM'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format(Line1_label)
    dpi = 300


fig, ax = plt.subplots()
labels = ax.get_xticklabels() + ax.get_yticklabels()
ax.set_xlabel(para.xlabel, para.xlabel_font)
ax.set_ylabel(para.ylabel, para.ylabel_font)
for label in labels:
    label.set_fontname(para.ticks_font)
    label.set_size(para.ticks_size)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='both', direction=para.tick_direction)
ax.plot(data1, data2, para.Line1_type, color=para.Line1_color)
ax.plot(data1, y_pred, para.Line2_type, color=para.Line2_color, label=' ')
ax.legend(bbox_to_anchor=para.bbox_to_anchor,  prop=para.Legend1_prop, frameon=False, handlelength=2)
x = para.Legend_x
y = para.Legend_y
for i in para.Line2_label:
    if i == '\n':
        x = para.Legend_x
        y -= para.Legend_l
        continue
    if ((i <= 'Z') & (i >= 'A')) | ((i <= 'z') & (i >= 'a')):
        ax.text(x, y, i, para.Legend2_prop)
    else:
        ax.text(x, y, i, para.Legend1_prop)
    x += 0.67
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

