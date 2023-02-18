# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 00:22:55 2020

@author: XiHuang O.Y.
"""

import os,sys
import pandas as pd
import numpy as np
from glob import glob as glb
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.font_manager import FontManager, FontProperties
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import f_regression
import statsmodels.formula.api as smf 

plt.rcParams['axes.unicode_minus'] = False  #显示负号
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['font.size'] = '7.5' # 设置字体大小
fpath = r'F:\文件\工作\NDVI_Zonal'
flist = glb(fpath+os.sep+'JX*Mean.xlsx')
#-----------------plot setting-------------------------------------------------
#title setting
title_name = "土地利用现状一级分类面积"
title_fontsz = 8
##tick and tick label setting
#font_prop = fm.FontProperties(fname=r'C:\Windows\Fonts\times.ttf')   # 设置字体

#other setting
#lwidth = 3.0    # axis width
#lw_spines = 1.0   # x,y spines width
lwidth = 2.0    # axis width
lw_spines = 1.0   # x,y spines width
marksize = 3.8
linestyle = '-'  # bar linestyle
c1 = (255/255,24/255,0/255)        #颜色1
c2 = 'b'        #颜色3
xlabel_fontsz = 7.5      #x轴字体大小
tick_labelsz = 2
tick_pad = 8

##==================要素坐标===================
legendp=(0.91, 0.95)

##==================X-Y刻度范围===================
xmin=-2
xmax=2
ymin=-2
ymax=2
y1lim=[-2,2]
y2lim=[500,3000]
ML1 = MultipleLocator(0.5)
ML2 = MultipleLocator(500)
#修改主刻度
xmajorLocator = MultipleLocator(0.5) #将x主刻度标签设置为5的倍数
ymajorLocator = MultipleLocator(0.02) #将y轴主刻度标签设置为0.5的倍数
#修改次刻度
xminorLocator = MultipleLocator(0.25) #将x轴次刻度标签设置为1的倍数
yminorLocator = MultipleLocator(0.01) #将此y轴次刻度标签设置为0.1的倍数
##==================坐标轴线======================
lineW=1.5
xoffset = (20, 0)
yoffset = (60, 0)
labelY='NDVI'
label1=u'Temperature'
label2=u'Precipitation'

def getChineseFont(tSize):  #Title字体设置
    return FontProperties(size=tSize,fname=r'C:\Windows\Fonts\simsun.ttc')

def linear_model(data_x, data_y, func=None):
    regr = LinearRegression()
    regr.fit(data_x, data_y)
    y_pred = regr.predict(data_x)
    r2score = r2_score(data_y, y_pred)          #决定系数(复相关系数)，反映因变量的全部变异能通过回归关系被自变量解释的比例,解释多少【值为0-1】【也可R2score = regr.score(data_x, data_y)】
    ncoef = regr.coef_                          #斜率
    pvalue = f_regression(data_x, data_y)[1]    #p值，小于0.05则相关性显著
    nintercept = regr.intercept_                #截距
    if func is None:
        #return pd.DataFrame(r2score, ncoef, pvalue, nintercept, column = ['r2', 'coef', 'pvalue', 'residual'])
        return r2score, ncoef, pvalue, nintercept
    else:
        func = "y = %.2f*x + %.2f"  %(ncoef, nintercept)
        #return pd.DataFrame(r2score, ncoef, pvalue, nintercept, func, column = ['r2', 'coef', 'pvalue', 'residual', 'func'])
        return r2score, ncoef, pvalue, nintercept, func, y_pred

def multi_linear(y1,y2,y3):
    x=np.column_stack((y2,y3))
    y=np.array(y1)
    reg = LinearRegression()
    reg.fit(x, y)
    
#    fit = smf.ols(x, data = y).fit()
#    fit.summary()
    
    z_pred = reg.predict(x)
    r2score = r2_score(y, z_pred)
    ncoef = reg.coef_
    pvalue = f_regression(x, y)    #p值，小于0.05则相关性显著
    #print(reg.intercept_,reg.coef_[0],reg.coef_[1])
    #print("The linear model is: Y = {:.5} + {:.5}*TV + {:.5}*radio ".format(reg.intercept_,reg.coef_[0],reg.coef_[1]))
    #print(r2score,pvalue)
    func = "Y =%.3f*T + %.3f*P + %.3f"  % (reg.coef_[0],reg.coef_[1],reg.intercept_)
    print("\n\nThe linear model is:\n" +func)
    print('方程的判定系数(R^2): %.2f' % reg.score(x, y))
    print('温度的P值(Pvalue): %.5f' % pvalue[1][0])
    print('降水的P值(Pvalue): %.5f' % pvalue[1][1])
    return r2score, ncoef, pvalue, reg.intercept_, func, z_pred


class para:
    xlabel_font = {'family': 'Times New Roman', 'size': 7}
    ylabel_font = {'family': 'Times New Roman', 'size': 7, 'horizontalalignment': 'left', 'rotation': 'horizontal'}
    ticks_fonts = {'family': 'Times New Roman', 'size': 9, 'rotation': 'horizontal'}
    ticks_font = 'Times New Roman'
    ticks_size = 7
    Legend_prop = {'family': 'Times New Roman', 'size': 7}

#================plot_line_见下=========================
def plot_line2(fig, i, name,y1,y2,y3,data):
    # fig = plt.figure(figsize=(3.5,2))  #figsize默认为4,4(图像尺寸),facecolor="blue"
    ax = fig.add_subplot(4,3,i+1)  #用[left, bottom, weight, height]的方式定义axes，0 <= l,b,w,h <= 1
    y_ce = y1.max()-y1.min()
    ymin = int((y1.min()-y_ce/10)*100)/100
    ymax = int((y1.max()+y_ce/10)*100)/100
    #    tpnp = np.r_[y2,y3]
    #    ymin = int(tpnp.min()*10)/10
    #    ymax = int(tpnp.max()*10)/10+0.1
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    # ax.set_xlabel('Change Value(Temperature and Precipitation)', para.xlabel_font)
    ax.set_ylabel('NDVI', fontdict=para.ylabel_font, y=1.05)
    for label in labels:
        label.set_fontname(para.ticks_font)
        label.set_size(para.ticks_size)
    #ax_ndvi.axis['left1'] = new_axisline(loc='left', axes=ax_ndvi, offset=offset1)
    #ax.axis['left'].set_axisline_style('->',size=2)  #轴的形状色
    # ax.axis['left'].line.set_linewidth(lineW)   #轴宽
    # ax.axis['bottom'].line.set_linewidth(lineW)   #轴宽
    # ax.set_xlabel('变量值（气温、降水）')
    # ax.set_ylabel('NDVI')
    
    # ax.xaxis.set_major_locator(xmajorLocator)    #设置主刻度标签的位置,没有标签文本格式ax.xaxis.set_major_formatter(FormatStrFormatter('%5.1f'))
    # ax.yaxis.set_major_locator(ymajorLocator)
    # ax.xaxis.set_minor_locator(xminorLocator)    #设置次刻度标签的位置,没有标签文本格式
    # ax.yaxis.set_minor_locator(yminorLocator)
    #    offset1 = xoffset
    #    offset2 = yoffset
    #    ax_.set_ylim(y1lim[0],y1lim[1])
    #    ax_p.set_ylim(y2lim[0],y2lim[1])
    
    #打开网格 略
    # fig.add_axes(ax)
    ax.minorticks_on()
    
    ax.scatter( y2,y1, label="Temperature", c=c1, marker=".")
    ax.scatter( y3,y1, label="Precipitation", c=c2, marker=".")
    xmajorLocator = MultipleLocator(1)  # 将x主刻度标签设置为20的倍数
    # xmajorFormatter = FormatStrFormatter('%5d')  # 设置x轴标签文本的格式
    ymajorLocator = MultipleLocator(0.02)  # 将y轴主刻度标签设置为0.5的倍数
    ymajorFormatter = FormatStrFormatter('%1.2f')  # 设置y轴标签文本的格式
    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    # ax.xaxis.set_major_formatter(xmajorFormatter)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)
#    ax_.scatter(y1, y3, label="降水", c=c2, marker=".")
#    p1, = ax.plot(y1, y2, label="NDVI", ls=linestyle, lw=lwidth, color=c1, marker=".", ms= marksize, mfc=c1)
    xminorLocator = MultipleLocator(0.5)  # 将x轴次刻度标签设置为5的倍数
    yminorLocator = MultipleLocator(0.01)  # 将此y轴次刻度标签设置为0.1的倍数
    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    
    estm1 = linear_model(y2.reshape(-1,1),y1,1)
    estm2 = linear_model(y3.reshape(-1,1),y1,1)
    print("\n\nThe linear model is:\n" +estm1[4])
    print('方程的判定系数(R^2): %.2f' %estm1[0])
    print('温度的P值(Pvalue): %.5f' %estm1[2])
    print("\nThe linear model is:\n" +estm2[4])
    print('方程的判定系数(R^2): %.2f' %estm2[0])
    print('降水的P值(Pvalue): %.5f' %estm2[2])
    
    #多元回归
    #错误函数estm3 = multi_linear(y1,y2,y3) 
    est=smf.ols(formula='y ~ T + P',data=data).fit()    #【est.summary()】【dir(est)】
    est.summary()
    estfunc = "NDVI = %.2f*T + %.2f*P + %.2f"  %(est.params[1],est.params[2],est.params[0])
    print(estfunc)
    
    
    p, =ax.plot(y2, estm1[5], color=c1, linewidth=0.7,ls='-')
    pp, =ax.plot(y3, estm2[5], color=c2, linewidth=0.7,ls='-')
    #ppp, =ax.plot(y3, estm3[5], color='black', linewidth=1,ls='--')
    #ax.set_xlabel('YEAR')
    #ax.set_ylabel('NDVI')
    # plt.legend(loc=1,bbox_to_anchor=legendp,prop=getChineseFont(8),ncol=1,frameon=False,mode='expend')
    ax.set_title(name, y=0.9, fontdict=para.ticks_fonts)
    #plt.savefig(r'F:\JJU_UP\Data\W_Study\投影寻踪【智慧城市】\Figure\20200926'+os.sep+name+r'.png', dpi=900, bbox_inches='tight')
    
    return [estm1[1][0],estm1[0],estm1[2][0],estm2[1][0],estm2[0],estm2[2][0],estfunc,est.rsquared,est.f_pvalue]

def Nominalize(tpdf):
    mn = tpdf.mean(axis=1)
    sd = tpdf.std(axis=1)
    tpdf = tpdf.sub(mn,axis=0).div(sd,axis=0)
    return tpdf
    
df = []
flist.sort()
for file_ in flist:
    df.append(pd.read_excel(file_,header=0,index_col =1))


df1 = df[0].iloc[:,6:16+1]
df2 = df[2].iloc[:,6:16+1]  #气温
df3 = df[1].iloc[:,6:16+1]  #降水
df2 = Nominalize(df2)
df3 = Nominalize(df3)
outcome = pd.DataFrame([])
fig = plt.figure(figsize=[19/2.54, 19/2.54])
for i in range(0,len(df[0].index)):
    name = df1.index[i]
#    x = np.arange(2005,2015+1)
#    y11 = df1.iloc[i,:]
    y1 = df1.iloc[i,:]
    y2 = df2.iloc[i,:]
    y3 = df3.iloc[i,:]
    data = pd.DataFrame([y1,y2,y3]).T
    data.columns = ['y','T','P']
    y2 = y2.values
    y3 = y3.values
    out = pd.DataFrame(plot_line2(fig, i, name, y1, y2, y3,data)).T# Name，NDVI，气温，降水
    out.index = [name]
    outcome=outcome.append(out,ignore_index=True)
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=legendp, prop=para.Legend_prop,ncol=1,frameon=False,mode='expend')
# fig.text(0.35, 0.05, 'Standardization of temperature and precipitation', va='center', fontdict=para.xlabel_font)
fig.show()
plt.subplots_adjust(wspace=0.2, hspace=0.3, left=0.08)
fig.savefig('F:/temp.tif', dpi=1000)
outcome.columns = ['一元T系数','一元T R²','一元T p值','一元P系数','一元P R²','一元P p值','多元回归方程','多元 R²','多元 p值']
outcome.index = df1.index
# outcome.to_excel(r'F:\JJU_UP\Data\W_Study\投影寻踪【智慧城市】\Figure\20200926\一+二元回归结果.xlsx')
print(outcome)
