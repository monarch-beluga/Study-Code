
import numpy as np
import pandas as pd
import pwlf
from numpy import piecewise
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family='Simsun')


# path = r'Z:\Group\Liuqiang\MeteoGrid_CEVSA.xlsx'
# file = 'PRCP'
# ylabel1 = '年平均气温：单位/℃'
# ylabel2 = '年平均气温的标准差'
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
    for i in a[1:]:
        x_data = data[a[0]].values
        y_data = data[i].values / 10
        x = [min(x_data)]
        # 分段不拟合
        model = piecewise(x_data, y_data)
        fig1 = plt.figure()
        plt.plot(x_data, y_data, '.', color='b', ms=5)
        for seg in model.segments:
            t_new = [seg.start_t, seg.end_t]
            v_hat = [seg.predict(x_data) for x_data in t_new]
            plt.plot(t_new, v_hat, color='r', ms=5)
        plt.title(file + '_' + i + '分段不拟合趋势图')
        if i in a[6:]:
            plt.ylabel(ylabel1)
        else:
            plt.ylabel(ylabel2)
        plt.xlabel('年份')
        fig1.savefig('Z:/Group/Liuqiang/CEVSA趋势图/' + file + '_8018' + '_' + i + '_分段趋势图.png', dpi=750,
                     bbox_inches='tight')
        # 分段拟合
        for j in range(len(model.segments) - 1):
            x.append(model.segments[j].end_t)
        x.append(max(x_data))
        my_pwlf = pwlf.PiecewiseLinFit(x_data, y_data)
        # my_pwlf.fit(len(model.segments))                  # 使用这一条时，按分段数分段
        my_pwlf.fit_with_breaks(x)  # 使用这一条时，按断点分段
        x_hat = np.linspace(x_data.min(), x_data.max(), 10000)
        y_hat = my_pwlf.predict(x_hat)
        fig2 = plt.figure()
        plt.plot(x_data, y_data, '.', color='b', ms=5)
        plt.plot(x_hat, y_hat, color='r', ms=5)
        plt.title(file + '_' + i + '分段拟合趋势图')
        if i in a[6:]:
            plt.ylabel(ylabel1)
        else:
            plt.ylabel(ylabel2)
        plt.xlabel('年份')
        fig2.savefig('Z:/Group/Liuqiang/CEVSA趋势图/' + file + '_8018' + '_' + i + '_分段拟合趋势图.png', dpi=750,
                     bbox_inches='tight')


# fun(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA.xlsx', 'PRCP', '年总降水量：单位/mm', '年总降水量的标准差')
# fun(r'Z:\Group\Liuqiang\MeteoGrid_CEVSA.xlsx', 'TAVG', '年平均气温：单位/℃', '年平均气温的标准差')
