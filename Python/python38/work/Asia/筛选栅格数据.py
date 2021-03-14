# 是一个筛选函数，主要时通过时间来筛选，应用在后面的几道程序中
# 这个时ECA处理的第一个程序
from datetime import datetime
from datetime import date


def select_date(file_list, file_date_start, file_date_end, moth_select):
    """

    :param file_list: tupian
    :param file_date_start: 
    :param file_date_end:
    :param moth_select:
    :return:
    """
    date_start = datetime.strptime(file_date_start, "%Y").date()
    date_end = datetime.strptime(file_date_end, "%Y").date()
    select_files = []
    i = 0
    date_start_moth = datetime.strptime('-'.join([file_date_start, moth_select[0]]), "%Y-%m-%d").date()
    date_end_moth = datetime.strptime('-'.join([file_date_start, moth_select[1]]), "%Y-%m-%d").date()
    while date_start < date_end:
        while i < len(file_list):
            file_name = file_list[i]
            i += 1
            file_date = datetime.strptime(file_name.split('.')[0].split('-')[-1], "%Y_%m_%d").date()
            if file_date >= date_start_moth:
                if file_date <= date_end_moth:
                    select_files.append(file_name)
                else:
                    i -= 1
                    break
        date_start_moth = date(date_start_moth.year+1, date_start_moth.month, date_start_moth.day)
        date_end_moth = date(date_end_moth.year+1, date_end_moth.month, date_end_moth.day)
        date_start = date(date_start.year+1, date_start.month, date_start.day)
    return select_files





