# -*- coding:utf-8 _*-
"""
author: monarch
@time:  2023/2/2
@file:  clip_dow_merge.py
"""
import ee


def clip_big_image(geo: ee.Geometry, image: ee.Image, scale: int, data_type_bytes: int,
                   crs='EPSG:4326', max_bytes=40000000):
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
    image_pro = image.reproject(**{'crs': crs, 'scale': scale}).clip(geo).getInfo()
    bands = image_pro['bands'][0]
    height = bands['dimensions'][1]
    width = bands['dimensions'][0]
    crs_transform = bands['crs_transform']
    scale = crs_transform[0]
    bounds = image_pro['properties']['system:footprint']['coordinates']

    # bands = image.bandNames().size().getInfo()
    poy = np.array(bounds[0])
    min_x = poy[:, 0].min()
    max_x = poy[:, 0].max()
    min_y = poy[:, 1].min()
    max_y = poy[:, 1].max()

    x_offset = min_x // scale
    y_offset = max_y // scale + 1
    # height = y_offset - int(min_y / scale)
    # width = int(max_x / scale) - x_offset + 1
    transform = [scale, 0, x_offset * scale, 0, -scale, y_offset * scale]

    x_interval = max_x - min_x
    y_interval = max_y - min_y
    max_region = max_bytes / (data_type_bytes * 2)
    region_area = height * width
    if max_region > region_area:
        print("不需要裁剪，可直接下载")
        return None, None, None, None, None, None
    else:
        sep_scale = math.sqrt(region_area // max_region + 1)
        sep_x = x_interval / sep_scale
        sep_y = y_interval / sep_scale
        # if x_interval < max_length:
        #     sep_x = x_interval
        #     sep_y = max_region / x_interval
        # if y_interval < max_length:
        #     sep_y = y_interval
        #     sep_x = max_region / y_interval
        p_x = np.arange(min_x, max_x, sep_x).tolist() + [max_x]
        p_y = np.arange(min_y, max_y, sep_y).tolist() + [max_y]
        polys = []
        for i in range(len(p_x) - 1):
            for j in range(len(p_y) - 1):
                poly = ee.Geometry(
                    ee.Geometry.Rectangle([float(p_x[i]), float(p_y[j]), float(p_x[i + 1]), float(p_y[j + 1])]),
                    ee.Projection(crs), False)
                polys.append(poly)
        return polys, x_offset, y_offset, height, width, transform


# def dow_Collection(image, ee_polys, count, path, scale, crs, max_worker=1):
#     from concurrent.futures import ThreadPoolExecutor
#     with ThreadPoolExecutor(max_worker) as pool:
#         pool.map(dow, [[image, ee_polys.get(i), i, path, scale, crs] for i in range(count)])


def clip_dow_merge(geo: ee.Geometry, image: ee.Image, outfile: str, scale: int,
                   data_type_bytes: int, crs='EPSG:4326', max_bytes=40000000, max_worker=1, flag=True):
    """

    Args:
        flag:
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
    start = time.time()
    polys, x_offset, y_offset, height, width, transform = clip_big_image(geo, image, scale, data_type_bytes, crs,
                                                                         max_bytes)
    if polys:
        ee_polys = ee.FeatureCollection(polys).filterBounds(geo)
        count = ee_polys.size().getInfo()
        ee_polys_list = ee_polys.toList(count)
        # clip_images = ee.ImageCollection(ee_polys.map(lambda x: image.clip(x.geometry()))).toList(count)
        print("影像切割完毕！！！")
        path = outfile + '_mk'
        if not os.path.exists(path):
            os.makedirs(path)
        files = len(glob(path + "/*.tif"))
        # print(f"需要下载的影像数: {count-files}\n")
        # dow_Collection(image, ee_polys.toList(count), count, path, scale, crs)
        while files != count:
            print(f"需要下载的影像数: {count - files}\n")
            # dow_Collection(clip_images, count, path, scale, crs)
            for i in range(count):
                dow([image, ee_polys_list.get(i), i, path, scale, crs])
            # dow_Collection(image, ee_polys_list, count, path, scale, crs, max_worker)
            files = len(glob(path + "/*.tif"))
        if flag:
            merge_img(path, outfile, x_offset, y_offset, height, width, transform)
    else:
        geemap.ee_export_image(image, outfile + '.tif', scale, crs)
    t_con = time.time() - start
    print(f'总耗时:{int(t_con / 3600):02d}h{int(t_con % 3600 / 60):02d}m{int(t_con % 3600 % 60):02d}s')


def dow(agrs):
    import geemap
    import os
    import time
    img, geo, img_count, path, scale, crs = agrs
    geo = ee.Feature(geo).geometry()
    if not os.path.exists(path + f'/{img_count}.tif'):
        # time.sleep(img_count%30)
        geemap.ee_export_image(img.clip(geo), path + f'/{img_count}.tif', scale, crs=crs,
                               region=geo)


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
    scale = transform[0]
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
                row_start = 0
                row_end = src_height
                col_start = 0
                col_end = src_width
            if row_offset < 0:
                row_start = -row_offset
                src_height += row_offset
                row_offset = 0
            elif row_offset + src_height > height:
                src_height -= row_offset + src_height - height
                row_end = src_height
            if col_offset < 0:
                col_start = -col_offset
                src_width += col_offset
                col_offset = 0
            elif col_offset + src_width > width:
                src_width -= col_offset + src_width - width
                col_end = src_width
            # print(tif_f)
            dest.write(data[:, int(row_start):int(row_end), int(col_start):int(col_end)],
                       window=rasterio.windows.Window(col_offset, row_offset, src_width, src_height))
    shutil.rmtree(path)
