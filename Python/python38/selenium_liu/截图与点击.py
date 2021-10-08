
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
from time import sleep

# headers = 'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"'
c_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
option = webdriver.ChromeOptions()
# option.add_argument(headers)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.binary_location = c_path
# option.add_argument('--start-maximized ')
master = webdriver.Chrome(options=option)
# 打开页面
master.get('https://kyfw.12306.cn/otn/resources/login.html')
master.execute_script('window.scrollTo(document.body.scrollWidth,0)')
sleep(1)
li = master.find_element_by_class_name('login-hd-account')
li.click()
# 全局截图
sleep(2)
outpath = 'E:/temp/爬虫/selenium/'
master.get_screenshot_as_file(outpath + '截图.png')

# 裁剪图片
# 标签定位
code_img_ele = master.find_element_by_id('J-loginImg')
# 获取左上角坐标
location = code_img_ele.location
# 得到标签的长和宽
size = code_img_ele.size
# 封装左上角坐标和右下角坐标
rangle = (location["x"], location['y'],
          location['x'] + size['width'],
          location['y'] + size['height'])
# 实例化Image对象
i = Image.open(outpath + '截图.png')
code_img_name = outpath + '裁剪截图.png'
# 进行裁剪
frame = i.crop(rangle)
frame.save(code_img_name)
input_id = master.find_element_by_id('J-userName')
input_id.send_keys('liu2744296237')
sleep(1)
input_p = master.find_element_by_id('J-password')
input_p.send_keys('2001925666LQsxyz')
sleep(1)
n = input('有几张符合的图片：')
w = 50
h = 10
for i in range(int(n)):
    x_n = input("第几列:")
    y_n = input("第几行:")
    x = w + 70*(int(x_n) - 1)
    y = h + 60*int(y_n)
    ActionChains(master).move_to_element_with_offset(code_img_ele, x, y).click().perform()
btn = master.find_element_by_id('J-login')
btn.click()
sleep(2)
span = master.find_element_by_id('nc_1_n1z')
action = ActionChains(master)
action.click_and_hold(span)
for i in range(6):
    # move_by_offset为移动的x，y个像素，perform()为立即执行
    try:
        action.move_by_offset(100, 0).perform()
        sleep(0.03)
    except:
        break
    else:
        continue
# 释放动作链对象
action.release()
# sleep(5)
# master.quit()



