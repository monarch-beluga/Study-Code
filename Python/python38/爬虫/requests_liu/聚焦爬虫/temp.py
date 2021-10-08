
# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
outpath = 'E:/temp/爬虫/requests/地铁符号/'
url = 'https://www.zhihu.com/question/53073409'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
names = tree.xpath('//div[@class="RichContent-inner"]//p/b/text()')
src_url = tree.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/span/figure/img/@data-actualsrc')
# dele = [0, 1, 22, 23, 51, 52]
# del src_url[22]
# n = 0
# for d in dele:
#     del names[d - n]
#     n += 1
# for src, name in zip(src_url, names):
#     img = requests.get(url=src, headers=headers).content
#     with open(outpath + name + '.jpg', 'wb') as fp:
#         fp.write(img)
#     print(name, '爬取成功！！！')
print('end')

