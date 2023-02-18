# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/05
@file: 最小二乘法.py
@function:
@modify:
"""
# 目标函数
import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def real_func(x):
    return np.sin(2*np.pi*x)

# 多项式
# ps: numpy.poly1d([1,2,3])  生成  $1x^2+2x^1+3x^0$*
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)

# 残差
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret

regularization = 0.0001

def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    ret = np.append(ret, np.sqrt(0.5*regularization*np.square(p))) # L2范数作为正则化项
    return ret

# 十个点
x = np.linspace(0, 1, 10)
x_points = np.linspace(0, 1, 1000)
# 加上正态分布噪音的目标函数的值
y_ = real_func(x)
y = [np.random.normal(0, 0.1)+y1 for y1 in y_]

def fitting(M=0):
    """
    n 为 多项式的次数
    """
    # 随机初始化多项式参数
    p_init = np.random.rand(M+1)
    # 最小二乘法
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    print('Fitting Parameters:', p_lsq[0])
    p_lsq_regularization = leastsq(residuals_func_regularization, p_init, args=(x, y))

    # 可视化
    plt.plot(x_points, real_func(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq_regularization[0], x_points), label='regularization')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    return p_lsq


'''
# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/05
@file: drive.py
@function:
@modify:
"""


import numpy as np
import scipy as sp
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

x_points = np.linspace(0, 44, 1000)


# 多项式
# ps: numpy.poly1d([1,2,3])  生成  $1x^2+2x^1+3x^0$*
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)


regularization = 0.0001


def residuals_func_regularization(p, x, y):
    ret = fit_func(p, x) - y
    ret = np.append(ret, np.sqrt(0.5*regularization*np.square(p)))  # L2范数作为正则化项
    return ret


# 残差
def residuals_func(p, x, y):
    ret = fit_func(p, x) - y
    return ret


def fitting(x, y, M=0):
    """
    n 为 多项式的次数
    """
    # 随机初始化多项式参数
    p_init = np.random.rand(M+1)
    # 最小二乘法
    p_lsq = leastsq(residuals_func, p_init, args=(x, y))
    p_lsq_regularization = leastsq(residuals_func_regularization, p_init, args=(x, y))
    print('Fitting Parameters:', p_lsq[0])

    # 可视化
    # plt.plot(x_points, real_func(x_points), label='real')
    plt.plot(x_points, fit_func(p_lsq[0], x_points), label='fitted curve')
    plt.plot(x_points, fit_func(p_lsq_regularization[0], x_points), label='regularization')
    plt.plot(x, y, 'bo', label='noise')
    plt.legend()
    return p_lsq


file = r'E:\Data\temp\temp.txt'
with open(file) as fp:
    data = fp.readlines()

data = [i.split() for i in data]
df = np.array(data)
df = df.astype('float')
df = df[:, 4:-1]
dx = np.array(list(range(0, 46, 2)))


'''
