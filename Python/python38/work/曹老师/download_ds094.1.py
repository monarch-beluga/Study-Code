#!/usr/bin/env python
#################################################################
# Python Script to retrieve 76 online Data files of 'ds094.1',
# total 30.96G. This script uses 'requests' to download data.
#
# Highlight this script by Select All, Copy and Paste it into a file;
# make the file executable and run it on command line.
#
# You need pass in your password as a parameter to execute
# this script; or you can set an environment variable RDAPSWD
# if your Operating System supports it.
#
# Contact dattore@ucar.edu (Bob Dattore) for further assistance.
#################################################################


import sys, os
import requests


def check_file_status(filepath, filesize):
    sys.stdout.write('\r')
    sys.stdout.flush()
    size = int(os.stat(filepath).st_size)
    percent_complete = (size / filesize) * 100
    sys.stdout.write('%.3f %s' % (percent_complete, '% Completed'))
    sys.stdout.flush()


# Try to get password
if len(sys.argv) < 2 and not 'RDAPSWD' in os.environ:
    try:
        import getpass
        input_pass = input()
    except:
        try:
            input_pass = input()
        except:
            pass
    pswd = input('Password: ')
else:
    try:
        pswd = sys.argv[1]
    except:
        pswd = os.environ['RDAPSWD']

url = 'https://rda.ucar.edu/cgi-bin/login'
values = {'email': '1175309706@qq.com', 'passwd': pswd, 'action': 'login'}
# Authenticate
ret = requests.post(url, data=values)
if ret.status_code != 200:
    print('Bad Authentication')
    print(ret.text)
    exit(1)
dspath = 'https://rda.ucar.edu/dsrqst/ZHU480105/'
filelist = [
    'dos-wget.480105.bat',
    'unix-curl.480105.csh',
    'unix-wget.480105.csh',
    'tmp2m.cdas1.201412.grb2.nc.gz',
    'tmp2m.cdas1.201501.grb2.nc.gz',
    'tmp2m.cdas1.201502.grb2.nc.gz',
    'tmp2m.cdas1.201503.grb2.nc.gz',
    'tmp2m.cdas1.201504.grb2.nc.gz',
    'tmp2m.cdas1.201505.grb2.nc.gz',
    'tmp2m.cdas1.201506.grb2.nc.gz',
    'tmp2m.cdas1.201507.grb2.nc.gz',
    'tmp2m.cdas1.201508.grb2.nc.gz',
    'tmp2m.cdas1.201509.grb2.nc.gz',
    'tmp2m.cdas1.201510.grb2.nc.gz',
    'tmp2m.cdas1.201511.grb2.nc.gz',
    'tmp2m.cdas1.201512.grb2.nc.gz',
    'tmp2m.cdas1.201601.grb2.nc.gz',
    'tmp2m.cdas1.201602.grb2.nc.gz',
    'tmp2m.cdas1.201603.grb2.nc.gz',
    'tmp2m.cdas1.201604.grb2.nc.gz',
    'tmp2m.cdas1.201605.grb2.nc.gz',
    'tmp2m.cdas1.201606.grb2.nc.gz',
    'tmp2m.cdas1.201607.grb2.nc.gz',
    'tmp2m.cdas1.201608.grb2.nc.gz',
    'tmp2m.cdas1.201609.grb2.nc.gz',
    'tmp2m.cdas1.201610.grb2.nc.gz',
    'tmp2m.cdas1.201611.grb2.nc.gz',
    'tmp2m.cdas1.201612.grb2.nc.gz',
    'tmp2m.cdas1.201701.grb2.nc.gz',
    'tmp2m.cdas1.201702.grb2.nc.gz',
    'tmp2m.cdas1.201703.grb2.nc.gz',
    'tmp2m.cdas1.201704.grb2.nc.gz',
    'tmp2m.cdas1.201705.grb2.nc.gz',
    'tmp2m.cdas1.201706.grb2.nc.gz',
    'tmp2m.cdas1.201707.grb2.nc.gz',
    'tmp2m.cdas1.201708.grb2.nc.gz',
    'tmp2m.cdas1.201709.grb2.nc.gz',
    'tmp2m.cdas1.201710.grb2.nc.gz',
    'tmp2m.cdas1.201711.grb2.nc.gz',
    'tmp2m.cdas1.201712.grb2.nc.gz',
    'tmp2m.cdas1.201801.grb2.nc.gz',
    'tmp2m.cdas1.201802.grb2.nc.gz',
    'tmp2m.cdas1.201803.grb2.nc.gz',
    'tmp2m.cdas1.201804.grb2.nc.gz',
    'tmp2m.cdas1.201805.grb2.nc.gz',
    'tmp2m.cdas1.201806.grb2.nc.gz',
    'tmp2m.cdas1.201807.grb2.nc.gz',
    'tmp2m.cdas1.201808.grb2.nc.gz',
    'tmp2m.cdas1.201809.grb2.nc.gz',
    'tmp2m.cdas1.201810.grb2.nc.gz',
    'tmp2m.cdas1.201811.grb2.nc.gz',
    'tmp2m.cdas1.201812.grb2.nc.gz',
    'tmp2m.cdas1.201901.grb2.nc.gz',
    'tmp2m.cdas1.201902.grb2.nc.gz',
    'tmp2m.cdas1.201903.grb2.nc.gz',
    'tmp2m.cdas1.201904.grb2.nc.gz',
    'tmp2m.cdas1.201905.grb2.nc.gz',
    'tmp2m.cdas1.201906.grb2.nc.gz',
    'tmp2m.cdas1.201907.grb2.nc.gz',
    'tmp2m.cdas1.201908.grb2.nc.gz',
    'tmp2m.cdas1.201909.grb2.nc.gz',
    'tmp2m.cdas1.201910.grb2.nc.gz',
    'tmp2m.cdas1.201911.grb2.nc.gz',
    'tmp2m.cdas1.201912.grb2.nc.gz',
    'tmp2m.cdas1.202001.grb2.nc.gz',
    'tmp2m.cdas1.202002.grb2.nc.gz',
    'tmp2m.cdas1.202003.grb2.nc.gz',
    'tmp2m.cdas1.202004.grb2.nc.gz',
    'tmp2m.cdas1.202005.grb2.nc.gz',
    'tmp2m.cdas1.202006.grb2.nc.gz',
    'tmp2m.cdas1.202007.grb2.nc.gz',
    'tmp2m.cdas1.202008.grb2.nc.gz',
    'tmp2m.cdas1.202009.grb2.nc.gz',
    'tmp2m.cdas1.202010.grb2.nc.gz',
    'tmp2m.cdas1.202011.grb2.nc.gz',
    'tmp2m.cdas1.202012.grb2.nc.gz']
for file in filelist:
    filename = dspath + file
    file_base = os.path.basename(file)
    print('Downloading', file_base)
    req = requests.get(filename, cookies=ret.cookies, allow_redirects=True, stream=True)
    filesize = int(req.headers['Content-length'])
    with open(file_base, 'wb') as outfile:
        chunk_size = 1048576
        for chunk in req.iter_content(chunk_size=chunk_size):
            outfile.write(chunk)
            if chunk_size < filesize:
                check_file_status(file_base, filesize)
    check_file_status(file_base, filesize)
    print()
