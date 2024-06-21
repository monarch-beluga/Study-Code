# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 10:27
# @Author  : Monarch
# @File    : RasterToPoly.py
# @Software: PyCharm

from osgeo import gdal, ogr, osr
import os


def raster2poly(raster, outshp):
    ds = gdal.Open(raster)  # 读取路径中的栅格数据
    band = ds.GetRasterBand(1)  # 这个波段就是最后想要转为矢量的波段，如果是单波段数据的话那就都是1
    prj = osr.SpatialReference()
    prj.ImportFromWkt(ds.GetProjection())  # 读取栅格数据的投影信息，用来为后面生成的矢量做准备

    drv = ogr.GetDriverByName("ESRI Shapefile")
    if os.path.exists(outshp):  # 若文件已经存在，则删除它继续重新做一遍
        drv.DeleteDataSource(outshp)
    polygon = drv.CreateDataSource(outshp)  # 创建一个目标文件
    poly_layer = polygon.CreateLayer(raster[:-4], srs=prj, geom_type=ogr.wkbMultiPolygon)  # 对shp文件创建一个图层，定义为多个面类
    new_field = ogr.FieldDefn('value', ogr.OFTReal)  # 给目标shp文件添加一个字段，用来存储原始栅格的pixel value
    poly_layer.CreateField(new_field)

    gdal.FPolygonize(band, None, poly_layer, 0)  # 核心函数，执行的就是栅格转矢量操作
    polygon.SyncToDisk()


os.chdir(r'D:\Work\Australia_p4_mangrove_2022_setnull')
raster2poly(r'Australia_p4_mangrove_2022_setnull.tif', "Australia_p4_mangrove_2022.shp")

