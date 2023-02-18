# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:57:38 2021

@author: 佩奇
"""

import pandas as pd
import time
import glob
import numpy as np

# -------------------修改部分---------------------------


username1 = 'arcgis@vip.163.com'  # 登录邮箱的用户名
password1 = 'FTGOJMXUJJIJPSAZ'  # 登录邮箱的密码，像笔者用的是qq邮箱，qq邮箱一般是网页版，需要用到客户端密码，需要在网页版的qq邮箱中设置授权码，该授权码即为客户端密码。
subject1 = '空间规划'  # 填写标题
text1 = "详细内容见附件"  # 填写正文
interval = 120  # 120是每发送一个人之后都会暂停120秒，再继续发送下一个邮件
path = r'D:\test1111'  # 附件所在文件夹，会发送文件夹下所有文件。文件过大建议做成压缩包。可以发送word，excle，dbf，txt，压缩包等等常见文件
f_excel = r'D:\pythontest\emails\excel_email_list.xlsx'  # 更改引号内内容为所要发布的excel邮箱号。要求excel无表头。无其他除邮箱号之外的东西
# ------------------------修改部分到此结束--------------每个账号每天可以发布的邮件有限，发送失败的话可以更换标题或者更换账号或者IP地址试试呢
data = pd.read_excel(f_excel, header=None)
smtpserver1 = "smtp." + username1.split("@")[-1]
sender1 = username1
a = username1 + '<' + username1 + '>'
c = smtpserver1
fff = glob.glob(path + "\\" + '*.*')

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.header import Header

for i in range(data.shape[0]):
    data1 = data[i].values.tolist()
    smtpserver = smtpserver1
    username = username1
    password = password1
    sender = sender1
    for n in data1:
        try:
            if type(n) != str:
                continue
            receiver = n
            subject = subject1
            subject = Header(subject, 'utf-8').encode()
            msg = MIMEMultipart('mixed')
            msg['Subject'] = subject
            msg['From'] = a
            msg['To'] = n
            text = text1
            text_plain = MIMEText(text, 'plain', 'utf-8')
            msg.attach(text_plain)
            for file_name in fff:
                # 构造附件
                xlsxpart = MIMEApplication(open(file_name, 'rb').read())
                # filename表示邮件中显示的附件名
                b = file_name.split("\\", -1)[-1]
                xlsxpart.add_header('Content-Disposition', 'attachment', filename=b)
                msg.attach(xlsxpart)
            # sendfile=open(f_attachment,'rb').read()#附件所在路径
            # text_att = MIMEApplication(sendfile, 'base64', 'utf-8') 
            # # text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
            # text_att["Content-Type"] = 'application/octet-stream'
            # b = f_attachment.split("\\",-1)[-1]
            # text_att.add_header('Content-Disposition', 'attachment', filename = b)
            # # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
            # msg.attach(text_att) 
            smtp = smtplib.SMTP()
            smtp.connect(c)
            # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
            # smtp.set_debuglevel(1)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            time.sleep(interval)
            print("{}发送成功".format(n))
        except:
            print("{}发送失败".format(n))
            continue
