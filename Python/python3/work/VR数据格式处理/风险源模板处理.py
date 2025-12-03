# -*- coding: utf-8 -*-
# @Time    : 2025/8/24 下午3:47
# @Author  : Monarch
# @File    : 风险源模板处理.py
# @Software: PyCharm

import os
import pandas as pd

os.chdir(r"D:\Work\pxvr\湘东工业园区VR数据表格-25.9.12")

in_file = r'01-企业风险源导入模板.xls'
addr_file = r'02-企业信息导入模板.xls'
out_file = r'rs.json'

df = pd.read_excel(in_file, sheet_name="Sheet2", index_col=1)
df1 = pd.read_excel(addr_file, index_col=0)
df2 = pd.concat([df1, df], axis=1)
df3 = df2[['经度', '纬度', '合成材料制造', '风险源名称*', "环境风险等级"]]
df3.reset_index(inplace=True)
columns = ['name', 'lon', 'lat', 'materialName', "riskSourcesName", "riskLevel"]
df3.columns = columns
df4 = df3.loc[~df3['riskLevel'].isna(), :].reset_index(drop=True)
df4['riskLevel'] = df4['riskLevel'].str[:2]
df4.loc[~df4['riskLevel'].isin(['一般', '较大']), 'riskLevel'] = "其他"
df4.to_json(out_file, indent=2, orient='records', force_ascii=False)

series1 = df4['riskLevel'].value_counts()
df5 = pd.DataFrame({'name': series1.index, "value": series1.values})
df5.to_json("rs_StatisticData.json", indent=2, orient='records', force_ascii=False)



