"""
Core.py
"""

from PIL import Image
import cv2
import numpy as np
from io import BytesIO
import time, requests


class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """
    def __init__(self):
        self.zoom = 1

    def cut_img(self,url):
        img = cv2.imread(url)
        loc = np.where(img > 0)  # 内容为非白色部分（有意义部分）
        lx = []
        ly = []
        for pt in zip(*loc[::-1]):  # pt 为每个像素点的坐标
            lx.append(pt[1])
            ly.append(pt[2])
        sx = min(lx)
        bx = max(lx)
        sy = min(ly)
        by = max(ly)
        cv2.imwrite(url, img[sy:by, sx:bx])  # 保存时只保留有意义部分
        return url


    def get_tracks(self, distance):
        print(distance)
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3 / 5  #减速阀值
        while current < distance:
            if current < mid:
                a = 2  #加速度为+2
            else:
                a = -3  #加速度-3
            s  = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(self.cut_img(template), 0)
        run = 1
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc  # 左上角的位置
        bottom_right = (top_left[0] + w, top_left[1] + h)  # 右下角的位
        return top_left[0]


if __name__ == '__main__':
    cs = CrackSlider()
    target = r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\008.jpg'
    template = r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\008.png'
    distance = cs.match(target, template)
    tracks = cs.get_tracks((distance + 3) * cs.zoom)  # 对位移的缩放计算
    print(tracks)

    # arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
    # sums = 0
    # for i in arr:
    #   sums += i
    # print(sums)



#
# if __name__ == '__main__':
#  # img1 = cv2.imread(r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\003.jpg')
#  # cv2.imshow('img1',img1)
#  # img2 = cv2.imread(r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\003.png')
#  # cv2.imshow('img2',img2)
#  # degree = classify_gray_hist(img1,img2)
#  # # degree = classify_hist_with_split(img1,img2)
#  # # degree = classify_aHash(img1,img2)
#  # # degree = classify_pHash(img1,img2)
#  # print(degree)
#
#  distence = match(r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\004.png',r'E:\tt\Lxguang.Web\app\utils\ImageService\Images\004.jpg')
#  print(distence)
#  tracks = get_tracks(distence)
#  print(tracks)
#  # cv2.waitKey(0)