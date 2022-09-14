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


def clip_big_image(geo: ee.Geometry, image: ee.Image, scale: int, data_type_bytes: int,
                     crs='EPSG:3857', max_bytes=40000000):
    """

    Args:
        geo: ee.Geometry, 需要下载的区域矢量几何
        image: ee.Image, 需要下载的影像
        scale: int, 下载时的像元大小
        data_type_bytes: int, 像元数据类型所占byres数, 如：16位整数占2位bytes，float浮点数占4bytes
        crs: str, 下载影像的投影，默认为 'EPSG:3857'
        max_bytes: int, 数据块最大请求大小, GEE限制为50331648byres, 即48MB

    Returns:
        list: 裁剪后的
    """
    import numpy as np
    import math
    bounds = geo.bounds(maxError=0.1, proj=ee.Projection(crs))
    bands = image.bandNames().size().getInfo()
    poy = np.array(bounds.coordinates().getInfo()[0])
    min_x = poy[:, 0].min()
    max_x = poy[:, 0].max()
    min_y = poy[:, 1].min()
    max_y = poy[:, 1].max()

    x_offset = int(min_x / scale)
    y_offset = int(max_y / scale) + 1
    height = y_offset - int(min_y / scale)
    width = int(max_x / scale) - x_offset + 1
    transform = [scale, 0, x_offset * scale , 0, -scale, y_offset * scale]

    x_interval = max_x - min_x
    y_interval = max_y - min_y
    max_region = max_bytes * (scale*scale) / bands / (data_type_bytes+1)
    max_length = int(math.sqrt(max_region))
    region_area = geo.area(maxError=0.1, proj=ee.Projection(crs)).getInfo()
    if max_region > region_area:
        print("不需要裁剪，可直接下载")
        return None, None, None, None, None, None
    else:
        sep_x = max_length
        sep_y = max_length
        if x_interval < max_length:
            sep_x = x_interval
            sep_y = max_region / x_interval
        if y_interval < max_length:
            sep_y = y_interval
            sep_x = max_region / y_interval
        p_x = [i for i in np.arange(min_x, max_x, sep_x)] + [max_x]
        p_y = [i for i in np.arange(min_y, max_y, sep_y)] + [max_y]
        polys = []
        for i in range(len(p_x) - 1):
            for j in range(len(p_y) - 1):
                poly = ee.Geometry(
                    ee.Geometry.Rectangle([float(p_x[i]), float(p_y[j]), float(p_x[i + 1]), float(p_y[j + 1])]),
                    ee.Projection(crs), False)
                polys.append(poly)
        return polys, x_offset, y_offset, height, width, transform


def dow_Collection(image, ee_polys, count, path, scale, crs):
    from concurrent.futures import ThreadPoolExecutor,  wait, ALL_COMPLETED
    with ThreadPoolExecutor(2) as pool:
        pool.map(dow, [[image, ee_polys.get(i), i, path, scale, crs] for i in range(count)])




def clip_dow_merge(geo: ee.Geometry, image: ee.Image, outfile: str, scale: int,
                   data_type_bytes: int, crs='EPSG:3857', max_bytes=40000000, flag=True):
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
    import geemap
    import time
    from glob import glob
    from concurrent.futures import ThreadPoolExecutor,  wait, ALL_COMPLETED, FIRST_COMPLETED
    start = time.time()
    polys, x_offset, y_offset, height, width, transform = clip_big_image(geo, image, scale, data_type_bytes, crs, max_bytes)
    if polys:
        ee_polys = ee.FeatureCollection(polys).filterBounds(geo)
        count = ee_polys.size().getInfo()
        # clip_images = ee.ImageCollection(ee_polys.map(lambda x: image.clip(x.geometry()))).toList(count)
        print("影像切割完毕！！！")
        path = outfile + '_mk'
        if not os.path.exists(path):
            os.makedirs(path)
        files = len(glob(path+"/*.tif"))
        # print(f"需要下载的影像数: {count-files}\n")
        # dow_Collection(image, ee_polys.toList(count), count, path, scale, crs)
        while files != count:
            print(f"需要下载的影像数: {count-files}\n")
            # dow_Collection(clip_images, count, path, scale, crs)
            dow_Collection(image, ee_polys.toList(count), count, path, scale, crs)
            files = len(glob(path+"/*.tif"))
        if flag:
            merge_img(path, outfile, x_offset, y_offset, height, width, transform)
    else:
        geemap.ee_export_image(image, outfile + '.tif', scale, crs)
    t_con = time.time()-start
    print(f'总耗时:{int(t_con/3600):02d}h{int(t_con%3600/60):02d}m{int(t_con%3600%60):02d}s')


def dow(agrs):
    import geemap
    import os
    import time
    img, geo, img_count, path, scale, crs = agrs
    if not os.path.exists(path+f'/{img_count}.tif'):
        # time.sleep(img_count%30)
        geemap.ee_export_image(img, path+f'/{img_count}.tif', scale, crs, 
            region=ee.Feature(geo).geometry())
        


def merge_img(path: str, outfile, x_offset, y_offset, height, width, transform):
    """

    Args:
        path: 影像所在文件夹
        outfile: 影像的输出路径, 不包含后缀

    Returns:

    """
    import rasterio
    from rasterio.merge import merge
    import shutil
    from glob import glob

    files = glob(path + "/*.tif")
    with rasterio.open(files[0]) as src:
        out_meta = src.meta.copy()
    out_meta.update({"driver": "GTiff",
                     "height": height,
                     "width": width,
                     "compress": 'lzw',
                     "transform": transform,
                     })
    with rasterio.open(outfile + ".tif", "w", **out_meta) as dest:
        for tif_f in files:
            with rasterio.open(tif_f) as src:
                col_offset = int(src.transform[2] / scale) - x_offset
                row_offset = y_offset - int(src.transform[5] / scale)
                src_height = src.height
                src_width = src.width
                data = src.read()
            dest.write(data, window=rasterio.windows.Window(col_offset, row_offset, src_width, src_height))
    shutil.rmtree(path)

