
import rasterio
import glob
import numpy as np
from scipy import stats
import time
from multiprocessing import Pool
import multiprocessing

start = time.time()
file1 = r'E:/study/资料/数据/'
File1 = r'prcp_year/PRCP1980SUM.tif'
a = []
b = []
with rasterio.open(file1 + File1) as src:  # 获取读取窗口
    windows = [window for ij, window in src.block_windows()]
    profile = src.profile
    nodata = src.nodata
write_file = ['prcp_slope.tif', 'prcp_r2scoer.tif', 'prcp_pvalue.tif']
Data = []
for i in write_file:
    src1 = rasterio.open(r'E:/study/资料/数据/趋势与显著性水平/' + i, 'w', **profile)
    Data.append(src1)


def fun2(data_2, data_1):
    """
    :param data_2:
    :param data_1: 需要计算趋势和显著性水平的数组
    :return: 返回趋势r2score和显著性水平pvalue
    """

    y_data = data_1 / 10
    if len(y_data[y_data == nodata]) > 0:
        return np.nan, np.nan, np.nan
    else:
        x_data = data_2
        OLS = stats.linregress(x_data, y_data)
        slope = OLS[0]
        r2scoer = OLS[2]**2
        pvalue = OLS[3]
        return slope, r2scoer, pvalue


def bing(Data1, Data2):
    """

    :param Data1:
    :param Data2:
    """
    if __name__ == '__main__':
        Data3 = zip(Data1, Data2)
        cores = multiprocessing.cpu_count()
        pool = Pool(2)
        Data4 = pool.starmap(fun2, Data3)
        return Data4


for win in windows:
    file = r'E:/study/资料/数据/prcp_year/*'
    for year in range(1980, 2019):
        file2 = glob.glob(file + str(year) + '*.tif')
        with rasterio.open(file2[0]) as src1:
            block_array = src1.read(window=win)[0].reshape(-1, 1)
        if year == 1980:
            data1 = block_array
        else:
            data1 = np.hstack((data1, block_array))
    data2 = np.zeros((win.height * win.width, 39))
    data2[:] = np.arange(1980, 2019, 1)
    data3 = bing(data2, data1)
    data3 = np.array(data3)
    for i, wf in enumerate(Data):
        wf.write(data2[i], window=win)
for wf in Data:
    wf.close()
end = time.time()
print(end - start)


