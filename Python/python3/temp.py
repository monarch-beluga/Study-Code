# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import numpy as np

X = np.array([[-1, 1, 3],
              [-2, -1, 2],
              [-3, -2, 4],
              [1, 1, 2],
              [2, 1, 3],
              [3, 2, 2]])

mean = X.mean(axis=0)
norm_X = X - mean

covariance_matrix = np.cov(norm_X.T)

eig_val, eig_vec = np.linalg.eig(covariance_matrix)
eig_pairs = [i for i in zip(np.abs(eig_val), eig_vec.T)]

eig_pairs.sort(reverse=True)

feature = np.array([ele[1] for ele in eig_pairs])

data_X = np.dot(norm_X, feature.T)

