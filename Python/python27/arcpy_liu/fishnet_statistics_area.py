# -*- coding: utf-8 -*-
# @Time    : 2024/3/28 18:08
# @Author  : Monarch
# @File    : fishnet_statistics_area.py
# @Software: PyCharm

import arcpy
import math
import os

path = r'D:\Work\Australia_p41'
os.chdir(path)
arcpy.env.workspace = path
arcpy.env.overwriteOutput = True

# 输入为湿地矢量
mudflat_shp = r'Australia_p41_mudflat_10m_2022_clip_new.shp'

# 输出文件位置
out_fishnet_file = r'Australia_p41_mudflat_10m_2022_clip_new_fishnet.shp'
out_intersect = r'Australia_p41_mudflat_10m_2022_clip_new_intersect.shp'
out_intersect_pro = r'Australia_p41_mudflat_10m_2022_clip_new_intersect_pro.shp'
out_intersect_dissolve = r'Australia_p41_mudflat_10m_2022_clip_new_intersect_dissolve.shp'

# 网格大小
cell_width = 0.5
cell_height = 0.5

# 计算网格起点
mudflat = arcpy.Describe(mudflat_shp)
extent = mudflat.extent
lower_left = extent.lowerLeft
upper_right = extent.upperRight

origin_coord = str(math.floor(lower_left.X)) + ' ' + str(math.floor(lower_left.Y))
orient_coord = str(math.floor(lower_left.X)) + ' ' + str(math.floor(lower_left.Y + 10))

# 修复几何
arcpy.RepairGeometry_management(mudflat_shp, "KEEP_NULL")

# 创建网格
arcpy.CreateFishnet_management(out_fishnet_file, origin_coord, orient_coord, cell_width=cell_width,
                               cell_height=cell_height, template=mudflat_shp, labels="NO_LABELS", geometry_type="POLYGON")

# 用于融合、连接的字段与FID对应
arcpy.CalculateField_management(out_fishnet_file, 'id', "!FID!", "PYTHON_9.3")

# 相交
arcpy.Intersect_analysis([out_fishnet_file, mudflat_shp], out_intersect, join_attributes="NO_FID")

# 投影为EPSG:3857 用于计算面积
arcpy.Project_management(out_intersect, out_intersect_pro, arcpy.SpatialReference(3857))

# 融合
arcpy.Dissolve_management(out_intersect_pro, out_intersect_dissolve, "id")

# 计算面积单位为平方米
arcpy.AddField_management(out_intersect_dissolve, "Area", "DOUBLE")
arcpy.CalculateField_management(out_intersect_dissolve, 'Area', "!shape.area!", "PYTHON_9.3")

# 属性连接
arcpy.JoinField_management(out_fishnet_file, "id", out_intersect_dissolve, 'id', ['Area'])

