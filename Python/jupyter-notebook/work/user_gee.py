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
    x_interval = max_x - min_x
    y_interval = max_y - min_y
    max_region = max_bytes * (scale*scale) / bands / (data_type_bytes+1)
    max_length = int(math.sqrt(max_region))
    region_area = geo.area(maxError=0.1, proj=ee.Projection(crs)).getInfo()
    if max_region > region_area:
        print("不需要裁剪，可直接下载")
        return None
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
        return polys
    
    
def dow_Collection(clip_images, count, path, scale, crs):
    from concurrent.futures import ThreadPoolExecutor,  wait, ALL_COMPLETED
    import os
    if not os.path.exists(path):
        os.makedirs(path)
    print(f"Total number of images: {count}\n")
    with ThreadPoolExecutor(5) as pool:
        pool.map(dow, [[clip_images.get(i), i, path, scale, crs] for i in range(count)])

        
def clip_dow_merge(geo: ee.Geometry, image: ee.Image, outfile: str, scale: int,
                   data_type_bytes: int, crs='EPSG:3857', max_bytes=40000000):
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
    import geemap
    import time
    from glob import glob
    
    start = time.time()
    polys = clip_big_image(geo, image, scale, data_type_bytes, crs, max_bytes)
    if polys:
        ee_polys = ee.FeatureCollection(polys).filterBounds(geo)
        path = outfile + '_mk'
        count = ee_polys.size().getInfo()
        clip_images = ee.ImageCollection(ee_polys.map(lambda x: image.clip(x.geometry()))).toList(count)
        dow_Collection(clip_images, count, path, scale, crs)
        # geemap.ee_export_image_collection(clip_images, path, scale, crs)
        files = glob(path+"/*.tif")
        while len(files) != count:
            dow_Collection(clip_images, count, path, scale, crs)
        merge_img(path, outfile)
        print("下载成功 !!!")
    else:
        geemap.ee_export_image(image, outfile + '.tif', scale, crs)
    t_con = time.time()-start
    print(f'总耗时:{int(t_con/3600):02d}h{int(t_con%3600/60):02d}m{int(t_con%3600%60):02d}s')


def dow(agrs):
    import geemap
    import os
    img, img_count, path, scale, crs = agrs
    if not os.path.exists(path+f'/{img_count}.tif'):
        geemap.ee_export_image(ee.Image(img), path+f'/{img_count}.tif', scale, crs)


def merge_img(path: str, outfile):
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
    with rasterio.open(outfile + ".tif", "w", **out_meta) as dest:
        dest.write(mosaic)
    for src in src_files_to_mosaic:
        src.close()
    shutil.rmtree(path)

