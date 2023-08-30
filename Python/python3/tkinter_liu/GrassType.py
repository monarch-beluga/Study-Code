# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 18:09
# @Author  : Monarch
# @File    : GrassType.py
# @Software: PyCharm

from tkinter import Frame, StringVar, Label, Entry, Button, Tk, filedialog, Radiobutton, W
from zipfile import ZipFile, ZIP_DEFLATED
from io import BytesIO
from PIL import Image, ImageTk
from xmltodict import parse, unparse
from json import dumps, loads


def img_show(img_name):
    img = Image.open(BytesIO(global_dict['zfp'].read(img_name))).resize((300, 300))
    render = ImageTk.PhotoImage(img)
    imgGL.image = render
    imgGL.config(image=render)


def choose_file():
    kmz_file = filedialog.askopenfilename(title='选择文件', filetypes=[("kmz Files", "*.kmz")])
    # print(selectFileName)
    if kmz_file != '':
        e.set(kmz_file)
        global_dict['kmz_file'] = kmz_file
        global_dict['zfp'] = ZipFile(kmz_file, 'r')
        xml_parse = parse(global_dict['zfp'].read('doc.kml'))
        json_str = dumps(xml_parse, indent=1)
        kml = loads(json_str)
        global_dict['kml'] = kml
        global_dict['ground_over'] = global_dict['kml']['kml']['Document']['Folder']['GroundOverlay']
        global_dict['Placemark'] = global_dict['kml']['kml']['Document']['Document']['Folder']['Placemark']
        global_dict['curr'] = 0
        global_dict['rb'] = [i['ExtendedData']['SchemaData']['SimpleData'][-2].get('#text') for i in global_dict['Placemark']]
        img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])
        rb_val.set(global_dict['rb'][global_dict['curr']])


def rb_select():
    i = global_dict['curr']
    global_dict['rb'][i] = rb_val.get()
    global_dict['Placemark'][i]['ExtendedData']['SchemaData']['SimpleData'][-2]['#text'] = rb_val.get()


def pre_img():
    global_dict['curr'] -= 1
    if global_dict['curr'] < 0:
        global_dict['curr'] = len(global_dict['ground_over']) - 1
    img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])
    rb_val.set(global_dict['rb'][global_dict['curr']])


def next_img():
    global_dict['curr'] += 1
    if global_dict['curr'] >= len(global_dict['ground_over']):
        global_dict['curr'] = 0
    img_show(global_dict['ground_over'][global_dict['curr']]['Icon']['href'])
    rb_val.set(global_dict['rb'][global_dict['curr']])


def choose_save_file():
    out_kmz = filedialog.asksaveasfilename(title='保存文件', defaultextension='.kmz', filetypes=[("kmz Files", "*.kmz")])
    save_e.set(out_kmz)


def save_kmz():
    kml_str = unparse(global_dict['kml'], encoding='UTF-8', pretty=True, indent='  ')
    zout = ZipFile(save_e.get(), 'w', ZIP_DEFLATED)
    for item in global_dict['zfp'].infolist():
        buffer = global_dict['zfp'].read(item.filename)
        if item.filename != 'doc.kml':
            zout.writestr(item, buffer)
        else:
            zout.writestr('doc.kml', kml_str)
    # global_dict['zfp'].close()
    zout.close()


def quit_program():
    if global_dict.get('zfp'):
        global_dict['zfp'].close()
    root.destroy()


global_dict = {}

root = Tk()

root.title('GrassType')
root.geometry(f'{400}x{720}')

select_file = Frame(root, width=300, height=30)
select_file.place(x=0, y=0)

e = StringVar()
Label(select_file, text='选择kmz文件:').grid(column=0, row=0, padx=5, pady=5)
select_file_text = Entry(select_file, textvariable=e, width=30)
select_file_text.grid(column=1, row=0, padx=5, pady=5)
select_file_button = Button(select_file, text='<<', command=choose_file)
select_file_button.grid(column=2, row=0, padx=5, pady=5)

Label(root, text='图片显示：').place(x=5, y=35)

img_frame = Frame(root, bd=2, relief="groove", width=350, height=300)
img_frame.place(x=5, y=65)
imgGL = Label(img_frame)
imgGL.place(x=0, y=0)

classification = [['温性草甸草原', '温性草原', '温性荒漠草原'],
                  ['高寒草甸草原', '高寒草原', '高寒荒漠草原'],
                  ['温性草原化荒漠', '温性荒漠', '高寒荒漠'],
                  ['热性草丛', '热性灌草丛', '暖性草丛'],
                  ['暖性灌草丛', '低地草甸', '温性山地草甸'],
                  ['高寒草甸', '沼泽', '人工草地']]

Label(root, text='草地类型选择：').place(x=5, y=365)

rb_frame = Frame(root, bd=2, relief="groove", width=300, height=200)
rb_frame.place(x=5, y=395)
rb_val = StringVar()
rb_val.set('none')

for row, x in enumerate(classification):
    for col, y in enumerate(x):
        Radiobutton(rb_frame, text=y, variable=rb_val, value=y, command=rb_select)\
            .grid(row=row, column=col, padx=5, pady=5, sticky=W)

save_file = Frame(root, width=300, height=30)
save_file.place(x=0, y=630)

save_e = StringVar()
Label(save_file, text='保存kmz文件:').grid(column=0, row=0, padx=5, pady=5)
save_file_text = Entry(save_file, textvariable=save_e, width=30)
save_file_text.grid(column=1, row=0, padx=5, pady=5)
save_file_button = Button(save_file, text='<<', command=choose_save_file)
save_file_button.grid(column=2, row=0, padx=5, pady=5)

bu_frame = Frame(root, width=300, height=30)
bu_frame.place(x=0, y=670)
Button(bu_frame, text='上一张', command=pre_img).grid(column=0, row=0, padx=10, pady=5)
Button(bu_frame, text='下一张', command=next_img).grid(column=1, row=0, padx=10, pady=5)
Button(bu_frame, text='保存', command=save_kmz).grid(column=2, row=0, padx=10, pady=5)
Button(bu_frame, text='退出', command=quit_program).grid(column=3, row=0, padx=10, pady=5)

root.mainloop()

