"""
滑动验证码解决
"""
import json
import base64
import os
import requests, re
import rsa
from logging.handlers import TimedRotatingFileHandler
import logging
import inspect
from lxml import etree
import math
import random, time, datetime, json, http.cookiejar
from multiprocessing import Process
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# email 用于构建邮件内容
from email.header import Header
from concurrent.futures import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# user_name, password, times_dict, room, seat, email
stu_dect = [
    ("19170218740", "2001925666LQsxyz", [("08:00", "09:00")], '4326', '001', "1329550246@qq.com"),  # 1195226441
    # ("17376587838", "yezhongdu990824", [("08:00", "12:00"), ("12:00", "16:00")], '0980', '029', "1195226441@qq.com"),# 1195226441
    # ("17816122906", "19981125llf", [("09:00", "13:00"), ("13:00", "17:00")], '0980', '009', "1770520942@qq.com"),# 1770520942
    # ("17816122906", "19981125llf", [ ("17:00", "21:00"), ("21:00", "22:00")], '0980', '009', "1770520942@qq.com"),# 1770520942
]


class tieba_login:
    def __init__(self):
        self.sut_dect = stu_dect
        self.login_page = "https://passport2.chaoxing.com/mlogin?loginType=1&newversion=true&fid="
        self.url = "https://office.chaoxing.com/front/third/apps/seat/code?id={}&seatNum={}"
        self.is_can_appoint_url = "https://office.chaoxing.com/data/apps/seat/room/info"
        self.submit_url = "https://office.chaoxing.com/data/apps/seat/submit"
        self.seat_url = "https://office.chaoxing.com/data/apps/seat/getusedtimes"
        self.login_url = "https://passport2.chaoxing.com/fanyalogin"
        self.token = ""
        self.success_times = 0
        self.fail_dict = []
        self.submit_msg = []
        self.start_time = None
        self.end_time = None
        self.requests = requests.session()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.05.2109131 MicroMessenger/8.0.5 Language/zh_CN webview/16364215743155638",
            "X-Requested-With": "com.tencent.mm"
        }
        self.login_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.05.2109131 MicroMessenger/8.0.5 Language/zh_CN webview/16364215743155638",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "passport2.chaoxing.com"
        }
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def get_html(self, url):
        response = self.requests.get(url=url, verify=False)
        html = response.content.decode('utf-8')
        token = re.findall('token: \'(.*?)\'', html)[0] if len(re.findall('token: \'(.*?)\'', html)) > 0 else ""

        return token

    def get_login_html(self):
        self.requests.headers = self.login_headers
        response = self.requests.get(url=self.login_page, verify=False)
        html = response.content.decode('utf-8')
        # print(html)

    def get_submit(self, url, seat, token, roomid, seatid, captcha):
        day = datetime.date.today() + datetime.timedelta(days=1)  # 预约明天
        # day = datetime.date.today()
        parm = {
            "roomId": roomid,
            "day": str(day),
            "startTime": seat[0],
            "endTime": seat[1],
            "seatNum": seatid,
            "token": token,
            "captcha": captcha,
            "type": 1
        }
        html = self.requests.post(url=url, params=parm, verify=False).content.decode('utf-8')
        self.submit_msg.append(seat[0] + "~" + seat[1] + ':  ' + str(json.loads(html)))
        print(self.submit_msg)
        print(html)
        return json.loads(html)["success"]

    def get_seat(self, url, roomid, seatid):
        parm = {
            "roomId": roomid,
            "day": str(datetime.date.today()),
            "seatNum": seatid
        }
        html = self.requests.post(url=url, params=parm, verify=False).content.decode('utf-8')

    # 登录
    def login(self, username, password):
        parm = {
            "fid": -1,
            "uname": username,
            "password": base64.b64encode(password.encode("utf-8")),
            "refer": "http%3A%2F%2Foffice.chaoxing.com%2Ffront%2Fthird%2Fapps%2Fseat%2Fcode%3Fid%3D4219%26seatNum%3D380",
            "t": True
        }
        jsons = self.requests.post(url=self.login_url, params=parm, verify=False)
        obj = jsons.json()
        print(obj)
        if obj['status']:
            return (True, '')
        else:
            return (False, obj['msg2'])

    def submit(self, i, roomid, seatid):
        flag = 5
        suc = False
        while flag > 1 and ~suc:
            token = self.get_html(self.url.format(roomid, seatid))
            captcha = self.getSlideResult(roomid, seatid)
            suc = self.get_submit(self.submit_url, i, token, roomid, seatid, captcha)
            flag -= 1

    def submit_final(self, seat_dict, roomid, seatid):
        self.start_time = time.time()
        # executor1 = ThreadPoolExecutor()
        for i in seat_dict:
            self.submit(i, roomid, seatid)
        self.end_time = time.time()

    def get_verification(self):
        # 获取滑动验证码图片信息
        times = str(int(int(round(time.time() * 1000))))
        verifi_url = "https://captcha.chaoxing.com/captcha/get/verification/image?" \
                     "callback=jQuery3310799222433353677_" + times + "&captchaId=42sxgHoTPTKbt0uZxPJ7ssOvtXr3ZgZ1&type=slide&version=1.1.6&_=" + times
        response = self.requests.get(verifi_url, verify=False)
        js = "jQuery3310799222433353677_" + times
        content = response.content.decode('utf-8')
        t = re.findall(js + "\((.*?)\)", content)
        if len(t) > 0:
            obj = json.loads(t[0])
            return (
                obj["token"], obj["imageVerificationVo"]["shadeImage"], obj["imageVerificationVo"]["cutoutImage"], js,)
        else:
            return None

    def get_verification_result(self, callback, token, textClickArr, coordinate):
        times = str(int(int(round(time.time() * 1000))))
        result_url = "https://captcha.chaoxing.com/captcha/check/verification/result?callback={}&captchaId=42sxgHoTPTKbt0uZxPJ7ssOvtXr3ZgZ1&type=slide&token={}&textClickArr={}&coordinate={}&runEnv=10&version=1.1.6&_={}".format(
            callback, token, textClickArr, coordinate, times)

        response = self.requests.get(result_url, verify=False)

        content = response.content.decode('utf-8')
        t = re.findall(callback + "\((.*?)\)", content)
        if len(t) > 0:
            obj = json.loads(t[0])
            obj1 = json.loads(obj["extraData"])

            return obj1["validate"]
        else:
            return None

    def getSlideResult(self, roomid, seatid):
        self.requests.headers.update({'Host': 'captcha.chaoxing.com'})
        self.requests.headers['Referer'] = 'https://office.chaoxing.com/'
        captcha = None
        import string
        seeds = string.digits
        random_str = random.sample(seeds, k=5)
        id = str(roomid) + "-" + str(seatid) + ("".join(random_str))
        obj = self.get_verification()
        if obj is not None:
            with open(r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.png'.format(id), 'wb') as f:
                f.write(base64.b64decode(obj[2]))
            with open(r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.jpg'.format(id), 'wb') as f:
                f.write(base64.b64decode(obj[1]))

            from Core import CrackSlider
            distance = CrackSlider().match(r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.jpg'.format(id),
                                           r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.png'.format(id))

            txtClickArr = '[{"x":' + str(distance - 5) + '}]'
            coordinate = ""
            from SomeData import datas
            if datas.__contains__(str(distance - 5)):
                _dict = json.loads(datas[str(distance - 5)][0])
                _dict[len(_dict) - 1][0] = distance + 36
                coordinate = str(_dict)
            else:
                coordinate = "[[36,383,0],[49,383,54],[66,383,57],[77,383,57],[88,383,50],[96,383,50],[104,382,54],[113,381,50],[130,378,50],[143,376,53],[147,375,104],[153,375,55],[157,375,61],[159,375,146],[163,374,59],[168,374,55],[170,374,105],[171,374,170],[175,374,56],[178,374,242],[180,374,359],[182,374,51],[{},374,341]]".format(
                    str(distance + 36))
            # coordinate = datas[str(distance-5)][0]
            from urllib.parse import quote
            captcha = self.get_verification_result(obj[3], obj[0], quote(txtClickArr), quote(coordinate))
        self.requests.headers.update({'Host': 'office.chaoxing.com'})
        self.requests.headers.pop("Referer")
        os.remove(r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.png'.format(id))
        os.remove(r'E:\Study\Projects\Python\python38\work\StudySeat\image\{}.jpg'.format(id))
        return captcha


def loginaction(username, password):
    s = tieba_login()
    s.get_login_html()
    result = s.login(username, password)
    return result


def run(username, password, timeArr, roomid, seatid, email):
    s = tieba_login()
    s.get_login_html()
    s.login(username, password)
    s.requests.headers.update({'Host': 'office.chaoxing.com'})
    s.submit_final(timeArr, roomid, seatid)
    #time.sleep(3)
    #s.send(email, username)
    return None


def tesT(username, password, roomid, seatid):
    s = tieba_login()
    s.get_login_html()
    s.login(username, password)
    s.requests.headers.update({'Host': 'office.chaoxing.com'})
    s.getSlideResult(roomid, seatid)

def main():
    run(stu_dect[0][0], stu_dect[0][1], stu_dect[0][2], stu_dect[0][3], stu_dect[0][4], stu_dect[0][5])

if __name__ == "__main__":
    # s = tieba_login(stu_dect[0])
    # login()
    # s.get_login_html()
    # run("18856657155","a123456", [["08:00","22:00"]], "1263294262@qq.com", "3788", "134")
    # test("19858121024", "buzhidao2000", "1870", "023",[["18:30","19:00"]])

    #test(stu_dect[0][0], stu_dect[0][1], stu_dect[0][3], stu_dect[0][4])

    # import string

    # seeds = string.digits
    # random_str = random.sample(seeds, k=5)
    # print("".join(random_str))

    main()

    # from app.utils.ImageService.SomeData import datas
    # if datas.__contains__(str(233-1)):
    #     _dict = json.loads(datas[str(232)][0])
    #     print(_dict)
    #     _dict[len(_dict)-1][0] = 0
    #     print(_dict)
    #     print(str(_dict).replace(' ',''), type(str(_dict)))
    #     print("[[36,383,0],[49,383,54],[66,383,57],[77,383,57],[88,383,50],[96,383,50],[104,382,54],[113,381,50],[130,378,50],[143,376,53],[147,375,104],[153,375,55],[157,375,61],[159,375,146],[163,374,59],[168,374,55],[170,374,105],[171,374,170],[175,374,56],[178,374,242],[180,374,359],[182,374,51],[{},374,341]]")
    # print(datas.__contains__(str(233-1)))
