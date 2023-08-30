# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 19:23
# @Author  : Monarch
# @File    : GrassType_res.py
# @Software: PyCharm

from tkinter import Frame, StringVar, Label, Entry, Button, Tk, filedialog, Radiobutton, W
from zipfile import ZipFile
from io import BytesIO
from PIL import Image, ImageTk
from xmltodict import parse
from json import dumps, loads
import sys
import os


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def img_show(img_name, img_scale=None):
    if not img_scale:
        img_width = img_frame.winfo_width()
        img_height = img_frame.winfo_height()
        img_scale = min(img_height, img_width)
    img = Image.open(BytesIO(global_dict['zfp'].read(img_name))).resize((img_scale, img_scale))
    render = ImageTk.PhotoImage(img)
    imgGL.image = render
    imgGL.config(image=render)


def rb_select():
    i = global_dict['curr']
    global_dict['rb'][i] = rb_val.get()
    global_dict['Placemark'][i]['ExtendedData']['SchemaData']['SimpleData'][-2]['#text'] = rb_val.get()


def pre_img():
    global_dict['curr'] -= 1
    if global_dict['curr'] < 0:
        global_dict['curr'] = len(global_dict['ground_over']) - 1
    img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])
    img_lab.set(f"图片显示：第{global_dict['curr']+1}张")
    rb_val.set(global_dict['rb'][global_dict['curr']])


def next_img():
    global_dict['curr'] += 1
    if global_dict['curr'] >= len(global_dict['ground_over']):
        global_dict['curr'] = 0
    img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])
    img_lab.set(f"图片显示：第{global_dict['curr']+1}张")
    rb_val.set(global_dict['rb'][global_dict['curr']])


def update_img():
    img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])


def choose_save_file():
    out_txt = filedialog.asksaveasfilename(title='保存文件', defaultextension='.txt', filetypes=[("txt Files", "*.txt")])
    save_e.set(out_txt)


def save_txt():
    out_txt = save_e.get()
    if out_txt != '':
        with open(out_txt, 'w') as fp:
            for i, p in enumerate(global_dict['Placemark']):
                print(f"{i+1},{p['name']},{p['ExtendedData']['SchemaData']['SimpleData'][-2].get('#text')}", file=fp)


def quit_program():
    if global_dict.get('zfp'):
        global_dict['zfp'].close()
    root.destroy()


global_dict = {}

root = Tk()
root.geometry('800x600')

root.title('GrassType')
mainFrame = Frame(root)
mainFrame.pack(side='left', anchor='n')

classification = [['温性草甸草原', '温性草原'],
                  ['温性荒漠草原', '热性草丛'],
                  ['高寒荒漠草原', '高寒草原'],
                  ['温性草原化荒漠', '温性荒漠'],
                  ['高寒草甸草原', '高寒荒漠'],
                  ['热性灌草丛', '暖性草丛'],
                  ['暖性灌草丛', '低地草甸'],
                  ['温性山地草甸', '高寒草甸'],
                  ['沼泽', '人工草地']]
Label(mainFrame, text='草地类型选择：').pack()

rb_frame = Frame(mainFrame, bd=2, relief="groove")
rb_frame.pack()
rb_val = StringVar()
rb_val.set('none')

for row, x in enumerate(classification):
    for col, y in enumerate(x):
        Radiobutton(rb_frame, text=y, variable=rb_val, value=y, command=rb_select)\
            .grid(row=row, column=col, padx=5, pady=5, sticky=W)

save_file = Frame(mainFrame)
save_file.pack()

save_e = StringVar()
Label(save_file, text='输出文件:').grid(column=0, row=0, padx=5, pady=5, sticky='w')
save_file_text = Entry(save_file, textvariable=save_e, width=25)
save_file_text.grid(column=0, row=1, padx=5, pady=5)
save_file_button = Button(save_file, text='<<', command=choose_save_file)
save_file_button.grid(column=1, row=1, padx=5, pady=5)

img_frame = Frame(root, relief="groove", bd=2)
img_frame.pack(side='right', anchor='n', fill='both', expand=1, padx=5, pady=5)
img_lab = StringVar()
img_lab.set('图片显示：')
Label(img_frame, textvariable=img_lab).pack(side='top')
showFrame = Frame(img_frame, relief="groove")
showFrame.pack()
imgGL = Label(showFrame)
imgGL.pack()

kmz_file = resource_path(os.path.join("res", "GrassType.kmz"))
global_dict['zfp'] = ZipFile(kmz_file, 'r')
xml_parse = parse(global_dict['zfp'].read('doc.kml'))
json_str = dumps(xml_parse, indent=1)
kml = loads(json_str)
global_dict['kml'] = kml
global_dict['ground_over'] = global_dict['kml']['kml']['Document']['Folder']['GroundOverlay']
global_dict['Placemark'] = global_dict['kml']['kml']['Document']['Document']['Folder']['Placemark']
global_dict['curr'] = 0
global_dict['rb'] = [i['ExtendedData']['SchemaData']['SimpleData'][-1].get('#text') for i in global_dict['Placemark']]
img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'], img_scale=560)
img_lab.set(f"图片显示：第{global_dict['curr']+1}张")
rb_val.set(global_dict['rb'][global_dict['curr']])

bu_frame = Frame(mainFrame)
bu_frame.pack(side='bottom')
Button(bu_frame, text='刷新图片', command=update_img).grid(column=0, row=0, padx=10, pady=5)
Button(bu_frame, text='上一张', command=pre_img).grid(column=1, row=0, padx=10, pady=5)
Button(bu_frame, text='下一张', command=next_img).grid(column=2, row=0, padx=10, pady=5)
Button(bu_frame, text='保存', command=save_txt).grid(column=0, row=1, padx=10, pady=5)
Button(bu_frame, text='退出', command=quit_program).grid(column=1, row=1, padx=10, pady=5)

root.mainloop()

