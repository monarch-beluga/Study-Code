
import asyncio


# 对语句中的环境进行控制
class AsynContextMager:
    def __init__(self, conn):
        self.conn = conn

    async def do_(self):
        return 666

    async def __aenter__(self):
        self.conn = await asyncio.sleep(2)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1)


async def fun():
    # async with来运行异步上下文管理器
    async with AsynContextMager(1) as f:
        result = await f.do_()
        print(result)


asyncio.run(fun())

