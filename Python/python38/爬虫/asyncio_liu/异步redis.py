
import aioredis
import asyncio


async def execute(address, password):
    print("开始执行", address)
    redis = await aioredis.create_redis(address, password)

    await redis.hmset_dict('car', key=1)
    result = await redis.hgetall('car', encoding='utf-8')
    print(result)

    redis.close()
    await redis.wait_closed()
    print('结束', address)


Task = [
    execute('redis://127.0.0.1:6379', "160925"),
    execute('redis://127.0.0.1:6379', "160925")
]

asyncio.run(asyncio.wait(Task))



