import time
import rasterio
import numpy as np
import os
from glob import glob
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression

ts = time.time()


class para:
    read_ypath = []
    read_xpath = [r'E:\study\资料\数据\prcp_year', r'E:\study\资料\数据\prcp_year']
    year_set = [1980, 2018]
    write_path = r'E:\study\资料\数据\趋势与显著性水平'
    yraster_type = []
    xraster_type = ['.tif', '.tif']
    while_type = '.tif'
    f_coefs = ['prcp_coef1', 'prcp_coef2']
    f_r2score = 'prcp_r2score'
    f_pvalue = 'prcp_pvalue'
    n = 4


ds_read = glob(para.read_xpath[0] + os.sep + '*' + str(para.year_set[0]) + '*' + para.xraster_type[0])[0]
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
x_var_time = np.arange(para.year_set[0], para.year_set[1] + 1)


def linear_trend(datax, datay=x_var_time):
    """
    :type datax: object
    :param datay:
    :param datax:
    :return: 返回趋势r2score和显著性水平pvalue
    """
    DATA = []
    x_data = datax.T
    if (len(x_data[np.isnan(x_data)]) > 0) | (len(datay[np.isnan(datay)]) > 0):
        return [np.nan] * para.n
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
        for year in range(para.year_set[0], para.year_set[1] + 1):
            file2 = glob(Path + os.sep + '*' + str(year) + '*' + Type)[0]
            with rasterio.open(file2) as src1:
                block_array = src1.read(window=Win)[0].reshape(-1, 1)
                block_array[block_array == nodata] = np.nan
            if year == para.year_set[0]:
                temp = block_array
            else:
                temp = np.hstack((temp, block_array))
        Data.append(temp)
    Data = np.array(Data).transpose(1, 0, 2)
    return Data


def fun(win):
    data = []
    if len(para.read_ypath) != 0:
        data_y = Read_data(win, para.read_ypath, para.yraster_type)
    data_x = Read_data(win, para.read_xpath, para.xraster_type)
    with ThreadPoolExecutor(max_workers=50) as executor:
        if len(para.read_ypath) != 0:
            for i in executor.map(linear_trend, data_x, data_y):
                data.append(i)
        else:
            for i in executor.map(linear_trend, data_x):
                data.append(i)
    data = np.array(data)
    # return data
    for i, wf in enumerate(f_coefs):
        temp = data[:, i].reshape(win.height, win.width)
        wf.write(temp.astype(rasterio.float32), 1, window=win)
    r2score_f = data[:, i + 1].reshape(win.height, win.width)
    pvalue_f = data[:, i + 2].reshape(win.height, win.width)
    f_r2score.write(r2score_f.astype(rasterio.float32), 1, window=win)
    f_pvalue.write(pvalue_f.astype(rasterio.float32), 1, window=win)


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as pool:
        for i in pool.map(fun, windows):
            print(1)
    for wf in f_coefs:
        wf.close()
    f_r2score.close()
    f_pvalue.close()
    print(time.time() - ts)


# data_x = Read_data(windows[0], para.read_xpath, para.xraster_type)
