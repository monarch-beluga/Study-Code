# -*- coding: utf-8 -*-
# @Time    : 2025/8/24 下午2:39
# @Author  : Monarch
# @File    : 应急物资模板处理.py
# @Software: PyCharm
import os
import pandas as pd

os.chdir(r"D:\Work\pxvr\湘东工业园区VR数据表格-25.9.12")

in_file1 = r"04-园区应急物资导入模板.xls"
in_file2 = r"06-企业应急物资导入模板.xls"
out_file = r'yjwz.json'

df = pd.read_excel(in_file1)
df1 = pd.read_excel(in_file2)
df = pd.concat([df, df1])
ds = {
    "firmName": "企业名称*",
    "materialName": "应急物资名称*",
    "materialAddress": "存储位置",
    "quantity": "数量/单位"
}
df2 = pd.DataFrame()

for i in ds:
    df2[i] = df[ds[i]]

# df2.to_json(out_file, indent=2, orient='records', force_ascii=False)

