
from work.My.为ipynb添加binder import add_binder
from glob import glob

location_repository = 'E:/Study/Study-Code/'
git_repository = 'Study-Code'
binder = 'https://notebooks.gesis.org/binder/v2/gh/'
Branch = 'master'

path = r'E:/Study/Study-Code/Python/jupyter-notebook/geemap/'

files = glob(path+'*.ipynb')

add_binder(files[7])
