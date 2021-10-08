
from selenium import webdriver
from time import sleep

c_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
option = webdriver.ChromeOptions()
# option.add_argument(headers)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.binary_location = c_path
master = webdriver.Chrome(options=option)

master.get('http://www.santostang.com/2018/07/04/hello-world/')
# iframe处理
while 1:
    try:
        frame = master.find_element_by_xpath('//*[@id="lv-container"]/iframe[2]')
    except:
        sleep(2)
    else:
        break
master.switch_to.frame(frame)
# 登录操作
# 为了防止数据还未刷新
# while 1:
#     try:
#         btn = master.find_element_by_class_name('i-c-qq-m')
#     except:
#         sleep(2)
#     else:
#         break
# btn.click()
# # 切换窗口
# current_window = master.current_window_handle
# all_windows = master.window_handles
# for window in all_windows:
#     if window != current_window:
#         master.switch_to.window(window)
# # 弹窗登录
# master.switch_to.frame('ptlogin_iframe')
# while 1:
#     try:
#         span = master.find_element_by_id('img_out_2744296237')
#     except:
#         sleep(2)
#     else:
#         break
# span.click()
# 切换为原来的窗口
# master.switch_to.window(current_window)
sleep(10)   # 防止登录延时
# iframe处理
master.switch_to.frame(frame)
# 评论
text = master.find_element_by_xpath('//*[@id="wf-content"]')
text.send_keys('前来测试')
sleep(1)
btn = master.find_element_by_id('wf-write-btn')
btn.click()
# 结束
sleep(10)
master.quit()


