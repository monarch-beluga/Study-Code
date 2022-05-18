import requests
from PIL import Image
from glob import glob
from concurrent.futures.thread import ThreadPoolExecutor
import os

url = 'https://s3.ananas.chaoxing.com/doc/fa/62/af/603322192cde7efa22b2ec687574ff93/thumb/{0}.png'
path = r'E:/Data/class/'
pdf_name = '导航电文.pdf'


def get_img(num):
    src_url = url.format(num)
    img = requests.get(url=src_url).content
    with open('{0:03d}.png'.format(num), 'wb') as fp:
        fp.write(img)


def combine_img_pdf(pdf_file_path):
    """
    合成文件夹下的所有图片为pdf

    Args:
        pdf_file_path (str): 输出路径
    """
    files = glob('*.png')
    sources = []
    output = Image.open(files[0]).convert("RGB")
    os.remove(files[0])
    files.pop(0)
    for file in files:
        png_file = Image.open(file).convert("RGB")
        sources.append(png_file)
        os.remove(file)
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)


os.chdir(path)
with ThreadPoolExecutor(max_workers=10) as worker:
    worker.map(get_img, list(range(1, 64)))
combine_img_pdf(pdf_name)
