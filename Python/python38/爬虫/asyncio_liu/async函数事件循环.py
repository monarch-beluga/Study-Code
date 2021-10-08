
import asyncio


async def fun():
    print('来单挑')

result = fun()
# 生成或获取一个事件循环
# loop = asyncio.get_event_loop()   # 3.7之前
# loop.run_until_complete(result)
asyncio.run(result)

