s = input()
d = 0
while s:
    d = d + 2 ** (len(s)-1) * int(s[0])
    s = s[1:]

print(d)
