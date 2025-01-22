# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 上午8:13
# @Author  : Monarch
# @File    : get_dy.py
# @Software: PyCharm

import os

path = r"D:\Study_tool\Tomcat\webapps\V2ray"
os.chdir(path)
html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>V2ray节点</title>
</head>
<body>
<ul>
"""
html_end = """
</ul>
</body>
</html>
"""

file_list = os.listdir("dy")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_head)
    for file in file_list:
        li = f"<li><a href='dy/{file}'>{file}</a></li>"
        f.write(li)
    f.write(html_end)
