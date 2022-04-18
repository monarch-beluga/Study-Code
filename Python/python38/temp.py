# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""

from lxml import etree

with open(r'D:\VPN\订阅\最新免费v2ray节点分享.html', encoding='utf-8') as fp:
    page_text = fp.read()
page_tree = etree.HTML(page_text)
