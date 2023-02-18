import pandas as pd
import pypyodbc as mdb

# 连接mdb文件
a = r'E:\Data\temp\有问题的疑问的数据.xlsx'
p_path = r'E:\Data\temp\20210907mdb\采矿权.mdb'

connStr = r'Driver={Microsoft Access Driver (*.mdb)}; DBQ=%s; Database=bill;' % p_path
conn = mdb.win_connect_mdb(connStr)
# 获得数据库操作对象
crsr = conn.cursor()

# 打印mdb文件中的表名
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name[2])

df = pd.read_excel(a)
# pandas 读取
dfTable = pd.read_sql("SELECT `矿山名称`,`区域坐标2000` FROM `采矿申请登记`", conn)


