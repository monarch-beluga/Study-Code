
import aiohttp
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
]


async def get_page(url):
    print('正在下载:', url)
    async with aiohttp.ClientSession() as session:
        # await 进行阻塞挂起
        # get(), post();
        # headers, params/data, proxy='http://ip:port'
        async with await session.get(url=url, headers=headers) as r:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回json对象的响应数据
            # 在获取响应数据操作之前要使用await进行响应挂起
            print("响应数据的长度为：", len(await r.read()))


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-Ts)
