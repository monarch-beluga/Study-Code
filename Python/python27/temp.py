# -*- coding: utf-8 -*-
import os
import re

# 保存作业的文件夹
path = r'E:\temp'
# 包含所有人学号姓名信息的文件
file = r"E:\A1931花名册.txt"
# 人数
num = 43

c = os.listdir(path.decode('utf8'))
b = [int(re.findall(r'\d+', i)[0]) for i in c]
with open(file.decode('utf8'), 'r') as f:
    a = [i for i in f.readlines()]
for j in range(1, num + 1):
    if j not in b:
        print a[j-1].decode('GBK')
