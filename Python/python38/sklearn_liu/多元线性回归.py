
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression


def fun1(datay, datax):
    for i, temp in enumerate(datax):
        if i == 0:
            data_x = temp.reshape(-1, 1)
        else:
            data_x = np.hstack((data_x, temp.reshape(-1, 1)))
    if(len(data_x[np.isnan(data_x)]) > 0) | (len(datay[np.isnan(datay)]) > 0):
        return [np.nan]*(i+1), np.nan, np.nan
    regr = LinearRegression().fit(data_x, datay)
    coef = [i for i in regr.coef_]
    y_pred = regr.predict(data_x)
    r2score = r2_score(datay, y_pred)
    pvalue = f_regression(datay.reshape(-1, 1), y_pred)[1][0]
    return coef, r2score, pvalue


a = np.array([6, 11, 10, 15])
b = np.array([[1, 2, 3, 4], [1, 2, 1, 2]])
data = fun1(a, b[0], b[1])










