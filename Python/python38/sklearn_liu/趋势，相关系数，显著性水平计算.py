
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression


a = [1, 2, 3, 4]
b = [5, 25, 56, 45]
df = pd.DataFrame({"cal": a, "obs": b})
x_data = df['cal'].values                       # 横轴
y_data = df['obs'].values                       # 竖轴
x_data = x_data.reshape(-1, 1)
regr = LinearRegression()
regr.fit(x_data, y_data)
y_pred = regr.predict(x_data)
slope = regr.coef_[0]                           # 趋势
r2score = r2_score(y_data, y_pred)              # 相关系数的平方
pvalue = f_regression(x_data, y_data)[1]    # 显著性水平
print(slope, r2score, pvalue)
