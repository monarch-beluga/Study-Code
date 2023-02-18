
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

s = 100
col = 'ELEVATION'
df = pd.read_excel(r'E:\study\资料\张力老师作图\叶辉 土地利用 降水 海拔 发送版.xlsx',
                   usecols=[7, 13, 21, 106], sheet_name='Sheet1')
x = '0'
temp = []
temp1 = []
select = []
df.columns = ['ELEVATION', 'PRCP', 'a', 'K']
data1 = df[['K', 'a']]
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
Data = data1.groupby('temp')['K'].mean()
DAta = np.array(data1.groupby('temp')['K'].std())
Data1 = np.array(Data)


class para:
    bar_width = 0.6
    bar_align = 'center'
    xticks_font = 'Times New Roman'
    xtick_direction = 'in'
    color = ['lime', 'gray', 'r', 'coral', 'tan', 'orange', 'y', 'g', 'c', 'b']
    frames = ['right', 'top']
    ylabel = '土壤可蚀性$\mathrm{K ((t·hm¹·h)/(hm¹·MJ·mm))}$'
    ylabel_font = {'family': 'Times New Roman', 'size': 14}
    error_kw = {'ecolor': 'k', 'capsize': 2, 'elinewidth': 0.5}
    save_path = 'E:\study\资料\张力老师作图\土壤可蚀性\{0}.png'.format('k值（土地类型）')
    dpi = 600


fig, ax = plt.subplots(figsize=(12, 8))
config = {
    "font.family": 'serif',
    "font.size": 14,
    "mathtext.fontset": 'stix',
    "font.serif": 'SimSun',
}
rcParams.update(config)
ax.set_xticklabels(Data.index, rotation=-30, fontsize=14)
labels = ax.get_yticklabels()
for label in labels:
    label.set_fontname(para.xticks_font)
for frame in para.frames:
    ax.spines[frame].set_visible(False)
ax.tick_params(axis='both', direction=para.xtick_direction)
for x, y, z, color in zip(Data.index, Data1, DAta, para.color):
    ax.bar(x, y, yerr=z,
           width=para.bar_width,
           align='center',
           color=color,
           error_kw=para.error_kw)
ax.set_ylabel(para.ylabel)
fig.savefig(para.save_path, dpi=para.dpi, bbox_inches='tight')

