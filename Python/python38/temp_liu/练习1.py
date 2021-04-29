

# 3. 求圆周率π
i = 1
j = 1
pai = 0
while 1 / j > 10e-6:
    pai += (1 / j) * i
    j += 2
    i = -i
pai *= 4
print("π = {}".format(pai))

# 6.
from random import randint

nums = [randint(1, 100) for i in range(100)]
odd_nums = [i for i in nums if (i % 2 != 0)]

# 12.
Sum = 0
for i in range(1, 100, 2):
    Sum += i * (i + 1)
print(Sum)

# 14.
s = input("请输入字符串：")
if s == s[::-1]:
    print("是回文字符串。")
else:
    print("不是回文字符串。")
