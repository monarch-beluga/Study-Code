# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/09
@file: drive.py
@function:
@modify:
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# List files in Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in fileList:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
