# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/7
@file:  download_hdf.py
"""

import requests
import os
import re
from concurrent.futures.thread import ThreadPoolExecutor
import time
from Monarch.tqdm_common import get_asyncio_bar


os.chdir(r'Z:\ECA\GLASS_temperature')

url = r'http://www.glass.umd.edu/LST/v01/Daily-ODC/'


def download_file(outfile):
    if not os.path.exists(outfile):
        file_temp = outfile+'.tmp'
        r = requests.get(f'{url}{outfile}', stream=True)
        with open(file_temp, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                bar.update(len(chunk))
                fd.write(chunk)
        os.rename(file_temp, outfile)
    else:
        bar.update(file_size)


hdf_file = []
for year in range(1991, 2001):
    if not os.path.exists(f'{year}'):
        os.mkdir(f'{year}')

    page_text = requests.get(url=f'{url}{year}').text
    ex = '<td><a href="(.*?)">.*?</a></td>'
    file_list = re.findall(ex, page_text, re.S)

    for i in file_list:
        if '.hdf' == i[-4:]:
            hdf_file.append(f'{year}/{i}')

r_file = requests.get(f'{url}{hdf_file[0]}', stream=True)
file_size = int(r_file.headers.get('content-length', 0))
r_file.close()

bar = get_asyncio_bar(f'download hdf data', len(hdf_file)*file_size)

with ThreadPoolExecutor(max_workers=20) as worker:
    worker.map(download_file, hdf_file)

bar.update(bar.total - bar.n)
bar.close()

