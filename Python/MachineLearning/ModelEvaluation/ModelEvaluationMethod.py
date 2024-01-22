# -*- coding: utf-8 -*-
# @Time    : 2024/1/7 10:30
# @Author  : Monarch
# @File    : ModelEvaluationMethod.py
# @Software: PyCharm

import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.base import clone
import warnings

# matplotlib参数设置
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
warnings.filterwarnings('ignore')
# 设定了单例RandomState实例的种子
np.random.seed(42)

mnist = fetch_openml('mnist_784', parser='auto')
X = mnist['data'].values
y = mnist['target'].values.codes
print(X.shape, y.shape)

# 展示第一个样本
x_0 = X[0, :].reshape(28, 28)
plt.imshow(x_0, cmap="gray_r")
plt.axis('off')
plt.show()

X_train = X[:60000]
X_test = X[60000:]
y_train = y[:60000]
y_test = y[60000:]

# 数据洗牌
# permutation随机排列序列
shuffle_index = np.random.permutation(60000)
X_train = X_train[shuffle_index]
y_train = y_train[shuffle_index]

sgd_clf = SGDClassifier(max_iter=5, random_state=42)
sgd_clf.fit(X_train, y_train)

# 进行预测并展示
y_pred_0 = sgd_clf.predict([X_test[3500]])
print("预测的值：", y_pred_0, "实际的值：", y_test[3500])
# x_3500 = X_test[3500].reshape(28, 28)
# plt.imshow(x_3500, cmap="gray_r")
# plt.axis('off')
# plt.show()

# 用sklearn自带的交叉验证函数
cross_score = cross_val_score(sgd_clf, X_train, y_train, cv=5, scoring='accuracy')
print(cross_score)

# 手动分块进行交叉验证
sk_folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_index, val_index in sk_folds.split(X_train, y_train):
    clone_clf = clone(sgd_clf)
    X_train_folds = X_train[train_index]
    y_train_folds = y_train[train_index]
    X_val_folds = X_train[val_index]
    y_val_folds = y_train[val_index]

    clone_clf.fit(X_train_folds, y_train_folds)
    y_pred = clone_clf.predict(X_val_folds)
    n_correct = sum(y_pred == y_val_folds)
    print(n_correct/len(y_pred))

# 混淆矩阵
labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train, cv=5)
from sklearn.metrics import confusion_matrix
y_confusion_matrix = confusion_matrix(y_train, y_train_pred, labels=labels)
print(y_confusion_matrix)

# 评估指标计算
TP = y_confusion_matrix.diagonal()
TN = TP.sum() - TP
FP = y_confusion_matrix.sum(axis=0) - TP
FN = y_confusion_matrix.sum(axis=1) - TP

# 准确率
Acc = TP.sum() / y_confusion_matrix.sum()
print("Accuracy:", Acc)

import pandas as pd
# 精确率
Ppv = TP / (TP + FP)
# 召回率
Tpr = TP / (TP + FN)
# 特异度
Tnr = TN / (TN + FP)
# F1 得分
F1 = TP / (TP + (FN + FP) / 2)
df = pd.DataFrame({'Precision': Ppv, 'Recall': Tpr, 'Specificity': Tnr, 'F1 score': F1}, index=labels)
print(df)
from sklearn.metrics import f1_score
f1_score(y_train, y_train_pred, average='macro')

