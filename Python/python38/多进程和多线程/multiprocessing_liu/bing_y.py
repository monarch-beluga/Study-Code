
from multiprocessing import Pool
import multiprocessing
from osgeo import gdal
from glob import glob
from scipy import stats
import numpy as np


class para:
    """
    path: 变量数据文件夹
    file_extension: 变量数据类型
    Write_path: 写入数据文件夹
    Write_file: 写入数据文件
    Data_number: 写入数据内容，0表示趋势slope，1表示相关系数r，2表示决定系数r^2,3表示显著水平p
    pool: 并行计算开启的进程池数量，最大值为 电脑的任务管理器 -> 性能 -> 逻辑处理器
    time: 数据的开始时间和结束时间
    """
    path = r'E:/study/资料/数据/prcp_year/'
    file_extension = '.tif'
    Write_path = r'E:/study/资料/数据/趋势与显著性水平/'
    Write_file = ['slope.tif', 'rscore.tif', 'r2score.tif', 'pvalue.tif']
    Data_number = [0, 1, 2, 3]
    pool = 6
    time = [1980, 2018]


data_1 = np.array(range(para.time[0], para.time[1] + 1))


def fun1(data_2):
    """
    :param data_2:
    :return:
    """
    if (len(data_1[np.isnan(data_1)]) > 0) | (len(data_2[np.isnan(data_2)]) > 0):
        return np.nan
    OLS = stats.linregress(data_1, data_2)
    slope = OLS[0]
    pvalue = OLS[3]
    rscore = OLS[2]
    r2score = rscore ** 2
    return slope, rscore, r2score, pvalue


def Write(path, File, Data_w, ds):
    """
    :param path:
    :param File: tif文件名
    :param Data_w: 写入的数组
    :param ds: 所需要的数据集
    """
    im_width = ds.RasterXSize
    im_height = ds.RasterYSize
    Data_w = Data_w.reshape(im_height, im_width)
    band1 = ds.GetRasterBand(1)
    img_datatype = band1.DataType
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(
        path + File,
        ds.RasterXSize,
        ds.RasterYSize,
        ds.RasterCount,
        img_datatype)
    out_ds.SetProjection(ds.GetProjection())
    out_ds.SetGeoTransform(ds.GetGeoTransform())
    print(ds.GetProjection(), ds.GetGeoTransform())
    for i in range(1, ds.RasterCount + 1):
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(Data_w)
    out_ds.FlushCache()
    del out_ds


def bing(Data1, cores):
    """
    :param cores:
    :param Data1:
    :param Data2:
    """
    if __name__ == '__main__':
        if cores > multiprocessing.cpu_count() * 2:
            cores = multiprocessing.cpu_count() * 2
        pool = Pool(cores)
        Data2 = pool.starmap(fun1, Data1)
        return Data2


for year in range(para.time[0], para.time[1] + 1):
    file = glob(para.path + '*' + str(year) + '*' + para.file_extension)[0]
    ds1 = gdal.Open(file)
    temp1 = ds1.ReadAsArray().reshape(-1, 1)
    if year == para.time[0]:
        data1 = temp1
    else:
        data1 = np.hstack((data1, temp1))
    del temp1,
data = bing(data1, para.pool)
data = np.array(data)
# for num, wf in zip(para.Data_number, para.Write_file):
#     Data = data[:, num]
#     Write(para.Write_path, wf, Data, ds1)
