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
    half_window = window_size // 2
    order_range = ee.List.sequence(0, order)
    k_range = ee.List.sequence(-half_window, half_window)
    b = ee.Array(k_range.map(lambda k: order_range.map(lambda o: ee.Number(k).pow(o))))
    m_pi = ee.Array(b.matrixPseudoInverse())
    impulse_response = (m_pi.slice(**{'axis': 0, 'start': deriv, 'end': deriv + 1})).project([1])
    y0 = y.get(0)
    first_filling = y.slice(1, half_window + 1).reverse().map(
        lambda e: ee.Number(e).subtract(y0).abs().multiply(-1).add(y0))
    y_end = y.get(-1)
    last_filling = y.slice(-half_window - 1, -1).reverse().map(
        lambda e: ee.Number(e).subtract(y_end).abs().add(y_end))
    y_ext = first_filling.cat(y).cat(last_filling)
    run_length = ee.List.sequence(0, y_ext.length().subtract(window_size))
    smooth = run_length.map(
        lambda i: ee.Array(y_ext.slice(ee.Number(i), ee.Number(i).add(window_size))).multiply(impulse_response).reduce(
            "sum", [0]).get([0])
    )
    return smooth


def sg_images(images: ee.ImageCollection, window_size: int, order: int, deriv=0) -> list:
    """
    基于影像的sg滤波处理
    Args:
        images: ee.ImageCollection, 需要处理的影像集, 注意请影像集中的每张影像的波段应处理为只有一个波段
        window_size: int, 窗口大小, 最好为奇数
        order: int, 多项式阶数, 必须小于window_size
        deriv: int, 求导数的阶数, 默认为0

    Returns: list, 包含滤波处理后的image的list

    """
    half_window = window_size // 2
    order_range = ee.List.sequence(0, order)
    k_range = ee.List.sequence(-half_window, half_window)
    b = ee.Array(k_range.map(lambda k: order_range.map(lambda o: ee.Number(k).pow(o))))
    m_pi = ee.Array(b.matrixPseudoInverse())
    impulse_response = (m_pi.slice(**{'axis': 0, 'start': deriv, 'end': deriv + 1})).project([1])
    y = images.sort('system:time_start', False).toBands().toArray()
    times = images.aggregate_array('system:time_start')
    ids = images.aggregate_array('system:id')
    y1 = images.sort('system:time_start', True).toBands().toArray()
    y0 = y1.arrayGet(0)
    first_filling = y.arraySlice(0, -half_window - 1, -1).subtract(y0).abs().multiply(-1).add(y0)
    y_end = y.arrayGet(0)
    last_filling = y.arraySlice(0, 1, half_window + 1).subtract(y_end).abs().add(y_end)
    y_ext = first_filling.arrayCat(y1, 0).arrayCat(last_filling, 0)
    run_length = ee.List.sequence(0, images.size().subtract(1))
    smooth = []
    for i in run_length.getInfo():
        smooth.append(ee.Image(y_ext.arraySlice(0, i, i + window_size)
                               .multiply(impulse_response).arrayReduce("sum", [0]).arrayGet([0])
                               .set({'system:time_start': times.get(i), 'system:id': ids.get(i)})))
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
    # qa = img.select('pixel_qa')                         # 特定的landsat 影像才有这一波段
    qa = img.select('QA_PIXEL')
    cloud_state = bitwise_extract(qa, 5)  # 云掩码
    cloud_shadow_state = bitwise_extract(qa, 3)  # 云影掩码
    mask = cloud_state.eq(0).And(cloud_shadow_state.eq(0))
    return img.updateMask(mask)


def rm_cloud_s2_sr(image):
    qa = image.select('QA60')
    cloud_bit_mask = 1 << 10
    cirrus_bit_mask = 1 << 11
    mask = qa.bitwiseAnd(cloud_bit_mask).eq(0).And(qa.bitwiseAnd(cirrus_bit_mask).eq(0))
    return image.updateMask(mask)


def sample_points_to_list(img, ps):
    ps_data = img.sampleRegions(ps,
                                geometries=True,
                                scale=img.projection().nominalScale())
    values_list = [f['properties'] for f in ps_data.getInfo()["features"]]
    return values_list


def sample_points_to_df(img, ps, col_names=None):
    import pandas as pd

    values_list = sample_points_to_list(img, ps)
    if col_names is None:
        values_df = pd.DataFrame(values_list)
    else:
        values_df = pd.DataFrame(values_list)[col_names]
    return values_df
