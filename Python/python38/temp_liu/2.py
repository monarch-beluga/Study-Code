import rasterio
import numpy as np
from multiprocessing import Pool
import multiprocessing
from scipy import stats
import time

data_2 = np.arange(1980, 2019, 1)


def fun2(data_1):
    """
    :param data_1: 需要计算趋势和显著性水平的数组
    :return: 返回趋势r2score和显著性水平pvalue
    """
    J = data_1.shape[1]
    K = data_1.shape[2]
    k = np.empty((2, 1, J, K), dtype='float32')
    for x in range(0, J):
        for y in range(0, K):
            y_data = data_1[:, x, y] / 10
            x_data = data_2
            OLS = stats.linregress(x_data, y_data)
            slope = OLS[0]
            # r2score = OLS[2]**2
            pvalue = OLS[3]
            k[0, 0, x, y] = pvalue          # 显著性水平
            k[1, 0, x, y] = slope           # 趋势
    return k


def fun(win):
    """

    :param win:
    """
    file = r'E:/study/资料/数据/'
    File2 = r'prcp_year/PRCP'
    File3 = r'SUM.tif'
    dat = []
    for year in range(1980, 2019):
        file2 = file + File2 + str(year) + File3
        with rasterio.open(file2) as src1:
            block_array = src1.read(window=win)[0]  # 读取数据
        dat.append(block_array)
    data1 = np.array([j for j in dat])  # 处理数
    data2 = fun2(data1)
    with open(r"E:/study/资料/数据/趋势与显著性水平/prcp_pvalue.flt", 'ab') as f:
        f.write(data2[0])
    with open(r"E:/study/资料/数据/趋势与显著性水平/prcp_slope.flt", 'ab') as f1:
        f1.write(data2[1])



if __name__ == '__main__':
    start = time.time()
    file1 = r'E:/study/资料/数据/'
    File1 = r'prcp_year/PRCP1980SUM.tif'
    a = []
    b = []
    with rasterio.open(file1 + File1) as src:  # 获取读取窗口
        windows = [window for ij, window in src.block_windows()]
        profile = src.profile
    cores = multiprocessing.cpu_count()  # 计算机cpu的核心数（核心数=线程数，但具有多线程技术和超线程技术的线程数一般为核心数的两倍）
    pool = Pool(cores)  # 开启线程池
    pool.map(fun, windows)
    end = time.time()
    print(end - start)
