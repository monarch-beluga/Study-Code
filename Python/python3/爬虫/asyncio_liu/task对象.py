
import asyncio
import time
ts = time.time()


async def fun():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 'fun'


# async def main():
#     Task = [
#         asyncio.create_task(fun(), name='n1'),
#         asyncio.create_task(fun(), name='n2')
#     ]
#
#     print('mian结束')
#     done, pending = await asyncio.wait(Task)
#     print(done)
#
#
# asyncio.run(main())

Task = [
    fun(),
    fun()
]

done, pending = asyncio.run(asyncio.wait(Task))
print(time.time() - ts)
