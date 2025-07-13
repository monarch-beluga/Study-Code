# -*- coding: utf-8 -*-
# @Time    : 2025/6/26 下午5:14
# @Author  : Monarch
# @File    : 爬取小说.py
# @Software: PyCharm

import requests
import os
from lxml import etree
import re
from fake_useragent import UserAgent

os.chdir(r"E:\Data\books")

book_name = ""

ua = UserAgent()

headers = {
     'User-Agent': ua.random
}
with open(book_name, "a+", encoding="utf-8") as f:
    for i in range(1, 334):
        url = f""
        r = requests.get(url=url, headers=headers)
        tree = etree.HTML(r.text)
        file_name = f"\n第{i}章\n"
        contents = tree.xpath('//div[@class="content font18"]/p//text()')
        f.write(file_name + "\n")
        f.writelines(contents)
        print(f'第{i}章')


# with open(book_name, "a+", encoding="utf-8") as f:
#     for i in range(1, 128):
#         url = f""
#         r = requests.get(url=url, headers=headers)
#         tree = etree.HTML(r.text)
#         contents = tree.xpath('//div[@class="content font18"]/p//text()')
#         text = "\n".join(contents)
#         result = re.sub(r'(第\d+章)', r'\n\1\n', text)
#         print(i)
#         f.write(result)

