# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 23:58
# @Author  : Monarch
# @File    : linear_regression.py
# @Software: PyCharm

import numpy as np


def prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data):

    data_processed = data
    features_mean = 0
    features_deviation = 0
    return data_processed, features_mean, features_deviation


class LinearRegression:
    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):

        # 预处理
        (data_processed, features_mean, features_deviation) = prepare_for_training(data, polynomial_degree,
                                                                                   sinusoid_degree, normalize_data)
        # 预处理后数据
        self.data = data_processed
        # 目标
        self.labels = labels
        # 数据平均值
        self.features_mean = features_mean
        # 数据标准差
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        # 数据列数
        num_features = self.data.shape[1]
        # 初始化参数矩阵
        self.theta = np.zeros((num_features, 1))

