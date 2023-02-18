
import pandas as pd

a = [['jiu1', 'jiu2', 'sda1', 'asd2'], ['weq1', 'qwe2', 'rit3', 'dfo4'], ['asd1', 'xcv2', 'sdf1', 'ghj1']]
b = pd.DataFrame(a).T
# 获取第0列，jiu开头的行
# 字符串分割: 当要求的字符有固定位置时时使用
print(b[b[0].str[:3] == 'jiu'])
# 提取第2列中存在s字符的行
# 2. 正则,小括号表示要保留的数：当要求的字符不在固定位置时使用
print(b[b[2].str.extract(r'(s)', expand=False).notna()])
