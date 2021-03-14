import time
# 多进程并行计算的库
from multiprocessing import Pool
import multiprocessing
# gdal库
from osgeo import gdal
# 关于数据处理的库
import numpy as np
from scipy import stats

data_2 = np.arange(1980, 2019, 1)
"""
趋势和显著性水平的计算
"""


def fun1(data_1):
    """
    :param data_1: 需要计算趋势和显著性水平的数组
    :return: 返回趋势r2score和显著性水平pvalue
    """
    x_data = data_2
    y_data = data_1 / 10
    OLS = stats.linregress(x_data, y_data)
    slope = OLS[0]                           # 趋势
    # r2score = OLS[2]**2              # 相关系数的平方
    pvalue = OLS[3]     # 显著性水平
    return slope, pvalue                            # 返回趋势和显著性水平


"""
gdal库写入tif文件
需要有写入tif文件的行，列，波段数，数据类型，投影信息，仿射信息（数据都包含在ds这个数据集中）
需要写入的数组，前面的数据都包含在ds这个数据集中
"""


def Write(file, data, ds):
    """
    :param file: tif文件名
    :param data: 写入的数组
    :param ds: 所需要的数据集
    """
    band1 = ds.GetRasterBand(1)
    img_datatype = band1.DataType
    driver = gdal.GetDriverByName('GTiff')                  # 明确写入数据驱动类型
    out_ds = driver.Create(
        r'E:/study/资料/数据/趋势与显著性水平/' + file,         # tif文件所保存的路径
        ds.RasterXSize,                                     # 行
        ds.RasterYSize,                                     # 列
        ds.RasterCount,                                     # 波段数
        img_datatype)                                       # 数据类型
    out_ds.SetProjection(ds.GetProjection())                # 投影信息
    out_ds.SetGeoTransform(ds.GetGeoTransform())            # 仿射信息
    print(ds.GetProjection(), ds.GetGeoTransform())
    for i in range(1, ds.RasterCount + 1):                  # 循环逐波段写入
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(data)                           # 写入数据
    out_ds.FlushCache()
    del out_ds


def fun(File1, File2, File3, File4, File5):
    """
    以路径E:/study/资料/数据/prcp_year/PRCP1980SUM.tif为例
    :param File1:为r'prcp_year/PRCP1980SUM.tif'
    :param File2:为r'prcp_year/PRCP'
    :param File3:为r'SUM.tif'
    :param File4:需要写入的趋势tif文件名，比如r'prcp趋势.tif'
    :param File5:需要写入的显著性水平tif文件名，比如r'prcp显著性水平.tif'
    """
    start = time.time()
    if __name__ == '__main__':                              # 程序入口
        file1 = r'E:/study/资料/数据/'                        # 需要读取的tif文件所在的文件夹的所在文件夹的路径
        ds = gdal.Open(file1 + File1)                       # 打开文件
        # 影像数据基本情况 波段数、行、列等
        im_width = ds.RasterXSize                           # 列
        im_height = ds.RasterYSize                          # 行
        im_bands = ds.RasterCount                           # 波段数
        # 影像数据读取
        band1 = ds.GetRasterBand(1)                         # 波段的indice起始为1，不为0
        img_datatype = band1.DataType                       # 数据类型
        data1 = np.full((39, im_height * im_width), 1.0)    # 建立数组
        for year in range(1980, 2019):
            file2 = file1 + File2 + str(year) + File3
            ds = gdal.Open(file2)
            img_data = ds.ReadAsArray()                     # 读取整幅图像转化为数组
            img_data = img_data.reshape(1, -1)              # 将数组转化为1行，自定义列的数组
            data1[year - 1980] = img_data                   # 将读取的数组合并成一个大数组
        # 将数组转换成以象元数为行数，年份为列数的数组
        data1 = data1.T                                     # 数组转化为dataframe，并进行行列互换
        data1[data1 == -9999] = np.nan
        # 多核并行计算
        cores = multiprocessing.cpu_count()                 # 计算机cpu的核心数（核心数=线程数，但具有多线程技术和超线程技术的线程数一般为核心数的两倍）
        pool = Pool(cores)                                  # 开启线程池
        data2 = pool.map(fun1, data1)                       # 进行并行计算，得到的data2是一个列表，map是按行读取数组来计算
        # 将data2转换成对应数组
        data2 = np.array(data2)
        data3 = data2[:, 0]
        data4 = data2[:, 1]
        data3 = data3.reshape(im_height, im_width)
        data4 = data4.reshape(im_height, im_width)
        # 写入文件
        Write(File4, data3, ds)                             # 调用Write函数
        Write(File5, data4, ds)
        end = time.time()
        print(end - start)


fun(r"prcp_year/PRCP1980SUM.tif", r'prcp_year/PRCP', r'SUM.tif', r'prcp趋势.tif', r'prcp显著性水平.tif')
# fun(r'tmax_year/TMAX1980MEAN.tif', r'tmax_year/TMAX', r'MEAN.tif', r'tmax趋势.tif', r'tmax显著性水平.tif')
# fun(r'tmean_year/TAVG1980_mean.tif', r'tmean_year/TAVG', r'_mean.tif', r'tmean趋势.tif', r'tmean显著性水平.tif')
# fun(r'tmin_year/TMIN1980MEAN.tif', r'tmin_year/TMIN', r'MEAN.tif', r'tmin趋势.tif', r'tmin显著性水平.tif')
