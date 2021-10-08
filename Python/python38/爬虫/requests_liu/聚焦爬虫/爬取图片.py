
import requests

url = r'https://pic.qiushibaike.com/system/pictures/12371/123719664/medium/07B405896Z0VQKLF.jpg'
# content返回二进制响应数据
# text返回字符串
img_r = requests.get(url=url).content
outpath = 'E:/temp/爬虫/requests/'
with open(outpath + 'quiutu.jpg', 'wb') as fp:
    fp.write(img_r)
print('end')
