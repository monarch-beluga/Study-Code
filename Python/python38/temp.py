# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

import time


def parse_p():
    time.sleep(1)
    print(1)


def parse(ls):
    for i in ls:
        yield parse_p()
        print(i)


url_list = ['a', 'b', 'c', 'd']

for i in parse(url_list):
    i = 0

