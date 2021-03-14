
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.loadtxt(r'E:\Public\JiangJun\标准流程数据\shuju_chuli\NPP\NPP_every_year_mean_value\NPP_year_mean_value.csv',
                  delimiter=",")
data1 = data[0]
data2 = data[1]
OLS = stats.linregress(data1, data2)
y_pred = OLS[0] * data1 + OLS[1]
symbol = '+'
if OLS[1] < 0:
    symbol = '-'
s = format(OLS[0], '.4f')
r = format(OLS[2], '.4f')
d = format(abs(-OLS[1]), '.4f')
n = data1.size


class para(object):
    Line1_type = '--s'
    Line1_color = 'k'
    Line2_type = '-'
    Line2_color = 'r'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    frames = ['right', 'top']
    Legend_x = 1999.5
    Legend_y = 107
    Legend_l = 13
    bbox_to_anchor = [0.6, 0.4]
    Line1_label = 'NPP'
    Line2_label = 'y = {0} x {1} {2}\n(R = {3} , n = {4} , P < 0.01)'.format(s, symbol, d, r, n)
    ylabel = 'NPP (gcm⁻²a⁻¹)'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 12}
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 12
    save_path = 'E:\Public\monarch\青海草地地表通量网络观测与模拟图片\{0}.png'.format(Line1_label)
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
