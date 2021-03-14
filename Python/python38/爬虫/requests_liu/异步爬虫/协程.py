
import asyncio


async def request(url):
    print("正在请求的url是：", url)
    print("请求成功，", url)
    return url

# async修饰函数，调用后返回一个协程对象
c = request('www.baidu.com')
# 创建一个事件循环对象
loop = asyncio.get_event_loop()

# 将协程对象注册到loop中，然后启动loop
loop.run_until_complete(c)

# task将协程对象封装到任务对象中
task = loop.create_task(c)
# 显示pending即待定
print(task)
# 运行任务对象
loop.run_until_complete(task)
# 显示finished即任务已完成
print(task)

# future不基于loop来创建任务对象
task = asyncio.ensure_future(c)
# 显示pending即待定
print(task)
loop.run_until_complete(task)
# 显示finished即任务已完成
print(task)


def callback_func(task):
    print(task.result())


# 绑定回调
task = asyncio.ensure_future(c)
# 绑定回调函数
task.add_done_callback(callback_func)
loop.run_until_complete(task)
