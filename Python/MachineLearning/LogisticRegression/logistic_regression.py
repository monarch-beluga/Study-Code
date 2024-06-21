# -*- coding: utf-8 -*-
# @Time    : 2024/4/20 9:56
# @Author  : Monarch
# @File    : logistic_regression.py
# @Software: PyCharm

import numpy as np
from utils.prepare_for_training import prepare_for_training
from utils.sigmoid import sigmoid, sigmoid_gradient


class LogisticRegression:
    def __init__(self, data, labels, polynomial_degree=0, sinusoid_degree=0, normalize_data=True, solver="bgd"):
        """
        模型初始化
        :param data: 特征值数据
        :param labels: 目标值数据
        :param polynomial_degree:
        :param sinusoid_degree:
        :param normalize_data:
        :param solver: 可选 "bgd"、"sgd"、"sag"
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
        self.solver = solver

        # 特征数
        num_features = self.data.shape[1]
        # 类别数
        num_class = self.unique_labels.shape[0]
        # 初始化参数矩阵
        self.theta = np.zeros((num_class, num_features))

    def train(self, num_iterations=500):
        """
        训练主函数, 执行梯度下降
        :param num_iterations: 迭代次数
        :return: 最终参数,损失值变化
        """
        cost_historys = []
        num_features = self.data.shape[1]
        for index, label in enumerate(self.unique_labels):
            theta = np.copy(self.theta[index].reshape(num_features, 1))
            labels = (self.labels == label).astype(float)
            theta, cost_history = self.gradient_descent(num_iterations, labels, theta)
            self.theta[index] = theta.T
            cost_historys.append(cost_history)
        return self.theta, cost_historys

    def gradient_descent(self, num_iterations, labels, theta):
        cost_history = []
        if self.solver == 'bgd':
            for _ in range(num_iterations):
                theta = self.bgd(theta, labels)
                cost_history.append(self.cost_function(self.data, labels, theta))
        elif self.solver == 'sgd':
            for _ in range(num_iterations):
                theta = self.sgd(theta, labels)
                cost_history.append(self.cost_function(self.data, labels, theta))
        elif self.solver == 'sag':
            d_prev = np.zeros(self.data.shape)
            d = np.zeros((self.data.shape[1], 1))
            for _ in range(num_iterations):
                theta = self.sag(theta, labels, d_prev, d)
                cost_history.append(self.cost_function(self.data, labels, theta))
        elif self.solver == 'newton':
            for _ in range(num_iterations):
                theta = self.newton(theta, labels)
                cost_history.append(self.cost_function(self.data, labels, theta))
        elif self.solver == "dfp":
            num_examples = self.data.shape[0]
            prediction = sigmoid(np.dot(self.data, theta))
            delta = prediction - labels
            gradients = np.dot(self.data.T, delta) / num_examples
            G = np.diag(np.ones(theta.shape[0]))
            for _ in range(num_iterations):
                theta, G, gradients = self.dfp(theta, labels, G, gradients)
                cost_history.append(self.cost_function(self.data, labels, theta))
        return theta, cost_history

    def sag(self, theta, labels, d_prev, d):
        num_examples = self.data.shape[0]
        random_index = np.random.randint(num_examples)
        xi = self.data[random_index:random_index + 1]
        yi = labels[random_index:random_index + 1]
        prediction = sigmoid(np.dot(xi, theta))
        delta = prediction - yi
        gradients = np.dot(xi.T, delta)
        d = d - d_prev[random_index:random_index + 1].T + gradients
        d_prev[random_index:random_index+1] = gradients.T
        theta -= (1 / num_examples) * d
        return theta

    def sgd(self, theta, labels):
        num_examples = self.data.shape[0]
        random_index = np.random.randint(num_examples)
        xi = self.data[random_index:random_index + 1]
        yi = labels[random_index:random_index + 1]
        prediction = sigmoid(np.dot(xi, theta))
        delta = prediction - yi
        gradients = np.dot(xi.T, delta)
        theta -= gradients
        return theta

    def bgd(self, theta, labels):
        # 批处理数量
        num_examples = self.data.shape[0]
        # 预测值计算
        prediction = sigmoid(np.dot(self.data, theta))
        # 计算真实值与预测值之差
        delta = prediction - labels
        gradients = np.dot(self.data.T, delta) / num_examples
        # 计算更新参数
        theta -= gradients
        return theta

    def get_hessian(self, prediction):
        num_examples = self.data.shape[0]
        n = prediction * (1 - prediction)
        A = np.diag(n.flatten())
        return self.data.T.dot(A).dot(self.data) / num_examples

    def newton(self, theta, labels):
        num_examples = self.data.shape[0]
        prediction = sigmoid(np.dot(self.data, theta))
        delta = prediction - labels
        gradients = np.dot(self.data.T, delta)/num_examples
        hessian = self.get_hessian(prediction)
        theta -= np.linalg.pinv(hessian).dot(gradients)
        return theta

    def dfp(self, theta, labels, G, prev_gradients):
        s = -G.dot(prev_gradients)
        theta = theta + s
        num_examples = self.data.shape[0]
        prediction = sigmoid(np.dot(self.data, theta))
        delta = prediction - labels
        gradients = np.dot(self.data.T, delta) / num_examples
        d = gradients - prev_gradients
        G += s.dot(s.T)/(s.T.dot(d)) - G.dot(d).dot(d.T).dot(G)/(d.T.dot(G).dot(d))
        return theta, G, gradients

    def bfgs(self):
        pass

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
