
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt


class para1(object):
    Folder_path = r'E:/temp/npp/sta'
    File_extension = '.csv'
    file = r"E:\temp\npp\Rh_ddq_80-18_sta.csv"
    FILE = 'Rh'
    ini_year = 1980
    end_year = 2010


data = pd.read_csv(para1.file, sep=',', header=0, index_col=0).values
for year in range(para1.ini_year, para1.end_year + 1, 10):
    file = glob(para1.Folder_path + '*' + para1.FILE + str(year) + '*' + para1.File_extension)
    temp = pd.read_csv(file[0], sep=',', header=0, index_col=0).values
    data = np.hstack([data, temp])
data2 = data.T
data1 = np.arange(1, 11)
data = ['Haibei', 'Yushudong', 'Guoluodong', 'Yushuxi', 'Huangnan', 'Tanggula',
        'Guoluoxi', 'Hainan', 'Haidong', 'Haixi']


class para:
    bar_width = 0.165
    bar_color = ['r', 'g', 'b', 'c', 'y']
    num = 5
    Line_labels = ['1980-2018', '1980-1990', '1990-2000', '2000-2010', '2010-2018']
    bar_align = 'center'
    ticks_font = 'Times New Roman'
    xtick_direction = 'in'
    ytick_direction = 'in'
    frames = ['right', 'top']
    ylabel = 'Rh (gCm⁻²a⁻¹)'
    xlabel = 'Location'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    save_path = r'E:\temp\npp\tupian\{0}.png'.format('Rh_Location')
    dpi = 300


fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlabel(para.xlabel, para.xlabel_font)
ax.set_ylabel(para.ylabel, para.ylabel_font)
labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontname(para.ticks_font)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='x', direction=para.xtick_direction)
ax.tick_params(axis='y', direction=para.ytick_direction)
for i in range(para.num):
    ax.bar(data1+para.bar_width*i, data2[i],
           width=para.bar_width,
           align='center',
           color=para.bar_color[i],
           ec='k',
           label=para.Line_labels[i])
ax.legend(bbox_to_anchor=[0.8, 0.9], prop=para.ylabel_font, frameon=False, handlelength=2)
ax.set_xticks(data1 + para.bar_width * (para.num / 2.0))
ax.set_xticklabels(data, rotation=-30, fontsize=12)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
