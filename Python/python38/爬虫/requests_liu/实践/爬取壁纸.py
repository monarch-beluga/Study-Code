
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from concurrent.futures.thread import ThreadPoolExecutor
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
outpath = 'E:/images/'
if not os.path.exists(outpath):
    os.makedirs(outpath)
url = r'https://wallhaven.cc/search'


def get(href):
    src_text = requests.get(url=href, headers=headers).text
    src_tree = etree.HTML(src_text)
    src_url = src_tree.xpath('//main//img/@src')[0]
    # print(src_url)
    name = src_url.split('/')[-1]
    img = requests.get(url=src_url, headers=headers).content
    with open(outpath + name, 'wb') as fp:
        fp.write(img)
    print(name, "爬取成功！！！")


for page in range(1, 2):
    param = {
        'q': 'id:5',
        'categories': '110',
        'purity': '100',
        'atleast': '1920x1200',
        'ratios': '16x10',
        # 'topRange': '6M',
        'sorting': 'relevance',
        'order': 'desc',
        'page': str(page)
    }
    page_text = requests.get(url=url, params=param, headers=headers).text
    page_tree = etree.HTML(page_text)
    href_url = page_tree.xpath('//*[@id="thumbs"]//ul/li/figure/a[1]/@href')
    with ThreadPoolExecutor(max_workers=10) as worker:
        worker.map(get, href_url)
    print('第', page, '页爬取成功！！！')
print('end')


