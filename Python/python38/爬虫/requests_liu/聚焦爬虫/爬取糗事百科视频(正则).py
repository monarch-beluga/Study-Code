
import requests
import re
import os
# 正则法则解析数据

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
for i in range(1, 3):
    url = r'https://www.qiushibaike.com/video/page/{0}/'.format(i)
    page_text = requests.get(url=url, headers=headers).text
    ex = '<video controls=.*?<source src="(.*?)" type=.*?</video>'
    void_src_list = re.findall(ex, page_text, re.S)
    outpath = 'E:/temp/爬虫/requests/糗事百科视频/page-{0}/'.format(i)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for j, src in enumerate(void_src_list[:4]):
        src = "http:" + src
        void_data = requests.get(url=src, headers=headers).content
        name = src.split('/')[-1]
        with open(outpath + name, "wb") as fp:
            fp.write(void_data)
        print(name, '下载成功')
print('end')


