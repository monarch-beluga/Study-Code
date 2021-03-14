
import numpy as np
import pandas as pd
from glob import glob
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


class para1:
    path = r'E:/temp/shuju/折线1/R_correlstion/'

'''
读取数据并处理
'''
File = glob(para1.path + '*.xlsx')
data = []
for i, file in enumerate(File):
    temp = pd.read_excel(file, sheet_name='R')
    if i == 0:
        data = temp
    else:
        data = pd.concat([data, temp])
data = data.round(3).values
data1 = np.arange(1995, 2016, 5)


class para(object):
    n = 6
    x = 3
    y = 2
    Line1_type = [':o', ':o', ':o', ':o', ':o', ':o', ':o']
    Line1_color = ['m', 'y', 'g', 'c', 'b', 'r']
    frames = ['right', 'top']
    Legend1_prop = {'family': 'Times New Roman', 'size': 14}
    ylabel = 'Pearson correlation coefficient'
    xlabel = 'Year'
    xlabel_font = {'family': 'Times New Roman', 'size': 14}
    ylabel_font = {'family': 'Times New Roman', 'size': 14}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 14
    title = ['(A)', '(B)', '(C)', '(D)', '(E)', '(F)']
    save_path = 'E:/temp/shuju/折线1/Fs12.jpg'
    dpi = 300


fig = plt.figure(figsize=(10, 15))
ax1 = fig.add_subplot(111)
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.spines['right'].set_color('none')
ax1.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
x_major_locator = MultipleLocator(5)
for i in range(para.n):
    ax = fig.add_subplot(para.x*100+para.y*10+i+1)
    ax.locator_params(nbins=4)
    # for frame in para.frames:
    #     ax.spines[frame].set_visible(False)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    for label in labels:
        label.set_fontname(para.ticks_font)
        label.set_size(para.ticks_size)
    ax.tick_params(axis='both', direction=para.tick_direction)
    ax.set_xlabel(para.xlabel, para.xlabel_font)
    ax.set_title(para.title[i], fontproperties=para.ticks_font, fontsize=para.ticks_size)
    ax.plot(data1, data[i], para.Line1_type[i], color='k')
    ax.xaxis.set_major_locator(x_major_locator)
    for x, y in zip(data1, data[i]):
        if x == 2015:
            x -= 5
        else:
            x += 1
        ax.text(x, y, y, para.Legend1_prop)
ax1.tick_params(axis='both', direction=para.tick_direction)
ax1.set_ylabel(para.ylabel, para.ylabel_font)
plt.xlim(1993, 2016, 5)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
