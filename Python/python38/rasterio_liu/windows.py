
import time
import rasterio
import os
from glob import glob
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression


ts = time.time()
class para:
    read_xpath = []
    read_ypath = [r'E:\study\资料\数据\prcp_year']
    year_set = [1980, 2018]
    write_path = r'E:\study\资料\数据\趋势与显著性水平'
    xraster_type = []
    yraster_type = ['.tif']
    while_type = '.tif'
    f_coefs = ['prcp_coef1', 'prcp_coef2']
    f_r2score = 'prcp_r2score'
    f_pvalue = 'prcp_pvalue'


ds_read = glob(para.read_ypath[0] + os.sep + '*' + str(para.year_set[0]) + '*' + para.yraster_type[0])[0]
with rasterio.open(ds_read) as src:
    windows = [window for ij, window in src.block_windows()]
    profile = src.profile
    nodata = src.nodata
f_coefs = []
for i in para.f_coefs:
    f_coef = rasterio.open(para.write_path + os.sep + i + para.while_type, 'w', **profile)
    f_coefs.append(f_coef)
f_r2score = rasterio.open(para.write_path + os.sep + para.f_r2score + para.while_type, 'w', **profile)
f_pvalue = rasterio.open(para.write_path + os.sep + para.f_pvalue + para.while_type, 'w', **profile)


def linear_trend(datay, *datax):
    """
    :param datay:
    :param datax:
    :return: 返回趋势r2score和显著性水平pvalue
    """
    DATA = []
    for i, temp in enumerate(datax):
        temp = temp.reshape(-1, 1)
        if i == 0:
            x_data = temp
        else:
            x_data = np.hstack((x_data, temp))
    if (len(x_data[np.isnan(x_data)]) > 0) | (len(datay[np.isnan(datay)]) > 0):
        return np.full((i + 3), np.nan)
    else:
        regr = LinearRegression().fit(x_data, datay)
        for i in regr.coef_:
            DATA.append(i)
        y_pred = regr.predict(x_data)
        r2score = r2_score(datay, y_pred)
        pvalue = f_regression(datay.reshape(-1, 1), y_pred)[1][0]
        DATA.append(r2score)
        DATA.append(pvalue)
        DATA = np.array(DATA)
        return DATA


def Read_data(Win, Paths, Types):
    Data = []
    for Path, Type in zip(Paths, Types):
        for year in range(para.year_set[0], para.year_set[1]+1):
            file2 = glob(Path + os.sep + '*' + str(year) + '*' + Type)[0]
            with rasterio.open(file2) as src1:
                block_array = src1.read(window=Win)[0].reshape(-1, 1)
                block_array[block_array == nodata] = np.nan
            if year == para.year_set[0]:
                temp = block_array
            else:
                temp = np.hstack((temp, block_array))
        Data.append(temp)
    return Data


for win in windows:
    if len(para.read_xpath) == 0:
        x_var_time = np.arange(para.year_set[0], para.year_set[1] + 1)
        P = win.height * win.width
        N = len(x_var_time)
        data_x = np.zeros((P, N))
        data_x[:] = x_var_time
        data_x = [data_x, data_x]
    else:
        data_x = Read_data(win, para.read_xpath, para.xraster_type)
    data_y = Read_data(win, para.read_ypath, para.yraster_type)
    data_y += data_x
    data = np.array([i for i in map(linear_trend, *data_y)])
    for i, wf in enumerate(f_coefs):
        temp = data[:, i].reshape(win.height, win.width)
        wf.write(temp.astype(rasterio.float32), 1, window=win)
    r2score_f = data[:, i+1].reshape(win.height, win.width)
    pvalue_f = data[:, i+2].reshape(win.height, win.width)
    f_r2score.write(r2score_f.astype(rasterio.float32), 1, window=win)
    f_pvalue.write(pvalue_f.astype(rasterio.float32), 1, window=win)
for wf in f_coefs:
    wf.close()
f_r2score.close()
f_pvalue.close()
print(time.time()-ts)



