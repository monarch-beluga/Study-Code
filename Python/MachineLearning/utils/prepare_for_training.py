# -*- coding: utf-8 -*-
# @Time    : 2024/1/3 11:42
# @Author  : Monarch
# @File    : prepare_for_training.py
# @Software: PyCharm

import numpy as np
from utils.standardization import standardization


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

    # 加一列1
    data_processed = np.hstack((np.ones((num_examples, 1)), data_processed))

    return data_processed, features_mean, features_deviation

