
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
get_url = r'https://www.qiushibaike.com/imgrank/page/1/'
page_text = requests.get(url=get_url, headers=headers).text
tree = etree.HTML(page_text)
r = tree.xpath('/html/head/meta')
# /:表示从根节点开始定位，并表示一个层级
r = tree.xpath('/html//meta')
r = tree.xpath('//meta')
# //:表示多个层级，并表示任意位置定位
r = tree.xpath('//div[@class="thumb"]//img')  # 属性定位
# 标签名[@属性名=属性]
r = tree.xpath('//meta[1]')             # 索引定位
# 标签名[索引]从1开始
r = tree.xpath('//div[@class="content"]/span/text()')       # 获取文本数据
r = tree.xpath('//div[@class="content"]//text()')
# 在定位的标签后面加上/text()，返回一个列表,获取的是定位的标签下直系的文本属性
# //text()获取定位标签下所有文本数据
r = tree.xpath('//div[@class="thumb"]//img/@src')           # 获取属性数据
# /@属性名称






