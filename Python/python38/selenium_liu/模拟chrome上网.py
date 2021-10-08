
from selenium import webdriver
from lxml import etree
from time import sleep

e_path = r'E:\study\python\anaconda3\Scripts\chromedriver'
master = webdriver.Chrome(executable_path=e_path)

master.get("https://www.baidu.com/")
search_input = master.find_element_by_id('kw')
search_input.send_keys('林俊杰')
btn = master.find_element_by_class_name('s_btn_wr')
btn.click()
master.get('https://www.taobao.com/')
btn = master.find_element_by_class_name('h')
btn.click()
search_input = master.find_element_by_name('fm-login-id')
search_input.send_keys('tb188911031')
search_input = master.find_element_by_name('fm-login-password')
search_input.send_keys('2001925666LQsxyz')
btn = master.find_element_by_class_name('fm-button')
btn.click()
a = input("kw:")
search_input = master.find_element_by_id('q')
search_input.send_keys(a)
btn = master.find_element_by_class_name('btn-search')
btn.click()
master.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(10)
master.quit()


