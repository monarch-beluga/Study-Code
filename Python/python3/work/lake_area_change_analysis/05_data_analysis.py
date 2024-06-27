# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 14:27
# @Author  : Monarch
# @File    : 05_data_analysis.py
# @Software: PyCharm

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
import pandas as pd
import os
import numpy as np


def normalization(data):
    _range = np.max(data, axis=0) - np.min(data, axis=0)
    return (data - np.min(data, axis=0)) / _range


path = r'D:\Work\LakeAreaChanges'
os.chdir(path)
out_path = "csv_data"
if not os.path.exists(out_path):
    os.mkdir(out_path)

# lakes = ['太湖', '梁子湖', '洞庭湖', '洪泽湖', '鄱阳湖', "巢湖"]
lakes = ['鄱阳湖']
index = ["TAVG", "PRCP", 'pop', 'gdp']

for lake in lakes:
    file = f'csv_data/{lake}_statistic.csv'
    df = pd.DataFrame()
    lake_data = pd.read_csv(file, encoding='gbk', index_col=0)
    X = lake_data[index].values
    X_nor = normalization(X)
    y = lake_data['area'].values

    lin_reg = LinearRegression()
    lin_reg.fit(X_nor, y)
    weight = lin_reg.coef_
    df['weight'] = weight
    p_value = f_regression(X, y)[1]
    df['p_value'] = p_value
    df.index = index
    df.to_csv(f"{out_path}/{lake}_driving_force.csv", encoding="gbk")


