# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:10:56 2020

@author: ZDP-10-10
"""

import os
from pymodis import downmodis
import glob

outpath = r"E:\temp\LST"  # This directory must already exist BTW
# tiles = "h25v05,h26v05"
tiles = "h20v03, h20v04, h20v05, h20v06，h21v03, h21v04, h21v05, h21v06,h22v03, h22v04, h22v05, h22v06，h23v03," \
        " h23v04, h23v05, h23v06，h24v03, h24v04, h24v05, h24v06，h25v03, h25v04, h25v05, h25v06，h26v03,"  # That's the MODIS tile covering China except the islands in sourth
day = "2014.01.01"
enddate = "2000.01.01"  # The download works backward, so that enddate is anterior to day=
product = "MOD11A2.006"
modis_down = downmodis.downModis(destinationFolder=outpath,  # 数据存放路径
                                 url="https://e4ftl01.cr.usgs.gov",  # 下载地址，这个参数不变
                                 tiles=tiles,  # 下载行列号
                                 today=day,  # 开始日期
                                 user="HuiYe.cn",
                                 password="4pgkyr7yXTY4pdg",
                                 enddate=enddate,  # 结束日期
                                 product=product,  # 产品名字
                                 path="MOLT")  # 轨道号
modis_down.connect()
modis_down.downloadsAllDay()
modis_files = glob.glob(outpath + os.path + '*.hdf')
print(modis_files)
# ,h21v03, h21v04, h21v05, h21v06，h22v03, h22v04, h22v05, h22v06，h23v03, h23v04, h23v05, h23v06，h24v03, h24v04, h24v05, h24v06，h25v03, h25v04, h25v05, h25v06，h26v03, h26v04, h26v05, h26v06
