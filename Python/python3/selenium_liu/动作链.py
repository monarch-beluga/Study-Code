
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

e_path = r'chromedriver'
master = webdriver.Chrome(executable_path=e_path)

master.get('https://www.taobao.com/')
btn = master.find_element_by_class_name('h')
btn.click()
search_input = master.find_element_by_name('fm-login-id')
search_input.send_keys('tb188911031')
search_input = master.find_element_by_name('fm-login-password')
search_input.send_keys('2001925666LQsxyz')
btn = master.find_element_by_class_name('fm-button')
btn.click()
# 定位到需要执行动作的标签
try:
    span = master.find_element_by_id('nc_1_n1z')
except:
    print("不用验证")
else:
    print('需要验证')
    # 实例化动作对象
    action = ActionChains(master)
    # 点击且长安操作
    action.click_and_hold(span)
    for i in range(5):
        # move_by_offset为移动的x，y个像素，perform()为立即执行
        try:
            action.move_by_offset(70, 0).perform()
            sleep(0.3)
        except:
            break
        else:
            continue
    # 释放动作链对象
    action.release()
    btn = master.find_element_by_class_name('fm-submit')
    btn.click()
sleep(5)
master.quit()
