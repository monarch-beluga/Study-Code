
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
for i in range(1, 6):
    outpath = 'E:/temp/爬虫/requests/ppt模板/page_{0}/'.format(str(i))
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    if i == 1:
        page_url = 'http://sc.chinaz.com/ppt/free.html'
    else:
        page_url = 'http://sc.chinaz.com/ppt/free_{0}.html'.format(str(i))
    r = requests.get(url=page_url, headers=headers)
    r.encoding = 'utf-8'
    page_text = r.text
    page_tree = etree.HTML(page_text)
    ppt_a = page_tree.xpath('//div[@id="main"]/div/div')
    # ppt_img = page_tree.xpath('//div[@class="sc_warp  mt20"]//img')
    # for img in ppt_img:
    #     src_url = img.xpath('./@src')[0]
    #     name = img.xpath('./@alt')[0]
    #     src = requests.get(url=src_url, headers=headers).content
    #     with open(outpath + name + '.jpg', 'wb') as fp:
    #         fp.write(src)
    #     print(name, '爬取成功！！！')
    for a in ppt_a:
        ppt_url = a.xpath('./p/a/@href')[0]
        ppt_name = a.xpath('./p/a/text()')[0]
        src_url = a.xpath('./a/img/@src')[0]
        src = requests.get(url=src_url, headers=headers).content
        with open(outpath + ppt_name + '.jpg', 'wb') as fp:
            fp.write(src)
        ppt_text = requests.get(url=ppt_url, headers=headers).text
        ppt_tree = etree.HTML(ppt_text)
        url = ppt_tree.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
        ppt = requests.get(url=url, headers=headers).content
        with open(outpath + ppt_name + '.rar', 'wb') as fp:
            fp.write(ppt)
        print(ppt_name, '爬取成功！！！')
    print('第', i, '页爬取成功！！！')
print('end')





