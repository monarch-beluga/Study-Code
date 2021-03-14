
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


class para1:
    path = r'E:/temp/shuju/折线/'


File = glob(para1.path + '*.csv')
for i, file in enumerate(File):
    temp = np.loadtxt(file, delimiter=",")
    temp = temp[:, 1].reshape(1, -1)
    if i == 0:
        data = temp
    else:
        data = np.vstack((data, temp))
data1 = np.arange(1995, 2016, 1)


class para(object):
    Line1_type = ['-', '-', '-', '-', '-', '-', '-']
    Line1_color = ['m', 'y', 'g', 'c', 'b', 'r']
    xtick = np.arange(1995, 2016, 5)
    frames = ['right', 'top']
    Legend1_prop = {'family': 'Times New Roman', 'size': 14}
    ylabel = ['Soil conservation (t ˙ ha⁻¹ ˙ a⁻¹)', 'Food supply (t ˙ ha⁻¹ ˙ a⁻¹)',
              'Habitat quality', 'Net primary productivity (gCm⁻²a⁻¹)'
              , 'Mean annual precipitation (mm)', 'Mean annual temperature (°C)']
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 14}
    ylabel_font = {'family': 'Times New Roman', 'size': 14}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 14
    title = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
    save_path = 'E:/temp/shuju/折线/all_vars1.jpg'
    dpi = 300


fig, ax = plt.subplots(3, 2, figsize=(12, 16))
x_major_locator = MultipleLocator(5)
for x in range(3):
    for y in range(2):
        n = x*2 + y
        labels = ax[x][y].get_xticklabels() + ax[x][y].get_yticklabels()
        for label in labels:
            label.set_fontname(para.ticks_font)
            label.set_size(para.ticks_size)
        ax[x][y].plot(data1, data[n], ls=para.Line1_type[n], color='k', ms=3)
        ax[x][y].set_xlabel(para.xlabel, para.xlabel_font)
        ax[x][y].set_ylabel(para.ylabel[n], para.ylabel_font)
        # for frame in para.frames:
        #     ax[x][y].spines[frame].set_visible(False)
        ax[x][y].tick_params(axis='both', direction=para.tick_direction)
        ax[x][y].set_xticks(para.xtick)
        ax[x][y].set_title(para.title[n], fontproperties=para.ticks_font, fontsize=para.ticks_size)
plt.xlim(1993, 2016)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
