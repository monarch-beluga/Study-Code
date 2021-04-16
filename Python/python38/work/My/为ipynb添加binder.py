
import json
from glob import glob
import os

path = r'E:/Study/Projects/Python/jupyter-notebook/geemap/'
location_repository = 'E:/Study/Projects/'
git_repository = 'Study-Code'
binder = 'https://notebooks.gesis.org/binder/v2/gh/'
Branch = 'master'


flag = "https://notebooks.gesis.org/binder/badge_logo.svg"
for file in glob(path+'*.ipynb'):
    with open(file, 'r', encoding='utf-8') as f:
        s = f.read()
    d1 = json.loads(s)
    if flag not in ''.join(d1['cells'][0]['source']):
        file_url = file.replace(location_repository, '')
        url = '{0}monarch-beluga/{1}/{2}?filepath={3}'\
            .format(binder, git_repository, Branch, file_url)
        file_name = os.path.split(file)[-1]
        s2 = ['<a href="{}" target="_parent">\n'.format(url),
              '<img src="https://notebooks.gesis.org/binder/badge_logo.svg" alt="launch binder"/>\n',
              '</a>']
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

