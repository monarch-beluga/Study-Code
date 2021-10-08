
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def fun(i):
    time.sleep(2)
    print(i)
    return i


if __name__ == '__main__':
    ts = time.time()
    a = [i for i in range(10)]
    b = map(fun, a)
    # with ProcessPoolExecutor(max_workers=10) as executor:
    #     a = executor.map(fun, a)
    print(time.time() - ts)

