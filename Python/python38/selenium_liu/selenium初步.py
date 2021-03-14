
from selenium import webdriver
from lxml import etree
import time

e_path = r'E:\study\python\anaconda3\Scripts\chromedriver'
# 实例化一个浏览器对象
master = webdriver.Chrome(executable_path=e_path)
# 让浏览器发起一个指定的url对应的请求
master.get('http://scxk.nmpa.gov.cn:81/xk/')
# page_source获取页面源码数据
page_text = master.page_source
# 解析数据
tree = etree.HTML(page_text)
names = tree.xpath('//*[@id="gzlist"]/li/dl/@title')
print(names)
time.sleep(5)
# 关闭浏览器
master.quit()
