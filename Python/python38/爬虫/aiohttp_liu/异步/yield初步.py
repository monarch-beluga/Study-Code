
def fun1():
    yield 1
    yield from fun2()
    yield 2


def fun2():
    yield 3
    yield 4


f1 = fun1()
for item in f1:
    print(item)

