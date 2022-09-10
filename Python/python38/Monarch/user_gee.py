# -*- coding:utf-8 _*-
"""
@version:
author:Monarch
@time: 2021/07/19
@file: user_gee.py
@function:
@modify:
"""
import ee


def savitzky_golay(y: ee.List, window_size: int, order: int, deriv=0) -> ee.List:
    """
    基于List的sg滤波处理
    Args:
        y: ee.List, 原始数据
        window_size: int, 窗口大小
        order: int, 多项式阶数, 必须小于window_size
        deriv: int, 求导数的阶数, 默认为0

    Returns: ee.List, 滤波后的数据

    """
    half_window = (window_size - 1) / 2
    order_range = ee.List.sequence(0, order)
    k_range = ee.List.sequence(-half_window, half_window)
    b = ee.Array(k_range.map(lambda k: order_range.map(lambda o: ee.Number(k).pow(o))))
    m_pi = ee.Array(b.matrixPseudoInverse())
    impulse_response = (m_pi.slice(**{'axis': 0, 'start': deriv, 'end': deriv + 1 })).project([1])
    y0 = y.get(0)
    first_filling = y.slice(1, half_window + 1).reverse().map(
        lambda e: ee.Number(e).subtract(y0).abs().multiply(-1).add(y0))
    y_end = y.get(-1)
    last_filling = y.slice(-half_window - 1, -1).reverse().map(
        lambda e: ee.Number(e).subtract(y_end).abs().add(y_end))
    y_ext = first_filling.cat(y).cat(last_filling)
    run_length = ee.List.sequence(0, y_ext.length().subtract(window_size))
    smooth = run_length.map(
        lambda i: ee.Array(y_ext.slice(ee.Number(i), ee.Number(i).add(window_size))).multiply(impulse_response).reduce("sum", [0]).get([0])
    )
    return smooth


def sg_images(images: ee.ImageCollection, window_size: int, order: int, deriv=0) -> list:
    """
    基于影像的sg滤波处理
    Args:
        images: ee.ImageCollection, 需要处理的影像集, 注意请影像集中的每张影像的波段应处理为只有一个波段
        window_size: int, 窗口大小
        order: int, 多项式阶数, 必须小于window_size
        deriv: int, 求导数的阶数, 默认为0

    Returns: list, 包含滤波处理后的image的list

    """
    half_window = (window_size - 1) / 2
    order_range = ee.List.sequence(0, order)
    k_range = ee.List.sequence(-half_window, half_window)
    b = ee.Array(k_range.map(lambda k: order_range.map(lambda o: ee.Number(k).pow(o))))
    m_pi = ee.Array(b.matrixPseudoInverse())
    impulse_response = (m_pi.slice(**{'axis': 0, 'start': deriv, 'end': deriv + 1})).project([1])
    y = images.sort('system:time_start', False).toBands().toArray()
    times = images.aggregate_array('system:time_start')
    ids = images.aggregate_array('system:id')
    band_name = images.first().bandNames().get(0).getInfo()
    y1 = images.sort('system:time_start', True).toBands().toArray()
    y0 = y1.arrayGet(0)
    first_filling = y.arraySlice(0, -half_window - 1, -1).subtract(y0).abs().multiply(-1).add(y0)
    y_end = y.arrayGet(0)
    last_filling = y.arraySlice(0, 1, half_window+1).subtract(y_end).abs().add(y_end)
    y_ext = first_filling.arrayCat(y1, 0).arrayCat(last_filling, 0)
    run_length = ee.List.sequence(0, images.size().subtract(1))
    smooth = []
    for i in run_length.getInfo():
        smooth.append(y_ext.arraySlice(0, ee.Number(i), ee.Number(i).add(window_size))
                      .multiply(impulse_response).arrayReduce("sum", [0]).arrayGet([0]).rename(band_name+f'_{i}')
                      .set({'system:time_start': times.get(i), 'system:id': ids.get(i)}))
    return smooth


def bitwise_extract(value: ee.Image, from_bit: int, to_bit: int = None) -> ee.Image:
    """

    Args:
        value: ee.Image, 输入Landsat去云波段
        from_bit: int, 云的位掩码
        to_bit: int, modis去云时需要的参数, 当掩码有多位时使用

    Returns: ee.Image

    """
    if to_bit is None:
        to_bit = from_bit
    mask_size = ee.Number(1).add(to_bit).subtract(from_bit)
    mask = ee.Number(1).leftShift(mask_size).subtract(1)
    return value.rightShift(from_bit).bitwiseAnd(mask)


def cloud_free_landsat_sr(img):
    """
    Landsat 去云处理
    Args:
        img: ee.Image, 原始影像

    Returns: ee.Image, 去云后的影像

    """
    qa = img.select('pixel_qa')                         # 特定的landsat 影像才有这一波段
    # qa = img.select('QA_PIXEL')
    cloud_state = bitwise_extract(qa, 5)                # 云掩码
    cloud_shadow_state = bitwise_extract(qa, 3)         # 云影掩码
    mask = cloud_state.eq(0).And(cloud_shadow_state.eq(0))
    return img.updateMask(mask)


def rm_cloud_s2_sr(image):
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = qa.bitwiseAnd(cloud_bit_mask).eq(0).And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    return image.updateMask(mask)


def clip_dow_merge(geo: ee.Geometry, image: ee.Image, outfile: str, scale: int,
                   data_type_bytes: int, crs='EPSG:3857', max_bytes = 40000000):
    """

    Args:
        geo: ee.Geometry, 需要下载的区域矢量几何
        image: ee.Image, 需要下载的影像
        outfile: str, 输出文件路径和名称，不需要文件后缀，下载的影响默认后缀为tif
        scale: int, 下载时的像元大小
        data_type_bytes: int, 像元数据类型所占byres数, 如：16位整数占2位bytes，float浮点数占4bytes
        crs: str, 下载影像的投影，默认为 'EPSG:3857'
        max_bytes: int, 数据块最大请求大小, GEE限制为50331648byres, 即48MB
    Returns: None

    """
    import os
    import numpy as np
    import rasterio
    from glob import glob
    from rasterio.merge import merge
    import shutil
    import geemap
    import time
    bounds = geo.bounds(maxError=0.1, proj=ee.Projection(crs))
    bands = image.bandNames().size().getInfo()
    poy = np.array(bounds.coordinates().getInfo()[0])
    min_x = poy[:, 0].min()
    max_x = poy[:, 0].max()
    min_y = poy[:, 1].min()
    max_y = poy[:, 1].max()
    max_region = max_bytes * (scale*scale) / bands / (data_type_bytes+1)
    region_area = region.area(maxError=0.1, proj=ee.Projection(crs)).getInfo()
    block = int(region_area / max_region)+1
    sep_p = [i for i in np.linspace(min_x, max_x, block+1, endpoint = True)]
    polys = []
    for i in range(block):
        x1 = sep_p[i]
        x2 = sep_p[i+1]
        poly = ee.Geometry(ee.Geometry.Rectangle([float(x1), float(min_y), float(x2), float(max_y)]), ee.Projection('EPSG:3857'), False)
        Map.addLayer(poly, {'color':'00ff00'}, f'poly{i}')
        polys.append(poly)
    if len(polys) > 1:
        print(f"分割成{len(polys)}份, 开始下载:")
        path = outfile+'_mk'
        t = 1
        if not os.path.exists(path):
            t = 0
            os.makedirs(path)
        for j, i in enumerate(polys):
            if not os.path.exists(path+f'/temp_{j}.tif'):
                if t:
                    clip_dow_merge(i, image, path + f'/temp_{j}', scale, sep=sep*0.5)
                else:
                    geemap.ee_export_image(image, path + f'/temp_{j}.tif', scale=scale, crs=crs, region=i)
            else:
                continue
        files = glob(path+"/*.tif")
        if len(files) == len(polys):
            src_files_to_mosaic = []
            for tif_f in files:
                src = rasterio.open(tif_f)
                src_files_to_mosaic.append(src)
            mosaic, out_trans = merge(src_files_to_mosaic)
            out_meta = src.meta.copy()
            out_meta.update({"driver": "GTiff",
                             "height": mosaic.shape[1],
                             "width": mosaic.shape[2],
                             "transform": out_trans,
                             })
            with rasterio.open(outfile+".tif", "w", **out_meta) as dest:
                dest.write(mosaic)
            for src in src_files_to_mosaic:
                src.close()
            shutil.rmtree(path)
        else:
            print('下载不完全！！')
    else:
        geemap.ee_export_image(image, outfile+'.tif', scale=scale, crs=crs, region=geo)
    print("download successful !!!")
