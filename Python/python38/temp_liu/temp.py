
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

file = glob(r'E:/temp/青海/' + '*' + '.csv')
for i, j in enumerate(file):
    temp = np.loadtxt(j, delimiter=",")
    if i == 0:
        data = temp
    else:
        data = np.vstack([data, temp[1]])
data = data[:, 1:]


class para(object):
    Line1_type = '-o'
    Line1_color = 'r'
    Line2_color = 'g'
    Line1_type1 = '-^'
    Line3_type = '-s'
    Line3_color = 'k'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    Line1_label = 'NPP'
    Line2_label = 'Rh'
    Line3_label = 'NEP'
    ylabel = 'NPP and Rh (gCm⁻²a⁻¹)'
    ylabel1 = 'NEP (gCm⁻²a⁻¹)'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = r'E:\temp\青海\NPP_Rh_NEP.png'
    dpi = 300


fig, ax = plt.subplots()
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
ax.plot(data[0], data[2], para.Line1_type, color=para.Line1_color, label=para.Line1_label)
ax.plot(data[0], data[3], para.Line1_type1, color=para.Line2_color, label=para.Line2_label)
ax1.plot(data[0], data[1], para.Line3_type, color=para.Line3_color, label=para.Line3_label)
ax.legend(loc=2, bbox_to_anchor=[0.1, 0.9], prop=para.Legend1_prop, frameon=False, handlelength=2)
ax1.legend(loc=2, bbox_to_anchor=[0.3, 0.9], prop=para.Legend1_prop, frameon=False, handlelength=2)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
