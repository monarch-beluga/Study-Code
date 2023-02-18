
from greenlet import greenlet


def fun1():
    print('第一个开始')
    gr2.switch()
    print('第一个结束')
    gr2.switch()


def fun2():
    print('第二个开始')
    gr1.switch()
    print('第二个结束')


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

gr1.switch()

# 运行结果
# 第一个开始
# 第二个开始
# 第一个结束
# 第二个结束
