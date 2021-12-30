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

