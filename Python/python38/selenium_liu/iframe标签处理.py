
from selenium import webdriver

e_path = r'chromedriver'
master = webdriver.Chrome(executable_path=e_path)

master.get('https://qzone.qq.com/')
# frame参数对象可以是id、name、index以及WebElement对象
master.switch_to.frame('login_frame')
btn = master.find_element_by_id('img_out_2744296237')
btn.click()



