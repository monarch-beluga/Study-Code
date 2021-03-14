from multiprocessing import Pool
import multiprocessing
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression
from multiprocessing import Pool
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family='Simsun')

data = pd.read_excel(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA.xlsx', index_col=0)
a = data.columns
a = np.array(a)
s = []
r = []
p = []
for i in a[1:]:

    x_data = data[a[0]].values
    y_data = data[i].values/10
    x_data = x_data.reshape(-1, 1)
    regr = LinearRegression()
    regr.fit(x_data, y_data)
    y_pred = regr.predict(x_data)
    slope = regr.coef_[0]
    r2score = r2_score(y_data, y_pred)
    pvalue = f_regression(x_data, y_data)[1][0]
    s.append(slope)
    r.append(r2score)
    p.append(pvalue)
    fig = plt.figure()
    plt.plot(x_data, y_data, '.', color='b', ms=5)
    plt.plot(x_data, y_pred, color='r', ms=5)
    plt.title('PRCP_' + i + '趋势图')
    plt.ylabel('年总降水量：单位/mm')
    plt.xlabel('年份')
    fig.savefig(r'Z:\Group\Liuqiang\CEVSA趋势图\PRCP_' + i + '.jpg', dpi=750, bbox_inches='tight')
data_prcp_s = pd.DataFrame({'地区': a[1:], '趋势': s, '相关系数的平方': r, '显著性水平': p})
with pd.ExcelWriter(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA.xlsx', mode='a', engine='openpyxl') as writer:
    data_prcp_s.to_excel(writer, sheet_name='PRCP_趋势')


