# -*- coding: utf-8 -*-
# @Time    : 2025/4/8 上午10:09
# @Author  : Monarch
# @File    : LandscapePI.py
# @Software: PyCharm

import os
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

os.chdir(r'D:\Work\景观格局指标对PM2.5影响')

df = pd.read_excel("样本数据.xlsx", header=1, index_col=0)
dataset = fetch_california_housing()

