import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats

matplotlib.rc("font", family='KaiTi')


def fun(path, file, ylabel1, ylabel2):
    """

    :param path:
    :param file:
    :param ylabel1:
    :param ylabel2:
    """
    data = pd.read_excel(path, sheet_name=file, index_col=0)
    a = data.columns
    a = np.array(a)
    s = []
    r = []
    p = []
    s1 = []
    r1 = []
    for i in a[1:]:
        x_data = data[a[0]]
        y_data = data[i]
        OLS = stats.linregress(x_data, y_data)
        Theil = stats.theilslopes(y_data, x_data)
        s.append(OLS[0])
        r.append(OLS[2] ** 2)
        p.append(OLS[3])
        s1.append(Theil[0])
        y_p = Theil[1] + Theil[0] * x_data
        y_p1 = OLS[1] + OLS[0] * x_data
        ssr = ((y_p - y_data.mean()) ** 2).sum()
        sst = ((y_data - y_data.mean()) ** 2).sum()
        r1.append(ssr / sst)
        # fig = plt.figure()
        # plt.plot(x_data, y_data, '.', color='b', ms=5)
        # plt.plot(x_data, y_p, color='r', )
        # plt.title(file + '_' + i + '_Theil-Sen趋势图')
        # if i in a[1:6]:
        #     plt.ylabel(ylabel1)
        # else:
        #     plt.ylabel(ylabel2)
        # plt.xlabel('年份')
        # fig.savefig('Z:/Group/Liuqiang/CEVSA趋势图/' + file + '_8018' + '_' + i + '_Theil-Sen趋势图.png', dpi=750,
        #             bbox_inches='tight')
    data_tavg_s = pd.DataFrame({'地区': a[1:], 'slope': s, 'r_squared': r, 'pvalue': p, 'Theil-Sen_slope': s1,
                                'Theil-Sen_r_squared': r1})
    with pd.ExcelWriter(path, mode='a', engine='openpyxl') as writer:
        data_tavg_s.to_excel(writer, sheet_name=file + '_趋势')


fun(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA_8018.xlsx', 'PRCP', '年总降水量：单位/mm', '年总降水量的标准差')
fun(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA_8018.xlsx', 'TAVG', '年平均气温：单位/℃', '年平均气温的标准差')
