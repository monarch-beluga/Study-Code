# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:50:26 2020

@author: XiHuang O.Y.
"""

import os,sys,xlsxwriter
import pandas as pd
import numpy as np
from glob import glob as glb
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.font_manager import FontManager, FontProperties
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes


fpath = r'F:\文件\工作\NDVI_Zonal'
flist = glb(fpath+os.sep+'JX*Mean.xlsx')
#-----------------plot setting-------------------------------------------------
#title setting
title_name = "土地利用现状一级分类面积"
title_fontsz = 14
#tick and tick label setting
font_prop = fm.FontProperties(fname=r'C:\Windows\Fonts\times.ttf')   # 设置字体

#color setting facecolor-> column color; ax_facecolor-> column background color
facecolor = [1, 0.5, 0.3]
ax_facecolor = [0.4, 0.78, 0.60]
edgecolor = 'black' # bar edgecolor setting
#bar_width = 0.8
#other setting
lwidth = 4.0    # axis width
lw_spines = 1.0   # x,y spines width
marksize = 8
linestyle = '-'  # bar linestyle
c1 = 'g'        #颜色1
c2 = 'r'        #颜色2
c3 = 'b'        #颜色3
xlabel_fontsz = 14      #x轴字体大小
tick_labelsz = 2
tick_pad = 8
#修改主刻度
xmajorLocator = MultipleLocator(1) #将x主刻度标签设置为5的倍数
ymajorLocator = MultipleLocator(0.05) #将y轴主刻度标签设置为0.5的倍数
#修改次刻度
xminorLocator = MultipleLocator(5) #将x轴次刻度标签设置为1的倍数
yminorLocator = MultipleLocator(0.05) #将此y轴次刻度标签设置为0.1的倍数


def getChineseFont(tSize):  #Title字体设置
    return FontProperties(size=tSize,fname=r'C:\Windows\Fonts\simsun.ttc')

def plot_line_(name,x,y1,y2,y3):
    #fig = plt.figure(figsize=(7,5))  #figsize默认为4,4(图像尺寸),facecolor="blue"
    fig = plt.figure(1)  #figsize默认为4,4(图像尺寸),facecolor="blue"
    ax = HostAxes(fig, [0.15, 0.1, 0.7, 0.8])  #用[left, bottom, weight, height]的方式定义axes，0 <= l,b,w,h <= 1
    ax_ndvi = ParasiteAxes(ax, sharex=ax)
    ax_t = ParasiteAxes(ax, sharex=ax)
    ax_p = ParasiteAxes(ax, sharex=ax)
    
    ax.parasites.append(ax_ndvi)
    ax.parasites.append(ax_p)
    ax.parasites.append(ax_t)
    
    ax.set_ylim(0.41,0.75)
    ax.set_xlim(2004.5,2015.5)
    ax.axis['right'].set_visible(False)
    ax.axis['top'].set_visible(False)
#    plt.tick_params(top = 'off', right = 'off')
    #ax_ndvi.axis['left1'] = new_axisline(loc='left', axes=ax_ndvi, offset=offset1)
    #ax.axis['left'].set_axisline_style('->',size=2)  #轴的形状色
    ax.axis['left'].line.set_linewidth(3)   #轴宽
    ax.axis['bottom'].line.set_linewidth(3)   #轴宽
    
    offset1 = (20, 0)
    offset2 = (60, 0)
    ax_t.set_ylim(10,30)
    ax_p.set_ylim(500,2500)
    new_axisline = ax_t._grid_helper.new_fixed_axis     # "_grid_helper"与"get_grid_helper()"等价，可以代替  #new_axisline = par2.get_grid_helper().new_fixed_axis  # 用"get_grid_helper()"代替，结果一样，区别目前不清楚
    new_axisline = ax_p._grid_helper.new_fixed_axis
    ax_t.axis['right2'] = new_axisline(loc='right', axes=ax_t, offset=offset1)
    #ax_t.axis['right2'].set_axisline_style('-|>',size=-1)  #轴的形状色
    ax_t.axis['right2'].line.set_linewidth(3)   #轴宽
    ax_t.axis['right2'].set_label('T')                  # ax_t.axis['right2'].set_axislabel_direction('-')
    ax_p.axis['right3'] = new_axisline(loc='right', axes=ax_p, offset=offset2)
    #ax_p.axis['right3'].set_axisline_style('->',size=-1)  #轴的形状色
    ax_p.axis['right3'].line.set_linewidth(3)   #轴宽
    ax_p.axis['right3'].set_label('P')
    
    ax_t.yaxis.set_major_locator(MultipleLocator(2))
    ax_p.yaxis.set_major_locator(MultipleLocator(500))
    ax.xaxis.set_major_locator(xmajorLocator)    #设置主刻度标签的位置,没有标签文本格式ax.xaxis.set_major_formatter(FormatStrFormatter('%5.1f'))
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.xaxis.set_minor_locator(xminorLocator)    #设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(xminorLocator)
    
    #打开网格
    ax_ndvi.grid(which='minor',color='black',linestyle='--')#,lw=0.8, alpha=0.5)  # grid setting)  #绘制网格线
    ax_t.grid(which='minor',color='black',linestyle='--')#,lw=0.8, alpha=0.5)  # grid setting)  #绘制网格线
    ax.tick_params(axis='both', which='major', direction='in', width=2,length=lwidth, pad=tick_pad, labelsize=tick_labelsz, grid_linewidth=3)
    
    ax.set_ylabel('NDVI',font_properties=getChineseFont(80))
    #ax.set_ylabel('NDVI',fontproperties=getChineseFont(100))
    
    
    ax_t.tick_params(axis='both', which='both', direction='in', width=3,length=100, pad=18, labelsize=100, grid_linewidth=1)
    ax_p.tick_params(axis='both', which='both', direction='in', width=3,length=100, pad=18, labelsize=100, grid_linewidth=1)
    
    fig.add_axes(ax)
    
    ax.set_xlabel('Year')
    p1, = ax.plot(x, y1, label="NDVI", ls=linestyle, lw=lwidth, color=c1, marker=".", ms= 16, mfc=c1)
    p2, = ax_t.plot(x, y3, label="Temperature", ls=linestyle, lw=lwidth, color=c2, marker="o", ms= marksize, mfc=c2)
    p3, = ax_p.plot(x, y2, label="Precipitation", ls=linestyle, lw=lwidth, color=c3, marker="o", ms= marksize, mfc=c3)
    #ax.set_xlabel('YEAR')
    #ax.set_ylabel('NDVI')
    plt.legend(loc=1,bbox_to_anchor=(0.9, 1.2),prop=getChineseFont(12),ncol=1,frameon=False,mode='expend')
    
    #plt.savefig(r'C:\Users\YeHui\Desktop\GGGGGGGGGGG.jpg')#, dpi=1000)
    plt.show()

df = []
flist.sort()
for file_ in flist:
    df.append(pd.read_excel(file_,header=0,index_col =1))


df1 = df[0].iloc[:,6:16+1]
df2 = df[1].iloc[:,6:16+1]
df3 = df[2].iloc[:,6:16+1]
# fig = plt.figure(figsize=[19, ])
for i in range(0,len(df[0].index)):
    name = df1.index[0]
    x = np.arange(2005,2015+1)
    y1 = df1.iloc[i,:]
    y2 = df2.iloc[i,:]
    y3 = df3.iloc[i,:]
    plot_line_(name, x, y1,y2,y3)
    pass








