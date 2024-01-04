# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 11:08
# @Author  : Monarch
# @File    : generate_sinusoids.py
# @Software: PyCharm

import numpy as np


def generate_sinusoids(dataset, sinusoid_degree):
    """
    sin函数变换
    :param dataset: 特征数据
    :param sinusoid_degree: 变换角度
    :return: 变换后的数据
    """
    num_examples = dataset.shape[0]
    sinusoids = np.empty((num_examples, 0))

    for degree in range(1, sinusoid_degree+1):
        sinusoid_features = np.sin(degree * dataset)
        sinusoids = np.concatenate((sinusoids, sinusoid_features), axis=1)

    return sinusoids
