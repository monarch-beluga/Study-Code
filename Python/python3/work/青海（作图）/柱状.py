
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv(r'E:\temp\TAVG_ddqall_sta.csv', sep=',', header=0)
data1 = df[['mean', 'std']]
data = ('Haibei', 'Yushudong', 'Guoluodong', 'Yushuxi', 'Huangnan', 'Tanggula',
        'Guoluoxi', 'Hainan', 'Haidong', "Haixi")


class para:
    bar_width = 0.6
    bar_align = 'center'
    ticks_font = 'Times New Roman'
    xtick_direction = 'in'
    ytick_direction = 'in'
    frames = ['right', 'top']
    ylabel = 'Mean of ATM'
    ylabel_font = {'family': 'Times New Roman', 'size': 12}
    error_kw = {'ecolor': 'k', 'capsize': 2, 'elinewidth': 0.5}
    save_path = r'E:\temp\TAVG_ddqall_sta.png'
    dpi = 300


fig, ax = plt.subplots(1, 1)
ax.spines['bottom'].set_position(('data', 0))
ax.set_xticklabels(data, rotation=-30, fontsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
for label in labels:
    label.set_fontname(para.ticks_font)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='x', direction=para.xtick_direction)
ax.tick_params(axis='y', direction=para.ytick_direction)
ax.bar(data, data1['mean'], yerr=data1['std'],
       width=para.bar_width,
       align='center',
       color='',
       ec='k',
       error_kw=para.error_kw)
ax.set_ylabel(para.ylabel, para.ylabel_font)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')
