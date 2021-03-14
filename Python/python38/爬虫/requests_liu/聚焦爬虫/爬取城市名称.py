
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = 'https://www.aqistudy.cn/historydata/'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
# city = tree.xpath('//div[@class="bottom"]//li/a/text()')           # 方法1
city = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div[2]/li/a/text()')
# |:应用在xpath中可以以多个表达式来提取数据



