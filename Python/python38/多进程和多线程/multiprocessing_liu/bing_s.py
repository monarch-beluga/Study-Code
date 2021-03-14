from multiprocessing import Pool
import multiprocessing
import pandas as pd
from scipy import stats
import numpy as np


def fun1(data_1, data_2):
    """
    :param data_2:
    :param data_1: 需要计算趋势和显著性水平的数组
    :return: 返回趋势r2score和显著性水平pvalue
    """
    if (len(data_1[np.isnan(data_1)]) > 0) | (len(data_2[np.isnan(data_2)]) > 0):
        return np.nan
    OLS = stats.linregress(data_1, data_2)
    r2score = OLS[2]  # 相关系数的平方
    return r2score


def bing(Data1, Data2):
    """

    :param Data1:
    :param Data2:
    """
    if __name__ == '__main__':
        Data3 = zip(Data1, Data2)
        cores = multiprocessing.cpu_count()
        pool = Pool(cores)
        data4 = pool.starmap(fun1, Data3)
        print(data4)

