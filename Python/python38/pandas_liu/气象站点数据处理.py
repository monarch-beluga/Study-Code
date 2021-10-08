import pandas as pd

# 全国气象站点数据
Sites_file = r"E:\Data\GIS\期末作业\MeteorStations\全国气象站-756.txt"
# 站点数据文件夹+MS
path = r'E:\Data\GIS\期末作业\MeteorStations\MeteorStations\MS'
# 起始年份
time_start = 1980
# 要计算啥
var = "平均气温"
# 站点文件（自建）
Site_file = r"E:\Data\GIS\期末作业\Site.txt"
# 输出路径
out_file = r"E:\Data\GIS\期末作业\陕西气象数据1.txt"


t = "台站	年	月	日	平均本站气压	平均气温	日最高气温	日最低气温	平均相对湿度	20-20时降水量	平均风速	日照时数"
t = t.split("\t")
data = pd.read_csv(Sites_file, sep='\t', index_col=0, encoding='gbk')
with open(Site_file, "r", encoding='utf-8') as f:
    for j, Site in enumerate(f.readlines()):
        Site_list = list(filter(None, Site.split(" ")))
        print(Site)
        df = pd.read_csv(path+Site_list[0]+'.txt', index_col=None, header=None)
        df = df.iloc[:, :-1]
        df.columns = t
        df1 = df[(df['年'] >= time_start) & (df['年'] < time_start+5)]
        df1.insert(df1.shape[1], var+'1', df1[var]/10)
        df2 = df1.groupby("年")[var+'1'].mean().to_frame().T
        df3 = data[data.index == int(Site_list[0])]
        df3.insert(df3.shape[1], '城市名称', Site_list[1])
        for i in range(time_start, time_start+5):
            df3.insert(df3.shape[1], str(i)+"平均气温", df2[i].values[0])
        df3.insert(df3.shape[1], '五年'+var, df2.mean(axis=1).values[0])
        if j == 0:
            df4 = df3
        else:
            df4 = pd.concat([df4, df3], axis=0)
    df4 = df4.round(4)
    df4.to_csv(out_file, sep='\t')





