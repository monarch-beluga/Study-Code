
import re

s = input('输入一串字符串：')
patt = re.compile(r"(\w)")
length = len(s)
chs = set(patt.findall(s))
print("字符 次数 频率")
for i in chs:
    print(i, end='\t')
    print(s.count(i), end='\t')
    print(format(s.count(i)/length, '.4f'))
