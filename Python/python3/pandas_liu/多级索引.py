
import pandas as pd
import pypyodbc as mdb
import os

p_path = r'E:\Data\temp\MeteoData20192020.mdb'
# 访问数据库                               # 连接mdb文件
connStr = r'Driver={Microsoft Access Driver (*.mdb)}; DBQ=%s; Database=bill;' % p_path
# 链接数据库
conn = mdb.win_connect_mdb(connStr)
# 操作数据库
crsr = conn.cursor()  # 获得数据库操作对象
files = ['all2019', 'all2020']      # 表列表
vars = ['日最高气温', '日最低气温', '降水量', '平均相对湿度', '日照时数', '平均风速']  # 数据列表
step = 8            # 八天求平均
out_path = r'E:/Data/shuchu/'       # 输出路径

for file in files:
    # 将mdb表数据读取为DataFrame
    df = pd.read_sql("SELECT * FROM {0}".format(file), conn)
    # 去重
    df.drop_duplicates(subset=None, keep='first', inplace=True)
    # 排序
    df_sort = df.sort_values(by=['台站', '月', '日'], ascending=(True, True, True))
    # 以八天为准建立唯一标识
    df_sort.insert(df_sort.shape[1], 'temp', df_sort['月']*100+df_sort['日'])
    days = len(df_sort['temp'].unique())
    Site_num = len(df_sort['台站'].unique())
    old = df_sort['temp'].unique().tolist()
    new = [day//step for day in range(days)]
    df_sort['temp'].replace(old, new, inplace=True)
    # 按vars循环计算
    for var in vars:
        # 降水量求和,其他的求平均
        if var == '降水量':
            # 分组计算
            # to_frame()转为DataFrame
            # unstack()将多级列表中的最内层列索引转为行索引，让时间序列变为行索引
            df_calc = df_sort.groupby(['台站', 'temp'])[var].sum().to_frame().unstack()
        else:
            df_calc = df_sort.groupby(['台站', 'temp'])[var].mean().to_frame().unstack()
        # 重新建立行索引
        cols_name = ['{0}_{1}'.format(i+1, i+8) for i in range(0, days-8, 8)]
        cols_name.append('361_366')
        df_calc.columns = cols_name
        # 建立文件夹
        out = out_path + var
        if not os.pa2.th.exists(out):
            os.makedirs(out)
        # 保留两位小数
        df_calc = df_calc.round(2)
        # 输出
        df_calc.to_csv(out + os.sep + var + file + '.txt', sep='\t')

