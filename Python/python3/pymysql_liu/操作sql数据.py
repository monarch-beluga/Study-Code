# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/22
@file: 操作sql数据.py
@function:
@modify:
"""

import pymysql

conn = pymysql.connect(host='192.168.1.116', password='123456', port=3306, user='root')

# sql = "insert into meteodata.student (name, sex) values ('张三', '男') ,('李四', '男'),('小丽', '女')"
sql = "delete from meteodata.student where id>1"

cour = conn.cursor()

try:
    cour.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()
