# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""
a = input("请输入:")
d = 0
while a:
    d = d*2+int(a[0])
    a = a[1:]
print("{}".format(d))

