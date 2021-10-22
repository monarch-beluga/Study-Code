
import dbfread
import numpy as np
from glob import glob
from scipy import stats
import matplotlib.pyplot as plt


class para1(object):
    Folder_path = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/PRCP/PRCP_ddq/'
    File_extension = '.dbf'
    ini_year = 1980
    end_year = 2018
    area = 3


data1 = []
data2 = []
for year in range(para1.ini_year, para1.end_year + 1):
    file = glob(para1.Folder_path + '*' + str(year) + '*' + para1.File_extension)
    table = dbfread.DBF(file[0])
    b = [i['MEAN'] for i in table]
    data2.append(b)
    data1.append(year)
data2 = np.array(data2).T[para1.area]
data1 = np.array(data1)
OLS = stats.linregress(data1, data2)
y_pred = OLS[0] * data1 + OLS[1]
symbol = '+'
if OLS[1] < 0:
    symbol = '-'
s = format(OLS[0], '.2f')
r = format(OLS[2], '.2f')
d = format(abs(OLS[1]), '.2f')
n = data1.size


class para(object):
    Line1_type = '-o'
    Line1_color = 'k'
    Line2_type = '-'
    Line2_color = 'k'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    frames = ['right', 'top']
    Legend_x = 1988.5
    Legend_y = 520
    Legend_l = 12
    bbox_to_anchor = [0.4, 1.1]
    Line1_label = 'Yushuxi'
    Line2_label = 'y = {0} x {1} {2}\n(R = {3} , n = {4} , P < 0.01)'.format(s, symbol, d, r, n)
    ylabel = 'Annual precipitation (mm)'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 10
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}_prc.png'.format(Line1_label)
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
ax.tick_params(axis='both', direction=para.tick_direction)
ax.plot(data1, data2, para.Line1_type, color=para.Line1_color, label=para.Line1_label)
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

