
from osgeo import gdal
import pandas as pd
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


data = np.loadtxt(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\TAVG\TAVG_every_year_mean_value\TAVG_year_mean_value.csv',
                  delimiter=",")
data3 = data[0]
data4 = data[1]
OLS = stats.linregress(data3, data4)
y_pred1 = OLS[0] * data3 + OLS[1]
symbol1 = '+'
if OLS[1] < 0:
    symbol1 = '-'
s1 = format(OLS[0], '.2f')
r1 = format(OLS[2], '.2f')
d1 = format(abs(-OLS[1]), '.2f')
n1 = data3.size
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
    Line1_type1 = '--^'
    Line2_type1 = '--'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    Legend_x = 1986.8
    Legend_y = -18
    Legend_l = 3
    bbox_to_anchor = [0.28, 1]
    Legend_x1 = 1996
    Legend_y1 = -1.78
    Legend_l1 = 0.2
    bbox_to_anchor1 = [0.3, 0.25]
    Line1_label = 'IM'
    Line2_label = 'y = {0} x {1} {2}\n(R = {3} , n = {4} , P < 0.01)'.format(s, symbol, d, r, n)
    Line3_label = 'ATM'
    Line4_label = 'y = {0} x {1} {2}\n(R = {3} , n = {4} , P < 0.01)'.format(s1, symbol1, d1, r1, n1)
    ylabel = 'IM'
    ylabel1 = 'Temperature (°C)'
    xlabel = 'Year'
    ytick = np.arange(-70, 0, 10)
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}_{1}.png'.format(Line1_label, Line3_label)
    dpi = 300


def fun(ax2, X, Y, L, Label):
    x1 = X
    y1 = Y
    for i in Label:
        if i == '\n':
            x1 = X - 4
            y1 -= L
            continue
        if ((i <= 'Z') & (i >= 'A')) | ((i <= 'z') & (i >= 'a')):
            ax2.text(x1, y1, i, para.Legend2_prop)
        else:
            ax2.text(x1, y1, i, para.Legend1_prop)
        x1 += 0.67


fig, ax = plt.subplots(1, 1)
ax1 = ax.twinx()
labels = ax.get_xticklabels() + ax.get_yticklabels() + ax1.get_yticklabels()
ax.set_xlabel(para.xlabel, para.xlabel_font)
ax.set_ylabel(para.ylabel, para.ylabel_font)
ax1.set_ylabel(para.ylabel1, para.ylabel_font)
for label in labels:
    label.set_fontname(para.ticks_font)
    label.set_size(para.ticks_size)
ax.tick_params(axis='both', direction=para.tick_direction)
ax1.tick_params(axis='y', direction=para.tick_direction)
ax.plot(data1, data2, para.Line1_type, color=para.Line1_color, label=para.Line1_label)
ax.plot(data1, y_pred, para.Line2_type, color=para.Line2_color, label=' ')
ax1.plot(data3, data4, para.Line1_type1, color=para.Line1_color, label=para.Line3_label)
ax1.plot(data3, y_pred1, para.Line2_type1, color=para.Line2_color, label=' ')
ax.legend(bbox_to_anchor=para.bbox_to_anchor,  prop=para.Legend1_prop, frameon=False, handlelength=2)
ax1.legend(bbox_to_anchor=para.bbox_to_anchor1,  prop=para.Legend1_prop, frameon=False, handlelength=2)
ax.set_yticks(para.ytick)
fun(ax, para.Legend_x, para.Legend_y, para.Legend_l, para.Line2_label)
fun(ax1, para.Legend_x1, para.Legend_y1, para.Legend_l1, para.Line4_label)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')



