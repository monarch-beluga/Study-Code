# -*- coding: utf-8 -*-
# @Time    : 2024/1/2 23:58
# @Author  : Monarch
# @File    : linear_regression.py
# @Software: PyCharm

import numpy as np
from utils.prepare_for_training import prepare_for_training


class LinearRegression:
    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        """
        模型初始化
        :param data: 特征值数据
        :param labels: 目标值数据
        :param prepare: 是否进行预处理
        :param polynomial_degree:
        :param sinusoid_degree:
        :param normalize_data:
        """
        # 预处理
        data_processed = data
        features_mean = 0
        features_deviation = 0

        (data_processed,
         features_mean,
         features_deviation) = prepare_for_training(data, polynomial_degree, sinusoid_degree, normalize_data)
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

    def train(self, alpha, num_iterations=500):
        """
        训练主函数, 执行梯度下降
        :param alpha: 学习率
        :param num_iterations: 迭代次数
        :return: 最终参数,损失值变化
        """
        cost_history = self.gradient_descent(alpha, num_iterations)
        return self.theta, cost_history

    def gradient_descent(self, alpha, num_iterations):
        """
        梯度下降，实际计算函数
        :param alpha: 学习率
        :param num_iterations: 迭代次数
        :return: 损失值变化
        """
        cost_history = []
        for _ in range(num_iterations):
            self.gradient_step(alpha)
            cost_history.append(self.cost_function(self.data, self.labels))
        return cost_history

    def gradient_step(self, alpha):
        """
        参数更新
        :param alpha: 学习率
        """
        # 批处理数量
        num_examples = self.data.shape[0]
        # 预测值计算
        prediction = LinearRegression.hypothesis(self.data, self.theta)
        # 计算真实值与预测值之差
        delta = prediction - self.labels
        # 计算更新参数
        theta = self.theta
        theta -= alpha * (1 / num_examples) * (np.dot(delta.T, self.data)).T
        self.theta = theta

    def cost_function(self, data, labels):
        """
        损失函数
        :param data: 特征值数据
        :param labels: 目标值数据
        :return: 损失值
        """
        num_examples = data.shape[0]
        prediction = LinearRegression.hypothesis(data, self.theta)
        delta = prediction - labels
        # 最小二乘法损失函数
        cost = (1 / 2) * np.dot(delta.T, delta) / num_examples
        return cost[0][0]

    @staticmethod
    def hypothesis(data, theta):
        """
        当前预测值计算
        :param data: 特征值数据
        :param theta: 参数
        :return: 预测值
        """
        predictions = np.dot(data, theta)
        return predictions

    def get_cost(self, data, labels):
        data_processed = prepare_for_training(data,
                                              self.polynomial_degree,
                                              self.sinusoid_degree,
                                              self.normalize_data)[0]
        return self.cost_function(data_processed, labels)

    def predict(self, data):
        """
        用训练好的模型去得到回归值结果
        :param data: 特征值数据
        :return: 回归值
        """

        data_processed = prepare_for_training(data,
                                              self.polynomial_degree,
                                              self.sinusoid_degree,
                                              self.normalize_data)[0]
        predictions = LinearRegression.hypothesis(data_processed, self.theta)
        return predictions

