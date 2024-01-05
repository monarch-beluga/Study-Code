# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 15:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from LinearRegression.linear_regression import LinearRegression

data = pd.read_csv("data/world-happiness-report-2017.csv")

# 得到训练和测试数据
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

# 使用两列数据作为输入的特征数据
input_param_names = ['Economy..GDP.per.Capita.', 'Family', 'Health..Life.Expectancy.', 'Freedom', 'Generosity',
                     'Trust..Government.Corruption.', 'Dystopia.Residual']
output_param_name = 'Happiness.Score'

# 获取训练数据的特征值和目标值
x_train = train_data[input_param_names].values
y_train = train_data[[output_param_name]].values

# 获取测试数据的特征值和目标值
x_test = test_data[input_param_names].values
y_test = test_data[[output_param_name]].values

num_iterations = 500
learning_rate = 0.01

#  模型训练
linear_regression = LinearRegression(x_train, y_train)
theta, cost_history = linear_regression.train(learning_rate, num_iterations)

print('开始时的损失：', cost_history[0])
print('训练后的损失：', cost_history[-1])

plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iter')
plt.ylabel('cost')
plt.title('GD')
plt.show()





