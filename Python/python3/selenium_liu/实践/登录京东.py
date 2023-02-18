# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/04/06
@file: 登录京东.py
@function:
@modify:
"""

from urllib import request
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions

e_path = r'chromedriver'
master = webdriver.Chrome(executable_path=e_path)

jd_url = r'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcountry%3DUSA'
master.get(jd_url)
master.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
master.find_element(By.XPATH, '//*[@id="loginname"]').send_keys('2744296237')
master.find_element(By.XPATH, '//*[@id="nloginpwd"]').send_keys('2001925666LQsxyz')
master.find_element(By.XPATH, '//*[@id="loginsubmit"]').click()


def fun():
    image1_x = master.find_element(By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
    image1 = image1_x.get_attribute('src')
    image2_x = master.find_element(By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
    image2 = image2_x.get_attribute('src')

    image1_name = 'slide_block.png'  # 滑块图片名
    image2_name = 'slide_bkg.png'   # 背景大图名

    # 下载滑块图片并存储到本地
    request.urlretrieve(image1, image1_name)
    # 下载背景大图并存储到本地
    request.urlretrieve(image2, image2_name)

    # 获取图片，并灰化
    block = cv2.imread(image1_name, 0)
    template = cv2.imread(image2_name, 0)

    # 二值化之后的图片名称
    block_name = 'block.jpg'
    template_name = 'template.jpg'
    # 将二值化后的图片进行保存
    cv2.imwrite(template_name, template)
    cv2.imwrite(block_name, block)
    block = cv2.imread(block_name)
    block = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
    block = abs(255 - block)
    cv2.imwrite(block_name, block)

    block = cv2.imread(block_name)
    template = cv2.imread(template_name)

    # 获取偏移量
    result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)  # 查找block图片在template中的匹配位置，result是一个矩阵，返回每个点的匹配结果
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    x, y = np.unravel_index(result.argmax(), result.shape)
    return x, y
# print("x,y:", x, y, 'result.shape:', result.shape)


element = master.find_element(By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
x, y = fun()
