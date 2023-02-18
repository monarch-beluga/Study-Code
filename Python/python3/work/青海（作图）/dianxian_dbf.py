
import dbfread
import numpy as np
from glob2 import glob
import matplotlib.pyplot as plt


class para1(object):
    Folder_path = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/TAVG/TAVG_ddq/'
    File_extension = '.dbf'
    ini_year = 1980
    end_year = 2018


data1 = []
data2 = []
for year in range(para1.ini_year, para1.end_year + 1):
    file = glob(para1.Folder_path + '*' + str(year) + '*' + para1.File_extension)
    table = dbfread.DBF(file[0])
    b = [i['MEAN'] for i in table]
    data2.append(b)
    data1.append(year)
data2 = np.array(data2).T
data1 = np.array(data1)


class para(object):
    Line_marker = ['^', 'o', 'p', 's']
    Line_ls = ['-.', '--', '-', '-']
    Legend = ['果洛东', '黄南', '果洛西', '海东']
    frames = ['right', 'top']
    Legend1_prop = {'family': 'SimSun', 'size': 12}
    # Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    # Line2_label = 'y = {0} x - {1}\n(R = {2} , n = {3} , P < 0.01)'.format(s, d, r, n)
    ylabel = 'Annual mean temperature (°C)'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = r'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\四大地区.png'
    dpi = 300


fig, ax = plt.subplots(1, 1)
labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontname(para.ticks_font)
    label.set_size(para.ticks_size)
ax.set_xlabel(para.xlabel, para.xlabel_font)
ax.set_ylabel(para.ylabel, para.ylabel_font)
for i, j in zip([0, 1, 2, 3], [2, 4, 6, 8]):
    ax.plot(data1, data2[j], marker=para.Line_marker[i], ls=para.Line_ls[i], c='k', label=para.Legend[i])
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='both', direction=para.tick_direction)
ax.legend(bbox_to_anchor=[0.1, 1.1], loc=2, ncol=2, prop=para.Legend1_prop, frameon=False, handlelength=3)
# fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

