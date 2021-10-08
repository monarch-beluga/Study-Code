
import asyncio
import time


async def request(url):
    print("正在下载：", url)
    # 在异步协程中如果出现了同步模块相关的代码，就无法实现异步
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print("下载完毕", url)
    return url

start = time.time()
urls = [
    'https://w.wallhaven.cc/full/nr/wallhaven-nrgmlm.jpg',
    'https://w.wallhaven.cc/full/kw/wallhaven-kwd36d.jpg',
    'https://w.wallhaven.cc/full/mp/wallhaven-mpexq8.png',
    'https://w.wallhaven.cc/full/kw/wallhaven-kww6mm.png',
]

# 任务列表
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start)

