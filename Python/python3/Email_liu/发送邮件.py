import time
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def sender(sender_qq, password, receivers, content):
    host_server = "smtp.qq.com"
    # sender_qq = "2744296237@qq.com"
    # pwd = "pkgqzlrrwftvdgag"
    sender_qq_mail = sender_qq
    # receiver = "1109744244@qq.com"

    mail_content = content
    mail_title = "芬兰航空更新"

    smtp = SMTP(host_server)
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, password)

    msg = MIMEText(mail_content, "plain", "utf-8")
    msg["Subject"] = Header(mail_title, "utf-8")
    msg["From"] = sender_qq_mail
    msg["To"] = "阿布"
    smtp.sendmail(sender_qq_mail, receivers, msg.as_string())
    smtp.quit()


qq = "2744296237@qq.com"
pwd = "pkgqzlrrwftvdgag"
receivers = "3202288413@qq.com"
for i in range(100):
    sender(qq, pwd, receivers, "邮件测试")
    time.sleep(10)
