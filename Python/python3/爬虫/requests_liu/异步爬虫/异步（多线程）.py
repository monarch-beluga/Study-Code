
import requests
from multiprocessing.dummy import Pool
import time
import multiprocessing
from lxml import etree
import os

Ts = time.time()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
urls = [
    'https://w.wallhaven.cc/full/nr/wallhaven-nrgmlm.jpg',
    'https://w.wallhaven.cc/full/kw/wallhaven-kwd36d.jpg',
    'https://w.wallhaven.cc/full/mp/wallhaven-mpexq8.png',
    'https://w.wallhaven.cc/full/kw/wallhaven-kww6mm.png',
]


def get_content(url):
    print('正在爬取：', url)
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        print("响应数据的长度为：", len(r.content))


# if __name__ == '__main__':
# cores = multiprocessing.cpu_count()
pool = Pool(4)
pool.map(get_content, urls)
pool.close()
pool.join()
Te = time.time()
print(Te - Ts)

