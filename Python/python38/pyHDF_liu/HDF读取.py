import netCDF4 as nc
from pyhdf.HDF import HDF, HC
import numpy as np
import pandas as pd

file_name = r'F:/temp.HDF'
f = nc.Dataset(file_name)
# print(file.info())
