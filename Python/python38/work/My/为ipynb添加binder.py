
import json
import re
from glob import glob
# import urllib.parse
import os

file = r'E:/Study/Projects/Python/jupyter-notebook/geemap/创建分割面板图和可视化GEE数据.ipynb'
file_url = 'Python/jupyter-notebook/geemap/创建分割面板图和可视化GEE数据.ipynb'
binder = 'https://notebooks.gesis.org/binder/v2/gh/'
git_repository = 'Study-Code'
Branch = 'master'
url = '{0}monarch-beluga/{1}/{2}?filepath={3}'\
    .format(binder, git_repository, Branch, file_url)
file_name = os.path.split(file)[-1]
# url = path_url + urllib.parse.quote(file_url)
# url = path_url + file_url
s2 = ['<a href="{}" target="_parent">\n'.format(url),
      '<img src="https://notebooks.gesis.org/binder/badge_logo.svg" alt="launch binder"/>\n',
      '</a>']
with open(file, 'r', encoding='utf-8') as f:
    s = f.read()
d1 = json.loads(s)
cell = {
    "cell_type": "markdown",
    "metadata": {
        "collapsed": False
    },
    "source": s2
}
d1['cells'].insert(0, cell)
str1 = json.dumps(d1, sort_keys=True, indent=1, separators=(',', ':'))
with open(file, 'w', encoding='utf-8') as f:
    f.write(str1)
