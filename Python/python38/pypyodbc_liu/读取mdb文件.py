import pandas as pd
import pypyodbc as mdb

# 连接mdb文件
p_path = r'E:\Data\MeteoData20192020.mdb'

connStr = r'Driver={Microsoft Access Driver (*.mdb)}; DBQ=%s; Database=bill;' % p_path
conn = mdb.win_connect_mdb(connStr)
# 获得数据库操作对象
crsr = conn.cursor()

# 打印mdb文件中的表名
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name[2])

# pandas 读取
dfTable = pd.read_sql("SELECT * FROM all2019", conn)


