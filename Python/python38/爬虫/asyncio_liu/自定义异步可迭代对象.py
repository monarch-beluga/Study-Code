
import asyncio
import requests


class Reader(object):
    # 构造函数
    def __init__(self, url_list):
        self.url_list = url_list
        self.count = 0

    # 主要执行函数
    async def readline(self):
        if self.count == len(self.url_list):
            return None
        url = self.url_list[self.count]
        r = requests.get(url, headers=headers).content
        self.count += 1
        return r

    # 声明异步迭代
    def __aiter__(self):
        return self

    # 使用执行函数并返回结果
    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


# 用协程for循环得到数据
async def fun(lis):
    obj = Reader(lis)
    async for item in obj:
        print(len(item))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
urls = [
    'https://w.wallhaven.cc/full/nr/wallhaven-nrgmlm.jpg',
    'https://w.wallhaven.cc/full/kw/wallhaven-kwd36d.jpg',
    'https://w.wallhaven.cc/full/mp/wallhaven-mpexq8.png',
]
asyncio.run(fun(urls))

