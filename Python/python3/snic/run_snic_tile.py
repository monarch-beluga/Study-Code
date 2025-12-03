# -*- coding: utf-8 -*-
# @Time    : 2025/10/15 下午8:51
# @Author  : Monarch
# @File    : run_snic_tile.py
# @Software: PyCharm

import os
from glob import glob

path = r"D:\Work\gaofen2\snic"
out_tif_path = r"D:\Work\gaofen2\snic_out_tif"
os.makedirs(out_tif_path, exist_ok=True)
out_label_path = r"D:\Work\gaofen2\snic_out_label"
os.makedirs(out_label_path, exist_ok=True)
os.chdir(r"D:\Work\snic_python_interface")
exe = "SNICrun.py"

for filename in glob(os.path.join(path, "*.TIF")):
    out_file = os.path.join(out_tif_path, os.path.basename(filename).replace(".TIF", "_snic.tif"))
    out_label = os.path.join(out_label_path, os.path.basename(filename).replace(".TIF", "_snic_label.tif"))
    os.system(exe + " " + filename + " " + out_file + " " + out_label)

