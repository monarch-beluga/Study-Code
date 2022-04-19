# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

n = int(input("请输入菱形的行数:"))
print()
for i in range(n//2+n%2):
  print(" "*((n-(2*i+1))//2*2), "* "*(2*i+1))
for i in range(n//2-1,-1,-1):
  print(" "*((n-(2*i+1))//2*2), "* "*(2*i+1))