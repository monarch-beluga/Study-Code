

import json
import re
from glob import glob

i = 1
# Dir = ['Geometry、Feature、FeatureCollection/', 'Image/', 'ImageCollection/', 'Join/', '机器学习/']
path = r'E:/Study-tool/Git/projects/Geemap_Tutorials/'
Dir = glob(path + '*')
Dir.remove(glob(path + '*.*')[0])
for d in Dir:
    for file in glob(d+'*.ipynb'):
        with open(file, 'r', encoding='utf-8') as f:
            s = f.read()
        d1 = json.loads(s)
        s1 = d1['cells'][0]['source'][0]
        url = re.findall('\((.*?)\)', s1, re.S)[1]
        s2 = ['<a href="{}" target="_parent">\n'.format(url),
              '<img src="https://notebooks.gesis.org/binder/badge_logo.svg" alt="launch binder"/>\n',
              '</a>']
        d1['cells'][0]['source'] = s2
        str1 = '\n ' + json.dumps(d1, sort_keys=True, indent=1, separators=(',', ':'))
        with open(file, 'w',  encoding='utf-8') as f:
            f.write(str1)



