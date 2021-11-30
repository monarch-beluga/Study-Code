import time
import os

a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
os.system("git add --all")
os.system(f'git commit -m {a}')
os.system(f'git pull origin master')
os.system(f'git push origin master')

# b = '''git add --all
# git commit -m "%s"
# git pull origin master
# git push origin master
# ''' % a
# with open(r"automatic1.bat", "w") as f:
#     f.write(b)
