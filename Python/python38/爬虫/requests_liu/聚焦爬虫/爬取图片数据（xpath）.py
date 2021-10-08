
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
# http://pic.netbian.com/
for i in range(1, 5):
    if i == 1:
        index = 'index.html'
    else:
        index = 'index_{0}.html'.format(str(i))
    url = 'http://pic.netbian.com/4kmeinv/' + index
    r = requests.get(url=url, headers=headers)
    # r.encoding = 'utf-8'                # 设定响应数据编码
    page_text = r.text
    tree = etree.HTML(page_text)
    img_list = tree.xpath('//ul[@class="clearfix"]//img')
    outpath = 'E:/temp/爬虫/requests/4k图片/index_{0}/'.format(str(i))
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for img in img_list:
        src_url = 'http://pic.netbian.com' + img.xpath('./@src')[0]
        src = requests.get(url=src_url, headers=headers).content
        name = img.xpath('./@alt')[0] + '.jpg'
        name = name.encode('iso-8859-1').decode('gbk')          # 改变乱码数据的编码格式
        with open(outpath + name, 'wb') as fp:
            fp.write(src)
        print(name, '爬取成功！！！')
    print(index, ' end')
print('end')


