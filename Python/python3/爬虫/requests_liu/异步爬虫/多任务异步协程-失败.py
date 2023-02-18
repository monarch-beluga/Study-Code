
import requests
import asyncio
import time

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


async def get_page(url):
    print('正在下载:', url)
    # requests发起的请求是基于同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    # alohttp基于异步的网络请求模块
    r = requests.get(url=url, headers=headers)
    print("响应数据的长度为：", len(r.content))


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-Ts)
