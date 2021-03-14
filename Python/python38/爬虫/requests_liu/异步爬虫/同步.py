
# -*- coding:utf-8 -*-
import requests
import time
from lxml import etree
import os

Ts = time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
urls = [
    'https://w.wallhaven.cc/full/nr/wallhaven-nrgmlm.jpg',
    'https://w.wallhaven.cc/full/kw/wallhaven-kwd36d.jpg',
    'https://w.wallhaven.cc/full/mp/wallhaven-mpexq8.png',
]


def get_content(url):
    print('正在爬取：', url)
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        return r.content


def parse_content(content):
    print("响应数据的长度为：", len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
Te = time.time()
print(Te - Ts)
