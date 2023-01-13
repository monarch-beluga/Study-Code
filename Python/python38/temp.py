# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

import numpy as np
from scipy.interpolate import CubicSpline

x = np.arange(10)
y = np.sin(x)
cs = CubicSpline(x, y)

