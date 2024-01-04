# -*- coding: utf-8 -*-
# @Time    : 2024/1/4 10:43
# @Author  : Monarch
# @File    : generate_polynomials.py
# @Software: PyCharm

from utils.standardization import standardization
import numpy as np


def generate_polynomials(dataset, polynomial_degree, normalize_data=False):
    """
    变换方法
    :param dataset: 特征数据
    :param polynomial_degree: 变换角度
    :param normalize_data: 是否标准化
    :return: 变换后的数据
    """
    features_split = np.array_split(dataset, 2, axis=1)
    dataset_1 = features_split[0]
    dataset_2 = features_split[1]

    num_examples_1, num_features_1 = dataset_1.shape
    num_examples_2, num_features_2 = dataset_2.shape

    if num_examples_1 != num_examples_2:
        raise ValueError('Can not generate polynomials for two sets with different number of row')

    if num_features_1 == 0 and num_features_2 == 0:
        raise ValueError('Can not generate polynomials for two sets with no columns')

    if num_features_1 == 0:
        dataset_1 = dataset_2
    elif num_features_2 == 0:
        dataset_2 = dataset_1

    num_features = num_features_1 if num_features_1 < num_examples_2 else num_features_2
    dataset_1 = dataset_1[:, :num_features]
    dataset_2 = dataset_2[:, :num_features]

    polynomials = np.empty((num_examples_1, 0))

    for i in range(1, polynomial_degree+1):
        for j in range(i+1):
            polynomial_feature = (dataset_1 ** (i - j)) * (dataset_2 ** j)
            polynomials = np.concatenate((polynomials, polynomial_feature), axis=1)

    if normalize_data:
        polynomials = standardization(polynomials)[0]

    return polynomials
