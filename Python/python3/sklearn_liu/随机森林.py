# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/12/30
@file: 随机森林.py
@function:
@modify:
"""

import pandas as pd
import os
from scipy_liu.IDW import Invdisttree
from sklearn.ensemble import RandomForestRegressor
import numpy as np

os.chdir(r'E:\Work\Estimation')
df = pd.read_excel('2_土壤碳密度信息.xlsx', sheet_name='开垦对碳密度的影响', usecols='E,F,CH,CQ,CV')
df.columns = ['Lat', 'Lon', 'Soil_layer', 'Mean_SOC_Tr', 'Mean_BD_Tr']
df = df.iloc[4:, :]
# df1 = df[~df['Lat'].isna()]
df = df[~((df['Mean_SOC_Tr'] == '/') | (df['Mean_SOC_Tr'].isna() & df['Lat'].isna()))]
df2 = df[~df['Lat'].isna()]
df3 = df2.drop_duplicates(subset=['Lat', 'Lon'], keep='first')[['Lat', 'Lon', 'Mean_SOC_Tr']]
df4 = df3[~df3['Mean_SOC_Tr'].isna()]
X = df4.iloc[:, :2].values
z = df4['Mean_SOC_Tr'].values
q = df3[df3['Mean_SOC_Tr'].isna()].iloc[:, :2].values
invdisttree = Invdisttree(X, z)
idw_soc = invdisttree.__call__(q, nnear=12)
df.loc[(~df['Lat'].isna()) & (df['Mean_SOC_Tr'].isna()), 'Soil_layer'] = '0-20'
df.loc[(~df['Lat'].isna()) & (df['Mean_SOC_Tr'].isna()), 'Mean_SOC_Tr'] = idw_soc
df['Lat'] = df['Lat'].fillna(method='ffill')
df['Lon'] = df['Lon'].fillna(method='ffill')
s_l = df['Soil_layer'].str.split('-')
df.insert(3, 'Soil_layer_min', s_l.str[0].astype(int))
df.insert(4, 'Soil_layer_max', s_l.str[1].astype(int))
df.drop(columns='Soil_layer', inplace=True)
data_train = df[~df['Mean_BD_Tr'].isna()]
data = df[df['Mean_BD_Tr'].isna()]
x_train = data_train.iloc[:, 2:5].values
y_train = data_train.iloc[:, 5].values
x = data.iloc[:, 2:5].values
regressor = RandomForestRegressor(n_estimators=200, random_state=0)
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x)
df.loc[df['Mean_BD_Tr'].isna(), 'Mean_BD_Tr'] = y_pred
df.to_excel('Mean_Bd.xlsx')

"""
import pandas as pd
import os
# from scipy_liu.IDW import Invdisttree
from sklearn.ensemble import RandomForestRegressor
import xlwings as xw


def sp(x):
    if type(x) is str:
        x1 = x.split('-')
        return (float(x1[0]) + float(x1[1])) / 2
    else:
        return x


os.chdir(r'E:\Work\Estimation\土壤碳密度信息')
path = 'r_土壤碳密度信息_r.xls'
app = xw.App(visible=False, add_book=False)
app.display_alerts = False
app.screen_updating = False  # 是否实时刷新excel程序的显示内容
wb = app.books.open(path)
ws = wb.sheets[0]
df_all = pd.read_excel('r_土壤碳密度信息.xls', sheet_name='Sheet1',
                   usecols='G,H,V,AK,AR,AT,CJ,CQ,CS,CX,DJ,DK,DL,DM,DN,DO,DP,DQ,AY')

# df1 = pd.read_excel('r_土壤碳密度信息.xlsx', sheet_name='Sheet1', usecols='')
a = df_all.columns
df_all.columns = 'G,H,V,AK,AR,AT,AY,CJ,CQ,CS,CX,DJ,DK,DL,DM,DN,DO,DP,DQ'.split(',')
df_all['V'] = df_all['V'].fillna(method='ffill')
df_all['V'] = df_all['V'].apply(sp)
df1 = df_all['G,H,V,AK,AR,AT,DJ,DK,DL,DM,DN,DO,DP,DQ,AY'.split(',')]
df1.index = 'AY'+(df1.index+2).astype('str')
df2 = df_all['G,H,V,CJ,CQ,CS,DJ,DK,DL,DM,DN,DO,DP,DQ,CX'.split(',')]
df2.index = 'CX'+(df2.index+2).astype('str')
df2 = df2.rename(columns={'CJ': 'AK', 'CQ': 'AR', 'CS': 'AT', 'CX': 'AY'})
df = pd.concat([df1, df2])
df = df[(df['AR'] == '%') | (df['AR'] == 'g/kg')]
# df = df1['G,H,V,AK,AT,DJ,DK,DL,DM,DN,DO,DP,DQ,AY'.split(',')]
df = df[~df['AK'].isna()]
df = df[~(df['AT'] == '/')]
df.loc[df['AR'] == 'g/kg', 'AT'] = df.loc[df['AR'] == 'g/kg', 'AT'] / 10
# df[df['AR'] == 'g/kg']['AK'] = df[df['AR'] == 'g/kg']['AK']*10
# df = df.iloc[4:, :]
# df1 = df[~df['Lat'].isna()]
# df = df[~((df['Mean_SOC_Tr'] == '/') | (df['Mean_SOC_Tr'].isna() & df['Lat'].isna()))]
# df2 = df[~df['Lat'].isna()]
# df3 = df2.drop_duplicates(subset=['Lat', 'Lon'], keep='first')[['Lat', 'Lon', 'Mean_SOC_Tr']]
# df4 = df3[~df3['Mean_SOC_Tr'].isna()]
# X = df4.iloc[:, :2].values
# z = df4['Mean_SOC_Tr'].values
# q = df3[df3['Mean_SOC_Tr'].isna()].iloc[:, :2].values
# invdisttree = Invdisttree(X, z)
# idw_soc = invdisttree.__call__(q, nnear=12)
# df.loc[(~df['Lat'].isna()) & (df['Mean_SOC_Tr'].isna()), 'Soil_layer'] = '0-20'
# df.loc[(~df['Lat'].isna()) & (df['Mean_SOC_Tr'].isna()), 'Mean_SOC_Tr'] = idw_soc
# df['Lat'] = df['Lat'].fillna(method='ffill')
# df['Lon'] = df['Lon'].fillna(method='ffill')
s_l = df['AK'].str.split('-')
df.insert(3, 'Soil_layer_min', s_l.str[0].astype(int))
df.insert(4, 'Soil_layer_max', s_l.str[1].astype(int))
df.drop(columns=['AK', 'AR'], inplace=True)
data_train = df[~df['AY'].isna()]
x_train = data_train.iloc[:, 2:14].values
y_train = data_train.iloc[:, 14].values
regressor = RandomForestRegressor(n_estimators=200, random_state=0)
regressor.fit(x_train, y_train)
data = df[df['AY'].isna()]
x = data.iloc[:, 2:14].values
y_pred = regressor.predict(x)
for j, i in enumerate(data.index):
    ws.range(f'{i}').value = y_pred[j]
wb.save()
wb.close()
app.quit()
# df.columns = ['Lat', 'Lon', 'Soil_layer_min', 'Soil_layer_max', 'Mean_SOC_Tr'] + a[5:].to_list() + ['Mean_BD_Tr']
# df.to_excel('Mean_Bd.xlsx')
"""
