# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 11:42
# @Author  : Monarch
# @File    : prepare_for_training.py
# @Software: PyCharm

import numpy as np
from utils.standardization import standardization
from utils.generate_sinusoids import generate_sinusoids
from utils.generate_polynomials import generate_polynomials


def prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data):

    # 获取样本总数
    num_examples = data.shape[0]

    data_processed = np.copy(data)

    # 标准化预处理
    features_mean = 0
    features_deviation = 0
    data_normalized = data_processed
    if normalize_data:
        data_normalized, features_mean, features_deviation = standardization(data_processed)

        data_processed = data_normalized

    # 特征变换sinusoidal
    if sinusoid_degree > 0:
        sinusoids = generate_sinusoids(data_normalized, sinusoid_degree)
        data_processed = np.concatenate((data_processed, sinusoids), axis=1)

    # 特征变换polynomial
    if polynomial_degree > 0:
        polynomials = generate_polynomials(data_normalized, polynomial_degree, normalize_data)
        data_processed = np.concatenate((data_processed, polynomials), axis=1)

    # 加一列1
    data_processed = np.hstack((np.ones((num_examples, 1)), data_processed))

    return data_processed, features_mean, features_deviation

