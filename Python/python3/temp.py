# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time


def get(img):
    src = img.get_attribute('src').split('@')[0]
    name = img.get_attribute('alt').strip('[]-').split('_')[-1] + '.png'
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
# e_path = r'msedgedriver'
master = webdriver.Chrome()

url = r'https://www.bilibili.com/opus/945372132325457943?spm_id_from=333.999.0.0'

master.get(url)

time.sleep(1)
imgs = master.find_elements(By.XPATH, '//*[@id="app"]/div[4]/div[1]/div[2]/p/img')
for i in imgs[1,-1]:
    get(i)
master.quit()

