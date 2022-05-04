# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2022/05/04
@file: dxf_to_pdf.py
@function:
@modify:
"""

import matplotlib.pyplot as plt
import ezdxf
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import os
from glob import glob


def convert_dxf2img(names, img_format, dpi):
    for name in names:
        doc = ezdxf.readfile(name)
        msp = doc.modelspace()
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ctx = RenderContext(doc)
        ctx.set_current_layout(msp)
        out = MatplotlibBackend(ax)
        Frontend(ctx, out).draw_layout(msp, finalize=True)
        img_name = name.replace('.dxf', img_format)
        plt.savefig(img_name, dpi=dpi)
        plt.close()


os.chdir(r'E:\Work\HDF5')
dxf_files = glob("*.dxf")
convert_dxf2img(dxf_files, img_format='.pdf', dpi=300)

