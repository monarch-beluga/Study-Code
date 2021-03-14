
import pandas as pd
import numpy as np

df = pd.read_excel(r'F:/文件/工作/城市高校数量及起薪数据/叶辉 城市高校数量及起薪数据.xlsx', sheet_name='高校数量', index_col=1)
data = df[['起薪.1', '起薪.2', '起薪.3', '起薪.4', '起薪.5']]
for j, i in enumerate(data.columns):
    temp = data[i]
    temp = temp.dropna()
    temp = pd.DataFrame(temp)
    temp = temp.groupby(temp.index).mean()
    temp = np.array(temp)
    if j == 0:
        data1 = temp
    else:
        data1 = np.hstack([data1, temp])
