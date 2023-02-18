
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from monarch_pack import code
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
outpath = 'E:/temp/爬虫/requests/'
sin_url = 'https://so.gushiwen.cn/user/login.aspx'
sin_text = requests.get(url=sin_url, headers=headers).text
sin_tree = etree.HTML(sin_text)
img_url = 'https://so.gushiwen.cn' + sin_tree.xpath('//*[@id="imgCode"]/@src')[0]
img = requests.get(url=img_url, headers=headers).content
with open(outpath + '验证码.jpg', 'wb') as fp:
    fp.write(img)
s = code.img_to_str(image_path=outpath + '验证码.jpg')
if len(s) < 5:
    s = input('输入验证码：')
post_url = "https://so.gushiwen.cn/user/login.aspx"
data = {
    '__VIEWSTATE': 'llrgf146Iur9VOQmMaSJc5NRGJeyPtlrNFKKIQjQNOBxrJ43mDq9cCiPxYajIbuElxk4EIXPXJ6FdtNbmjPEsCryfR9MHRD0i0WA9atZ2+LqkeSoll03MoD0D9N4=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2744296237@qq.com',
    'pwd': '2001925666LQsxyz',
    'code': s[:4],
    'denglu': '登录',
}
r = requests.post(url=post_url, data=data, headers=headers)
print(r.status_code)
r.encoding = 'utf-8'
post_text = r.text
with open(outpath + 'a.html', 'w', encoding='utf-8') as fp:
    fp.write(post_text)

