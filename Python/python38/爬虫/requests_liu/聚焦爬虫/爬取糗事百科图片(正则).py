
import requests
import re
import os
# 正则法则解析数据

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
for i in range(1, 5):
    url = r'https://www.qiushibaike.com/imgrank/page/{0}/'.format(str(i))
    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    outpath = 'E:/temp/爬虫/requests/糗事百科图片/page-{0}/'.format(str(i))
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for src in img_src_list:
        src = 'https:' + src
        name = src.split('/')[-1]
        img_data = requests.get(url=src, headers=headers).content
        with open(outpath + name, 'wb') as fp:
            fp.write(img_data)
            print(name, '下载成功')
print('end')


