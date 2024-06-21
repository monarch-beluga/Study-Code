# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 10:00
# @Author  : Monarch
# @File    : sigmoid.py
# @Software: PyCharm

import numpy as np


def sigmoid(matrix):
    """Applies sigmoid function to NumPy matrix"""

    return 1 / (1 + np.exp(-matrix))


def sigmoid_gradient(matrix):
    """Computes the gradient of the sigmoid function evaluated at z."""

    return sigmoid(matrix) * (1 - sigmoid(matrix))
