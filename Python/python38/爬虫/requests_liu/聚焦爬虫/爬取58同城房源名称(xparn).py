
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
get_url = 'https://bj.58.com/ershoufang/'
page_text = requests.get(url=get_url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
with open(r'E:\temp\爬虫\requests\58同城\58.txt', 'w', encoding='utf-8') as fp:
    for li in li_list:
        t = li.xpath('./div[2]//a/text()')[0]
        m = li.xpath('./div[3]//b/text()')[0] + '万'
        v = li.xpath('./div[3]/p[2]/text()')[0]
        fp.write(t + '\n' + m + '\t' + v + '\n\n')
# li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
# for li in li_list:
#     li.xpath('./div[2]/h2/a/text()')
print('end')

