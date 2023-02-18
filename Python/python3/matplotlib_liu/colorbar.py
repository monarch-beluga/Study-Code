import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family='KaiTi')                           # 选择字体
plt.rcParams['axes.unicode_minus'] = False                      # 负号不显示问题
ds_mak = gdal.Open(r'Z:/Group/Liuqiang/Climate_4R.tif')
mak = ds_mak.ReadAsArray()


def fun(path, file):
    """
    :param path: 图片文件夹
    :param file:
    """
    for i in ['_slope_8018', '_Rsquare_8018', '_pvalue_8018']:
        ds = gdal.Open(path + file + i + '.tif')
        data = ds.ReadAsArray()
        im_width = ds.RasterXSize
        im_height = ds.RasterYSize
        data[mak > 100] = np.nan
        if file == 'PRCP':
            cmap = matplotlib.cm.rainbow_r
        else:
            cmap = matplotlib.cm.rainbow
        fig = plt.figure()
        h = plt.imshow(data, cmap=cmap)
        plt.title(file + i)
        plt.colorbar(h, orientation='horizontal', fraction=0.05, shrink=0.5, spacing='uniform')
        # orientation调节颜色条水平还是垂直 ， faction调节大小
        plt.show()
        fig.savefig('Z:/Group/Liuqiang/CEVSA空间趋势图/' + file + i + '.png', dpi=600, bbox_inches='tight')


fun(r'Z:/Group/Liuqiang/CEVSA空间趋势图/', 'TEM')
