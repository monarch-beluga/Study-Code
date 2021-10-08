
from selenium import webdriver
from time import sleep

e_path = r'chromedriver'
master = webdriver.Chrome(executable_path=e_path)

master.get('https://qzone.qq.com/')
master.switch_to.frame('login_frame')
# btn = master.find_element_by_id('img_out_2744296237')
# btn.click()
btn = master.find_element_by_id('switcher_plogin')
btn.click()
id_input = master.find_element_by_id('u')
id_input.send_keys('2744296237')
password = master.find_element_by_id('p')
password.send_keys('2001925666LQsxyz')
btn = master.find_element_by_id('login_button')
btn.click()
sleep(5)
master.quit()

