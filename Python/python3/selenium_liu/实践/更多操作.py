
from selenium import webdriver
from lxml import etree
from time import sleep

e_path = r'E:\study\python\anaconda3\Scripts\chromedriver'
master = webdriver.Chrome(executable_path=e_path)
master.get("https://www.taobao.com/")

# 执行一组js程序
master.execute_script('window.scrollTo(0,document.body.scrollHeight)')

master.get('https://www.baidu.com/')
sleep(2)
# 浏览器回退
master.back()
sleep(2)
# 浏览器前进
master.forward()
sleep(2)
master.back()

# 标签定位
search_input = master.find_element_by_id('q')
# 标签交互
search_input.send_keys('Iphone')
# 点击搜索按钮
btn = master.find_element_by_css_selector('.btn-search')
btn.click()

