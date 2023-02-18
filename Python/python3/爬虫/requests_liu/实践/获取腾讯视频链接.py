# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/16
@file:  获取腾讯视频链接.py
"""

import os
import requests
from lxml import etree

os.chdir(r'H:\Monarch')
title = '三体电视剧链接'
head = r'https://jx.aidouer.net/?url='
head_url = r'https://v.qq.com/x/cover/mzc002007knmh3g/'
url = r'https://v.qq.com/x/cover/mzc002007knmh3g/s00453h4di9.html'

page_text = requests.get(url=url).text
page_tree = etree.HTML(page_text)
id_list = page_tree.xpath('//div[@class="episode-list-rect__item"]/div/@data-vid')
index_list = page_tree.xpath('//div[@class="episode-list-rect__item"]/div/span/text()')

with open(f'{title}.html', 'w', encoding='utf-8') as fp:
    head_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
    <div id="div">
        <h2 class="title">{title}</h2>
        <ul>
    """
    print(head_html, file=fp)
    for i, j in zip(id_list, index_list):
        print(f'<li><a href={head}{head_url}{i}.html>{j}</a></li>', file=fp)
    end_html = """
        </ul>
    </div>




    </body>
    </html>
    """
    print(end_html, file=fp)


