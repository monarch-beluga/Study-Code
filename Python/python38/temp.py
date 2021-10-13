# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/14
@file: 气象数据处理.py
@function:
@modify:
"""

from work.Meteodata_import_sql.import_data import me_data_import

me_data_import(r'H:\Monarch\Data\Asia_2020.txt', 2020, 'meteodata_extens')

