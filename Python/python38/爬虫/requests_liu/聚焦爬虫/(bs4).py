
from bs4 import BeautifulSoup
import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = r'https://www.qiushibaike.com/imgrank/page/1/'
page_text = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(page_text, 'lxml')         # bs4化页面数据
"""筛选标签"""
print(soup.find('div', class_='thumb'))
# find返回查找的标签（div），属性为（thumb）的第一个数据
print(soup.find_all('div', class_='thumb'))
# find_all返回所有标签为（div）,属性为（thumb）的数据,返回类型为列表
print(soup.select('.thumb > a > img'))
# select可以按某种筛选器来选择数据，其中>表示一个层级（层级筛选）
print(soup.select('.thumb img'))
# 空格表示多个层级
"""提取标签中的数据"""
for i in soup.select('.thumb img'):
    print(i['src'])
# [属性名称]获取标签中对应的属性值，获取文本信息是直接.text或者.string



