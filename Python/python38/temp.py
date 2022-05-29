# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/22
@file: temp.py
@function:
@modify:
"""
import requests
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

os.chdir(r'D:\entertainment\Love Death Robots\第一季')
url_head = r'http://www.ntyou.cc{}'
e_path = r'chromedriver'
master = webdriver.Chrome(executable_path=e_path)
master.get(url_head.format('/play/3035-1-1.html'))
page_text = master.page_source
tree = etree.HTML(page_text)
src_links = tree.xpath('//*[@id="main0"]/div[1]/ul/li/a/@href')
video_urls = []
for src_link in src_links:
    master.get(url_head.format(src_link))
    master.switch_to.frame(2)
    time.sleep(1)
    video_urls.append(master.find_element(By.XPATH, '//*[@id="lelevideo"]').get_attribute('src'))
master.quit()
# for video_url in video_urls:
#     with open(f'{i:02d}第{i}集.mp4', 'wb') as fp:
#         fp.write(requests.get(url=video_url).content)
#     print(f'{i:02d}第{i}集.mp4 下载成功！！！')



