# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/08/11
@file: Snake.py
@function:
@modify:
"""

from tkinter import *
from PIL import Image, ImageTk
from time import sleep


def local_img(file_name):
    return ImageTk.PhotoImage(Image.open(file_name))


size = 24
snakeX = [6, 5, 4]
snakeY = [2, 2, 2]

windows = Tk()
windows.geometry('1000x800+100+100')
windows.title("贪吃蛇")
windows.resizable(False, False)

title_img = local_img('statics/Title.jpg')
head_img = local_img('statics/head.jpg')
food_img = local_img('statics/food.png')
body_img = local_img('statics/body.jpg')

frame = Frame(height=600, width=960, bg='black')
frame.place(x=20, y=180)

title_label = Label(image=title_img)
title_label.place(x=20, y=10)

head_label = Label(image=head_img, bg='black')

i = 2


def paint_snake():
    global i
    length = len(snakeX)
    head_label.place(x=20+size*i, y=180+size*snakeY[0])
    i += 1
    # for i in range(1, length):
    #     body_label = Label(image=body_img, bg='black')
    #     body_label.place(x=20+size * snakeX[i], y=180+size * snakeY[i])


windows.after(1, paint_snake)
windows.mainloop()

