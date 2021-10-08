# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/08/07
@file: bilibili表情包.py
@function:
@modify:
"""

from selenium import webdriver
import requests
import os
import time


def get(img):
    src = img.get_attribute('src').split('@')[0]
    name = img.get_attribute('title').strip('[]') + '.png'
    image = requests.get(src).content
    with open(outpath + name, 'wb') as fp:
        fp.write(image)
    print(name, "爬取成功！！！")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}

outpath = 'E:/images/'
if not os.path.exists(outpath):
    os.makedirs(outpath)
e_path = r'msedgedriver'
master = webdriver.Edge(executable_path=e_path)

url = r'https://www.bilibili.com/video/BV1554y177Sf?spm_id_from=333.851.b_7265636f6d6d656e64.1'

master.get(url)
master.execute_script('window.scrollTo(0, 500)')
while 1:
    try:
        btn = master.find_element_by_xpath('//div[@class="comment-emoji"]')
    except:
        time.sleep(1)
    else:
        break
btn.click()
time.sleep(1)
while 1:
    try:
        imgs = master.find_elements_by_xpath('//div[@class="emoji-wrap"]/a/img')
    except:
        time.sleep(1)
    else:
        break

for i in imgs:
    get(i)

master.quit()


