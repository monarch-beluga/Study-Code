import os
import pandas as pd
from simpledbf import Dbf5
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc("font", family='KaiTi')

f_dbf = r'F:\文件\工作\CMKY\安远县土地利用.dbf'
table = Dbf5(f_dbf, codec='gbk')
df = table.to_dataframe()
df1 = df[["TDLYMC", "AREA"]].groupby("TDLYMC").sum()
filepath = r'F:\文件\工作\CMKY\土地利用类型编码说明及配色表.xlsx'
data_frame = pd.read_excel(filepath, index_col=0) / 100
# df2 = data_frame.drop(0, axis=1)
# df3 = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
df3 = pd.merge(df1, data_frame, how="left", left_index=True, right_index=True)
del df3['代码']
s = df3['AREA'].sum()
df3['AREA'] = df3['AREA'] / s
RGB = []
for i, j in enumerate(df3.index):
    rgb = [(1 - df3['C'][i] * (1 - df3['K'][i])), (1 - df3["M"][i] * (1 - df3['K'][i])), (1 - df3['Y'][i] * (1 - df3['K'][i]))]
    RGB.append(rgb)
fig = plt.figure()
plt.pie(df3['AREA'], labels=df3.index, colors=RGB)


