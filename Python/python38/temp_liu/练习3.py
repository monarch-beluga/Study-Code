
# 1.  斐波那契前n项和
def sumfib(n):
    pev = 0
    sum_fib = 0
    curr = 1
    for i in range(n):
        sum_fib += curr
        nx = pev + curr
        pev = curr
        curr = nx
    return sum_fib

# 3. 一元二次方程
import math
def fcg(a, b, c):
    if (b*b-4*a*c) > 0:
        print('两个解')
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        return x1, x2
    elif (b*b-4*a*c) == 0:
        print('一个解')
        x = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        return x
    else:
        print('无解')
        return None

# 4. 回文字符串
def hw(ch):
    if ch == ch[::-1]:
        print('是回文字符串')
    else:
        print('不是回文字符串')


# 2.求阶乘
def jc(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s


class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def hello(self):
        print('你好, 我叫{0}, 今年{1}岁'.format(self.name, self.age))


zs = Student('张三', 18)
zs.hello()
ls = Student('李四', 19)
ls.hello()



