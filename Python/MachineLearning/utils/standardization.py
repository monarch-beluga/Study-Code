# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 11:19
# @Author  : Monarch
# @File    : standardization.py
# @Software: PyCharm

import numpy as np


def standardization(features):
    """
    特征数据标准化
    :param features: 特征值数据
    :return:
    """
    features_normalized = np.copy(features).astype('float')

    # 计算均值
    features_mean = np.mean(features, 0)

    # 计算标准差
    features_deviation = np.std(features, 0)

    # 标准化操作
    if features.shape[0] > 1:
        features_normalized -= features_mean

    # 防止除以0
    features_deviation[features_deviation == 0] = 1
    features_normalized /= features_deviation

    return features_normalized, features_mean, features_deviation



