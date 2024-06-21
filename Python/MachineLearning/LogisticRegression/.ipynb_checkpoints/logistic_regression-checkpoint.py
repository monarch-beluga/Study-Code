# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 9:56
# @Author  : Monarch
# @File    : logistic_regression.py
# @Software: PyCharm

import numpy as np
from utils.prepare_for_training import prepare_for_training
from utils.sigmoid import sigmoid, sigmoid_gradient


class LogisticRegression:
    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True):
        """
        模型初始化
        :param data: 特征值数据
        :param labels: 目标值数据
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
        # 目标值类别
        self.unique_labels = np.unique(labels)
        # 数据平均值
        self.features_mean = features_mean
        # 数据标准差
        self.features_deviation = features_deviation
        self.polynomial_degree = polynomial_degree
        self.sinusoid_degree = sinusoid_degree
        self.normalize_data = normalize_data

        # 特征数
        num_features = self.data.shape[1]
        # 类别数
        num_class = self.unique_labels.shape[0]
        # 初始化参数矩阵
        self.theta = np.zeros((num_class, num_features))

    def train(self, alpha, num_iterations=500):
        """
        训练主函数, 执行梯度下降
        :param alpha: 学习率
        :param num_iterations: 迭代次数
        :return: 最终参数,损失值变化
        """
        cost_histories = []
        num_features = self.data.shape[1]
        num_class = self.unique_labels.shape[0]
        for index, label in enumerate(self.unique_labels):
            theta = np.copy(self.theta[index].reshape(num_features, 1))
            labels = (self.labels == label).astype(float)
            (theta, cost_history) = self.gradient_descent(alpha, num_iterations, labels, theta)
            self.theta[index] = theta.T
            cost_histories.append(cost_history)
        return self.theta, cost_histories

    def gradient_descent(self, alpha, num_iterations, labels, theta):
        cost_history = []
        for _ in range(num_iterations):
            theta = self.gradient_step(alpha, theta, labels)
            cost_history.append(self.cost_function(self.data, labels, theta))
        return theta, cost_history

    def gradient_step(self, alpha, theta, labels):
        """
        参数更新
        :param alpha: 学习率
        :param theta:
        :param labels:
        :return:
        """
        # 批处理数量
        num_examples = self.data.shape[0]
        # 预测值计算
        prediction = sigmoid(np.dot(self.data, theta))
        # 计算真实值与预测值之差
        delta = prediction - labels
        # 计算更新参数
        theta -= alpha * (1 / num_examples) * np.dot(self.data.T, delta)
        return theta

    def predict(self, data):
        num_examples = data.shape[0]
        data_processed = prepare_for_training(data, self.polynomial_degree, self.sinusoid_degree, self.normalize_data)[
            0]
        prob = sigmoid(np.dot(data_processed, self.theta.T))
        max_prob_index = np.argmax(prob, axis=1)
        class_prediction = np.empty(max_prob_index.shape, dtype=object)
        for index, label in enumerate(self.unique_labels):
            class_prediction[max_prob_index == index] = label
        return class_prediction.reshape((num_examples, 1))

    @staticmethod
    def cost_function(data, labels, theta):
        """
        损失函数
        :param data: 特征值数据
        :param labels: 目标值数据
        :param theta
        :return: 损失值
        """
        num_examples = data.shape[0]
        prediction = sigmoid(np.dot(data, theta))
        y_is_set_cost = np.sum(np.log(prediction[labels == 1]))
        y_is_not_set_cost = np.sum(np.log(1 - prediction[labels == 0]))
        cost = (-1 / num_examples) * (y_is_set_cost + y_is_not_set_cost)
        return cost
