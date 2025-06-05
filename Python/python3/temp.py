# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 14:25
# @Author  : Monarch
# @File    : temp.py
# @Software: PyChar

import os
import geopandas as gpd
import pandas as pd
from glob import glob

os.chdir(r"D:\Study_tool\Tomcat\webapps\anyi\api\jsonData")

df = pd.read_json("anyi_yjwz.json")



