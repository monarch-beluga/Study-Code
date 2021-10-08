
import json
import urllib.parse

location_repository = 'E:/Study/Study-Code/'
git_repository = 'Study-Code'
binder = 'https://notebooks.gesis.org/binder/v2/gh/'
Branch = 'master'


def add_binder(file):
    file = file.replace('\\', '/')
    with open(file, 'r', encoding='utf-8') as f:
        s = f.read()
    d1 = json.loads(s)
    file_url = urllib.parse.quote(file.replace(location_repository, ''))
    url = '{0}monarch-beluga/{1}/{2}?filepath={3}'\
        .format(binder, git_repository, Branch, file_url)
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
    cell_d = d1['cells'][0]
    if cell_d != cell:
        if 'launch binder' in ''.join(cell_d['source']):
            d1['cells'][0] = cell
        else:
            d1['cells'].insert(0, cell)
        str1 = json.dumps(d1, sort_keys=True, indent=1, separators=(',', ':'))
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str1)


