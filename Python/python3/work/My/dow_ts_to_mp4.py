# -*- coding: utf-8 -*-
# @Time    : 2024/2/18 12:02
# @Author  : Monarch
# @File    : dow_ts_to_mp4.py
# @Software: PyCharm

import os
from glob import glob


def get_dow_url(main_url, n):
    path = f'E:/Platform/Games/ASMR'
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    with open(f'dow.txt', 'w') as fp:
        for i in range(2, n+1):
            print(main_url.format(i), file=fp)


def meger_ts(video_file):
    path = f'E:/Platform/Games/ASMR'
    os.chdir(path)
    files = glob(f'*.ts')
    with open(f'file.txt', 'w') as fp:
        for file in files:
            print(f"file '{file}'", file=fp)
    os.system(f'ffmpeg.exe -f concat -safe 0 -i file.txt -c copy "E:/Platform/Games/{video_file}.mp4"')
    for file in files:
        os.remove(file)


video = "ASMR AVATAR"
flag = 0
if flag:
    url = ''
    get_dow_url(url, 405)
else:
    meger_ts(video)

