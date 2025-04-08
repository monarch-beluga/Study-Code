# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import pandas as pd

os.chdir(r"D:\Work\安义数据采集\安义化工集中区VR数据采集")

in_file = r"安义化工集中区-救援队伍信息导入模板.xls"
df = pd.read_excel(in_file)
ds = {
    "firmName": "企业名称",
    "responsiblePersonName": "负责人",
    "contactNumber": "负责人电话",
    "responsiblePersonName2": "负责人2",
    "contactNumber2": "负责人电话2",
}
df2 = df.loc[df['类型'] == '企业', :]
df1 = pd.DataFrame()
for i in ds:
    df1[i] = df2[ds[i]]
df1.to_json("anyi_qyjy.json", indent=2, orient='records', force_ascii=False)


