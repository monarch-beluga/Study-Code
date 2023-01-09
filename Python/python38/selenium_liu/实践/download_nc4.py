# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/1/8
@file:  download_nc4.py
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = r'H:\Monarch\Work\subset'
os.chdir(path)
url_file = r'subset_M2T1NXRAD_5.12.4_20230107_142752_.txt'

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,  # 防止保存弹窗
         'download.default_directory': path,  # 设置默认下载路径
         "profile.default_content_setting_values.automatic_downloads": 1  # 允许多文件下载
         }
options.add_experimental_option('prefs', prefs)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

master = webdriver.Chrome(options=options)

# 登录界面
master.get(r'https://urs.earthdata.nasa.gov/')
while 1:
    try:
        username = master.find_element(By.ID, 'username')
    except:
        time.sleep(1)
    else:
        break
password = master.find_element(By.ID, 'password')

# 账号密码输入
username_key = input('请输入账号：')
password_key = input('请输入密码：')
username.send_keys(username_key)
password.send_keys(password_key)
submit = master.find_element(By.XPATH, r'//*[@id="login"]/p[5]/input')
submit.click()

# # txt文件读取
with open(url_file) as fp:
    urls = fp.readlines()

file_name = ''
time.sleep(5)
# txt文件中的url下载
for i, url in enumerate(urls[:5]):      # 这里尝试下载5个url
    url = url.strip()
    master.get(url)
    file_name = url.split('/')[-1]
    print(f'{i} {file_name} 正在下载...')
    # 下载等待
    time.sleep(40)

# 下载完成后退出程序
while os.path.exists(file_name):
    master.quit()

