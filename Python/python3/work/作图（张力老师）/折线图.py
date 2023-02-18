
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math
from scipy.stats import t

s = 10
col = 'PRCP'
df = pd.read_excel(r'E:\study\资料\张力老师作图\土壤可蚀性\叶辉 土壤可蚀性k值 原始数据.xlsx',
                   usecols=[37, 43, 51, 128], sheet_name='Sheet1')
df.columns = ['ELEVATION', 'PRCP', 'a', 'K']
data1 = df[[col, 'K']]
data1 = data1.dropna().sort_values(by=col, ascending=0)
data1_min = data1[col].min()
data1_max = data1[col].max()
bins = [i for i in range(int(data1_min), int(data1_max)+s, s)]
label = [i for i, j in enumerate(range(int(data1_min), int(data1_max), s))]
data1['temp'] = pd.cut(data1[col], bins, labels=label)
temp1 = data1.groupby('temp')[col].mean()
temp2 = data1.groupby('temp')['K'].mean()
temp3 = data1.groupby('temp')['K'].sem()
data1 = pd.DataFrame([temp1, temp2, temp3])
data1 = data1.dropna(axis=1).values
conf_interval_RL = [1.960*i for i in data1[2]]


class para(object):
    fmt = '-'
    Line1_color = 'k'
    Line2_type = '-'
    Line2_color = 'r'
    Legend1_prop = {'family': 'Times New Roman', 'size': 12}
    Legend2_prop = {'family': 'Times New Roman', 'style': 'italic', 'size': 12}
    frames = ['right', 'top']
    ytick = np.arange(0, 0.05, 0.01)
    Line1_label = '全区 $\mathrm{Whole \; area }$'
    Line2_label = '%$\mathrm{95}$置信区间 %$\mathrm{95 \; confidence \; interval}$'
    ylabel = '土壤可蚀性$\mathrm{K ((t·hm¹·h)/(hm¹·MJ·mm))}$'
    xlabel = '降水 $\mathrm{precipitation \; (mm)}$'
    xlabel_font = {'family': 'Times New Roman', 'size': 14}
    ylabel_font = {'family': 'Times New Roman', 'size': 14}
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 14
    save_path = 'E:\study\资料\张力老师作图\土壤可蚀性\{0}.png'.format('降水与k值')
    dpi = 600


config = {
    "font.family": 'serif',
    "font.size": 14,
    "mathtext.fontset": 'stix',
    "font.serif": 'Simsun',
}
rcParams.update(config)
fig, ax = plt.subplots()
labels = ax.get_xticklabels() + ax.get_yticklabels()
ax.set_xlabel(para.xlabel)
ax.set_ylabel(para.ylabel)
for label in labels:
    label.set_fontname(para.ticks_font)
    label.set_size(para.ticks_size)
ax.tick_params(axis='both', direction=para.tick_direction)
ax.plot(data1[0], data1[1], '-', color='k', lw=1, label=para.Line1_label)
ax.fill_between(data1[0], (data1[1]-conf_interval_RL), (data1[1]+conf_interval_RL), color='r', alpha=.2,
                label=para.Line2_label)
ax.legend(loc=2, frameon=False, handlelength=2)
ax.set_yticks(para.ytick)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

