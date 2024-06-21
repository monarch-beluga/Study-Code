# -*- coding: utf-8 -*-
# @Time    : 2023/8/6 10:00
# @Author  : Monarch
# @File    : 机会平等模型.py
# @Software: PyCharm

from random import randint
import matplotlib.pyplot as plt

n = [100]*100
m = 10000
flag = 0
for f in range(m):
    for i in range(100):
        k = randint(0, 99)
        # if n[i] != 0:
        n[k] += 1
        n[i] -= 1
n.sort()
fig = plt.figure(figsize=(16, 8))
plt.bar(list(range(100)), n)
plt.show()
print(n[99] - n[0])


