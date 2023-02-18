
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}
http = {'https': '154.127.50.138:1080'}
outpath = 'E:/Data/'
url = "http://ip.293.net/"
page_text = requests.get(url=url, headers=headers, proxies=http).text
tree = etree.HTML(page_text)
ip = tree.xpath('//div[@id="content_left"]//di[@class="c-row"]/div[2]//span/text()')

