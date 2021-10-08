
import numpy as np
import matplotlib.pyplot as plt


class para1(object):
    Folder_path = r'E:/Public/JiangJun/标准流程数据/shuju_chuli/IM/'
    File_extension = '.flt'
    ini_year = 1980
    end_year = 2018


data1 = np.loadtxt(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\PRCP\PRCP_every_year_mean_value\PRCP_year_mean_value.csv',
                   delimiter=",")
data = np.loadtxt(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\NPP\NPP_every_year_mean_value\NPP_year_mean_value.csv'
                  , delimiter=",")


class para(object):
    Line1_type = '-s'
    Line1_color = 'k'
    Line2_color = 'k'
    Line1_type1 = '-^'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    Line1_label = 'NPP'
    Line3_label = 'APPT'
    ylabel = 'NPP (gcm⁻²a⁻¹)'
    ylabel1 = 'Anual precipitation (mm)'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}_{1}.png'.format(Line1_label, Line3_label)
    dpi = 300


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
ax.plot(data[0], data[1], para.Line1_type, color=para.Line1_color, label=para.Line1_label)
ax1.plot(data1[0], data1[1], para.Line1_type1, color=para.Line1_color, label=para.Line3_label)
ax.legend(loc=2, prop=para.Legend1_prop, frameon=False, handlelength=2)
ax1.legend(loc=9, prop=para.Legend1_prop, frameon=False, handlelength=2)
# fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
