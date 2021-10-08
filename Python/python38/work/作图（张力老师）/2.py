
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math
from scipy.stats import t

s = 100
col = 'ELEVATION'
df = pd.read_excel(r'E:\study\资料\张力老师作图\叶辉 土地利用 降水 海拔 发送版.xlsx',
                   usecols=[7, 13, 21, 106], sheet_name='Sheet1')
x = '0'
temp = []
temp1 = []
select = []
df.columns = ['ELEVATION', 'PRCP', 'a', 'K']
data1 = df[[col, 'K', 'a']]
data1 = data1.dropna()
for i in data1['a']:
    if x in i:
        temp.append(x)
    else:
        x = i
        temp.append(x)
for j, i in enumerate(temp):
    if i in ['旱地', '水田', '水浇地']:
        temp[j] = '耕地'
for i in temp:
    if (i != x) & (i not in temp1):
        x = i
        temp1.append(x)
    else:
        continue
data1['temp'] = temp
data2 = []


class para(object):
    line_font = ['-', '--']
    line_color = ['b', 'g', 'r', 'c', 'm', 'y']
    Legend_prop = {'family': 'Simsun', 'size': 12}
    ylabel = '土壤可蚀性$\mathrm{K ((t·hm¹·h)/(hm¹·MJ·mm))}$'
    xlabel = '高程 $\mathrm{elevation \; (m)}$'
    tick_direction = 'in'
    ticks_font = 'Times New Roman'
    ticks_size = 14
    n = len(line_font)
    save_path = 'E:\study\资料\张力老师作图\土壤可蚀性\{0}.png'.format('高程（分类型）与k值')
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
for j, i in enumerate(temp1):
    font = para.line_font[j % para.n]
    color = para.line_color[j // para.n]
    data = data1[data1['temp'] == i]
    bins = [i for i in range(int(data[col].min())-1, int(data[col].max())-1+s, s)]
    label1 = [j for i, j in enumerate(range(int(data[col].min()), int(data[col].max()), s))]
    data['temp1'] = pd.cut(data[col], bins, labels=label1)
    temp2 = data.groupby('temp1')[col].mean()
    temp3 = data.groupby('temp1')['K'].mean()
    temp4 = data.groupby('temp1')['K'].count()
    data2.append(temp4)
    data = pd.DataFrame([temp2, temp3])
    data = data.dropna(axis=1).values
    ax.plot(data[0], data[1], ls=font, color=color, lw=1, label=i)
# ax.fill_between(data1[0], (data1[1]-conf_interval_RL), (data1[1]+conf_interval_RL), color='r', alpha=.2,
#                 label=para.Line2_label)
ax.legend(loc=7, prop=para.Legend_prop, bbox_to_anchor=[1.4, 0.5], frameon=False, handlelength=2)
# ax.set_yticks(para.ytick)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

