# -*- coding: utf-8 -*-
# @Time    : 2024/1/5 14:46
# @Author  : Monarch
# @File    : Non-linearRegression.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from linear_regression import LinearRegression

data = pd.read_csv('../data/non-linear-regression-x-y.csv')

x = data['x'].values.reshape((data.shape[0], 1))
y = data['y'].values.reshape((data.shape[0], 1))

plt.plot(x, y)
plt.show()

# 非线性回归就需要用到 polynomial 和 sinusoid 变换
# polynomial_degree 和 sinusoid_degree大小的选择一般是不确定的，
# 要通过不断调试，来得到一个好的值，太小会欠拟合，太大又容易过拟合
num_iterations = 50000
learning_rate = 0.02
polynomial_degree = 15
sinusoid_degree = 15
normalize_data = True

linear_regression = LinearRegression(x, y, polynomial_degree, sinusoid_degree, normalize_data)

theta, cost_history = linear_regression.train(learning_rate, num_iterations)

print('开始损失: {:.2f}'.format(cost_history[0]))
print('结束损失: {:.2f}'.format(cost_history[-1]))

plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Gradient Descent Progress')
plt.show()

predictions_num = 1000
x_predictions = np.linspace(x.min(), x.max(), predictions_num).reshape(predictions_num, 1);
y_predictions = linear_regression.predict(x_predictions)

plt.plot(x, y, label='Training Dataset')
plt.plot(x_predictions, y_predictions, 'r', label='Prediction')
plt.show()

