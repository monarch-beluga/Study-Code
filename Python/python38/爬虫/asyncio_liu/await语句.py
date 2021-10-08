
import asyncio


async def fun():
    print('来单挑')
    await asyncio.sleep(2)
    print('end')
    return 'fanhui'


async def fun1():
    print('加载')
    r = await fun()
    print('结果', r)
    r1 = await fun()
    print('jieguo', r1)

asyncio.run(fun1())




