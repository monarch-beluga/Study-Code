# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 15:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
import scipy.stats as st


data = pd.read_csv("data/world-happiness-report-2017.csv")

# 得到训练和测试数据
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

input_param_name = 'Economy..GDP.per.Capita.'
output_param_name = 'Happiness.Score'

# 获取训练数据的特征值和目标值
x_train = train_data[[input_param_name]].values
y_train = train_data[[output_param_name]].values

# 获取测试数据的特征值和目标值
x_test = test_data[[input_param_name]].values
y_test = test_data[[output_param_name]].values

# plt.scatter(x_train, y_train, label='Train data')
# plt.scatter(x_test, y_test, label='Test data')
# plt.xlabel(input_param_name)
# plt.ylabel(output_param_name)
# plt.title('City happiness')
# plt.legend()
# plt.show()

regr = LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_train)

slope = regr.coef_[0]
intercept = regr.intercept_[0]
predictions_num = 100
x_predictions = np.linspace(x_train.min(), x_train.max(), predictions_num).reshape(-1, 1)
y_predictions = regr.predict(x_predictions)

# plt.scatter(x_train, y_train, label='Train data')
# plt.scatter(x_test, y_test, label='Test data')
# plt.plot(x_predictions, y_predictions, 'r', label='Prediction')
# plt.xlabel(input_param_name)
# plt.ylabel(output_param_name)
# plt.title('City happiness')
# plt.legend()
# plt.show()

num_examples = x_train.shape[0]
delta = y_pred - y_train
cost = (1 / 2) * np.dot(delta.T, delta) / num_examples
print('最后的损失值：', cost[0][0])



