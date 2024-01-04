# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 9:25
# @Author  : Monarch
# @File    : MultivariateLinearRegression.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go

from linear_regression import LinearRegression
plotly.offline.init_notebook_mode()

data = pd.read_csv("../data/world-happiness-report-2017.csv")

# 得到训练和测试数据
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

input_param_name_1 = 'Economy..GDP.per.Capita.'
input_param_name_2 = 'Freedom'
output_param_name = 'Happiness.Score'

# 获取训练数据的特征值和目标值
x_train = train_data[[input_param_name_1, input_param_name_2]].values
y_train = train_data[[output_param_name]].values

# 获取测试数据的特征值和目标值
x_test = test_data[[input_param_name_1, input_param_name_2]].values
y_test = test_data[[output_param_name]].values

# 绘制三维数据点
plot_training_trace = go.Scatter3d(
    x=x_train[:, 0],
    y=x_train[:, 1],
    z=y_train[:, 0],
    name='Training Set',
    mode='markers',
    marker={
        'size': 10,
        'opacity': 1,
        'line': {
            'color': 'rgb(255, 255, 255)',
            'width': 1
        },
    }
)

plot_test_trace = go.Scatter3d(
    x=x_test[:, 0],
    y=x_test[:, 1],
    z=y_test[:, 0],
    name='Training Set',
    mode='markers',
    marker={
        'size': 10,
        'opacity': 1,
        'line': {
            'color': 'rgb(255, 255, 255)',
            'width': 1
        },
    }
)

plot_layout = go.Layout(
    title='Date Sets',
    scene={
        'xaxis': {'title': input_param_name_1},
        'yaxis': {'title': input_param_name_2},
        'zaxis': {'title': output_param_name}
    },
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0}
)
plot_data = [plot_training_trace, plot_test_trace]

plot_figure = go.Figure(data=plot_data, layout=plot_layout)

plotly.offline.plot(plot_figure)

num_iterations = 500
learning_rate = 0.01

linear_regression = LinearRegression(x_train, y_train)
theta, cost_history = linear_regression.train(learning_rate, num_iterations)

print('开始时的损失：', cost_history[0])
print('训练后的损失：', cost_history[-1])

plt.plot(range(num_iterations), cost_history)
plt.xlabel('Iter')
plt.ylabel('cost')
plt.title('GD')
plt.show()

predictions_num = 10
x_axis = np.linspace(x_train[:, 0].min(), x_train[:, 0].max(), predictions_num)
y_axis = np.linspace(x_train[:, 1].min(), x_train[:, 1].max(), predictions_num)
x_predictions, y_predictions = np.meshgrid(x_axis, y_axis)
x_predictions = x_predictions.reshape(-1, 1)
y_predictions = y_predictions.reshape(-1, 1)

z_predictions = linear_regression.predict(np.hstack((x_predictions, y_predictions)))

plot_predictions_trace = go.Scatter3d(
    x=x_predictions[:, 0],
    y=y_predictions[:, 0],
    z=z_predictions[:, 0],
    name='Prediction Plane',
    mode='markers',
    marker={
        'size': 1,
    },
    opacity=0.8,
    surfaceaxis=2,
)

plot_data = [plot_training_trace, plot_test_trace, plot_predictions_trace]
plot_figure = go.Figure(data=plot_data, layout=plot_layout)
plotly.offline.plot(plot_figure)

