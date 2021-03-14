
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

c_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
headers = 'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"'
# 浏览器参数设置
option = ChromeOptions()
# add_argument()添加启动参数
# 启动最大化界面
option.add_argument('--start-maximized ')
# 添加UA
option.add_argument(headers)
# 指定浏览器分辨率
option.add_argument('window-size=1920x3000')
# 无可视化界面浏览
option.add_argument('--headless')
# 规避bug
option.add_argument('--disable-gpu')

# add_experimental_option()添加实验性质的设置参数
# 规避监测， 即启动开发者模式
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 指定使用的浏览器位置
option.binary_location = c_path

# option.add_extension()/option.add_encoded_extension()添加扩展应用
# 添加指定crx插件
option.add_extension(r'E:\temp\爬虫\crx\Adblock.crx')
# e_path = r'E:\study\python\anaconda3\Scripts\chromedriver'
master = webdriver.Chrome(options=option)

master.get('https://kyfw.12306.cn/otn/login/init')
# # 查看浏览历史
master.get('chrome://history/')

sleep(5)
master.quit()


