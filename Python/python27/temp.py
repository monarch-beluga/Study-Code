# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import arcpy
import os

# 获取当前工作路径
path1 = os.getcwd()
print(U"当前工作路径为: %s" % path1)

# 设置当前arcpy工具输入和输出的工作环境
arcpy.env.workspace = U"D:\\Public\\data"
# 设置环境可以覆盖文件夹内存在的数据
arcpy.env.overwriteOutput = True

# 更改工作路径
path2 = "D:\\Public\\data"    # 设置工作路径
os.chdir(path2)
path3 = os.getcwd()
print(U"更改后工作路径为: %s" % path3)

# ---------------------------------------------------------------------------
# 输入数据：
# 1、取水口点数据
# 2、国土三调土地利用现状数据
# 3、分水岭数据
# 4、地区栅格数据
# 数据路径
point_path = U"point.shp"    # 取水口点数据
sd_path = U"国土三调土地利用现状.shp"    # 国土三调土地利用现状数据
fsl_path = U"分水岭.shp"    # 分水岭数据
data_img = U"地区.tif"    # 地区栅格数据

# ---------------------------------------------------------------------------
# 输出数据:
# 输出路径:
# 统一投影数据
po_prj = U"po_prj.shp"    # 投影取水口数据
sd_prj = U"sd_prj.shp"    # 投影国土三调土地利用现状数据
fsl_prj = U"fsl\\fsl_prj.shp"    # 投影分水岭数据

# 裁剪要素
sd_clip_1000 = U"buf\\sd_clip_1000.shp"    # 裁剪取水口1000米缓冲区的国土三调土地利用现状数据
sd_clip_1100 = U"buf\\sd_clip_1100.shp"    # 裁剪取水口1100米缓冲区的国土三调土地利用现状数据
CE_line_buf_clip = U"center_line\\CE_line_buf_clip.shp"    # 裁剪河流中心线缓冲区超过取水口1000米缓冲区的部分

# 道路数据
rode_path = U"rode\\rode.shp"    # 农村道路数据
rode_line = U"rode\\rode_line.shp"    # 农村道路转线
rode_dis = U"rode\\rode_dis.shp"    # 融合农村道路
rode_line_clip = U"rode\\rode_line_clip.shp"    # 裁剪河流中心线缓冲区内的农村道路
rode_merge = U"rode\\rode_merge.shp"    # 农村道路与河流中心线缓冲区的合并线
rode_and_buf_dis = U"rode\\rode_and_buf_dis.shp"    # 融合农村道路与河流中心线缓冲区的合并线

# 河流数据
HL_1000_path = U"hl\\HL_1000.shp"    # 1000米河流
HL_1100_path = U"hl\\HL_1100.shp"    # 1100米河流
HL_JX_1000 = U"hl\\HL_JX_1000.shp"    # 生成河流线段
HL_simp = U"hl\\HL_simp.shp"    # 简化河流线

# 河流中心线
CE_path1 = U"center_line\\HL_CE_line1.shp"    # 提取河流中心线1
CE_path2 = U"center_line\\HL_CE_line2.shp"    # 提取河流中心线2
CE_line_end = U"center_line\\CE_line_end.shp"    # 提取过程最终所需的河流中心线

# 获取交点
buf_100_JX_line = U"center_line\\buf_100_JX_line.shp"    # 河流中心线与100米缓冲区的交线
start_and_end_point = U"center_line\\start_and_end_point.shp"    # 河流中心线与100米缓冲区的两个交点
point_JD = U"point_JD.shp"    # 两个交点取下游端点
CE_line_join = U"center_line\\CE_line_join.shp"    # 下游端点与河流中心线链接

# buffer
CE_line_buf = U"center_line\\CE_line_buf.shp"    # 中心线生成的缓冲区
CE_buf_line = U"center_line\\CE_buf_line.shp"    # 中心线生成的缓冲区转线
CX_line = U"CX_line.shp"    # 下游端点到河流一端的线
CX_line_extend = U"CX_line_merge.shp"    # 切割线

# 分水岭
fsl_line = U"fsl\\fsl_line.shp"    # 分水岭转线
fsl_clip = U"fsl\\fsl_clip.shp"    # 裁剪缓冲区内的分水岭
fsl_and_hl = U"fsl\\fsl_and_hl.shp"    # 分水岭与河流的交线
fsl_del_hl = U"fsl\\fsl_del_hl.shp"    # 分水岭去除河流的交线

# 陆域和水域
ly_line = U"ly_line.shp"    # 生成陆域的线
ly_mian = U"ly_mian.shp"    # 陆域面
sy = U"sy.shp"    # 水域
ly = U"ly.shp"    # 陆域

# 筛选陆域与水域
ly_po_join = U"ly_po_join.shp"    # 陆域与点链接
ly_select = U"ly_select.shp"    # 筛选陆域
ly_select1 = U"ly_select1.shp"    # 陆域

# 参数设置
# 缓冲区参数
buf_distance = [100, 1000, 1100]    # 100米、1000米、1100米
buf_CE_line_distance = "450 Meters"    # 河流中心线缓冲区，河流缓冲区变大，中心线缓冲区也应当变大

# 河流参数设置
hl_simple_len = "80 Meters"    # 河流简化参数
HL_agg_distance = "40 Meters"    # 河流聚合距离一般为40米

# 提取河流中心线参数
CE_line_max_width = "300 Meters"    # 提取的最大宽度
CE_line_min_width = "0 Meters"    # 提取的最小宽度
hl_len = [1000, 1100]    # 河流长度

# 临近分析参数
near_distance = "200 Meters"    # 距离河流线最近距离

# 延伸线长度参数
CX_len_extend = "900 Meters"    # 下游端点与河流最近点连线的延伸长度 注：需要大于中心线生成缓冲区的距离,尽量设大一点，一般设置为中心线缓冲区的两倍
rode_line_extend1 = "5 Meters"     # 道路延申长度
rode_line_extend2 = "80 Meters"    # 道路延伸长度(特例2) 使某一段离散的道路延伸至主道路

# 整合道路参数
rode_width = "5 Meters"    # 整合道路线宽度

# ---------------------------------------------------------------------------
# 创建文件夹
# 判断建立的文件夹是否存在
folder_name = ["buf", "fsl", "rode", "hl", "center_line"]    # 缓冲区、分水岭、道路、河流、中心线
for i in folder_name:
    if not os.path.exists(i):
        os.makedirs(i)
        print(U"该文件夹不存在，创建了%s文件夹" % i)
    else:
        print(U"该文件夹已存在，不再创建%s文件夹" % i)

# 投影
# 获取栅格数据的坐标系
spatial_ref = arcpy.SpatialReference(3857)

# 对取水口、三调、分水岭数据进行投影
arcpy.Project_management(sd_path, sd_prj, spatial_ref)
arcpy.Project_management(point_path, po_prj, spatial_ref)
arcpy.Project_management(fsl_path, fsl_prj, spatial_ref)

# 构建缓冲区
print(U"开始生成缓冲区")
# buf_distance = [100, 1000, 1100]   ## 取水口缓冲区设置
buf_lis = []    # 获取缓冲区路径

for i in buf_distance:
    buf_path = U"buf\\" + "buf_" + str(i) + ".shp"    # 生成缓冲区的路径
    distance = str(i) + " Meters"   # 生成缓冲区的距离
    buf_lis.append(buf_path)
    arcpy.Buffer_analysis(po_prj, buf_path, distance)    # 生成缓冲区
print(U"缓冲区生成完成")
# 裁剪取水点1000米和1100米内的三调数据
buf_1000_path = buf_lis[1]
buf_1100_path = buf_lis[2]

# 裁剪数据
arcpy.Clip_analysis(sd_prj, buf_1000_path, sd_clip_1000)
arcpy.Clip_analysis(sd_prj, buf_1100_path, sd_clip_1100)

# ---------------------------------------------------------------------------
print(U"开始提取河流中心线")
# 获取河流中心线
HL_shp = []    # 获取河流面要素路径
HL_line_lis = []    # 获取河流线要素路径
def HL(HL_path, sd_clip, length, po_prj, HL_agg_distance):
    # 判断筛选的字段是否存在
    try:
        arcpy.Select_analysis(sd_clip, HL_path, "\"DLBM\" = '1101'")
        print(U"筛选成功：%s" % (str(length) + U"米河流"))
    except arcpy.ExecuteError:
        print(U"ERROR: 该字段或字段值不存在")
        field_list = [field.name for field in arcpy.ListFields(sd_clip)]
        if "DLMC" in field_list:
            print(U"ERROR: 该字段存在，但字段值不存在")
        else:
            print(U"ERROR: 该字段不存在")
    # 河流融合dissolve
    HL_agg = U"hl\\" + "HL_" + str(length) + "_agg.shp"
    arcpy.AggregatePolygons_cartography(HL_path, HL_agg, HL_agg_distance)

    # 河流与点链接
    HL_join = U"hl\\" + "HL_" + str(length) + "_join.shp"
    arcpy.SpatialJoin_analysis(HL_agg, po_prj, HL_join)

    # 筛选河流
    HL_select = U"hl\\" + "HL_" + str(length) + "_select.shp"
    arcpy.Select_analysis(HL_join, HL_select, "\"Join_Count\" = 1")

    # 消除河流内部空洞
    HL_eli = U"hl\\" + "HL_" + str(length) + "_eli.shp"
    HL_shp.append(HL_eli)
    arcpy.EliminatePolygonPart_management(HL_select, HL_eli, "PERCENT", "", 99.9)

    # 河流转线
    HL_line = U"hl\\" + "HL_line" + str(length) + ".shp"
    HL_line_lis.append(HL_line)
    arcpy.FeatureToLine_management(HL_eli, HL_line)
    return

# 传入河流输出路径，三调数据被裁剪的路径，河流长度
HL(HL_1000_path, sd_clip_1000, hl_len[0], po_prj, HL_agg_distance)
HL(HL_1100_path, sd_clip_1100, hl_len[1], po_prj, HL_agg_distance)

# 获取河流线
path1 = HL_line_lis[0]
path2 = HL_line_lis[1]
arcpy.Intersect_analysis([path1, path2], HL_JX_1000, "ALL", "", "LINE")

# 简化河流线
arcpy.SimplifyLine_cartography(HL_JX_1000, HL_simp, "POINT_REMOVE", hl_simple_len, "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS", "CHECK", "")

# 提取河流中心线
arcpy.CollapseDualLinesToCenterline_cartography(HL_simp, CE_path1, CE_line_max_width, CE_line_min_width)

# 本案例特殊处理1: 清除河流空洞生成的线
# arcpy.FeatureToLine_management(CE_path1, CE_path2, "", "ATTRIBUTES")

# 筛选河流中心线
buf_100_path = buf_lis[0]
arcpy.AddField_management(buf_100_path, "select", "LONG")

# 获取河流中心线与100米buf的交线
# arcpy.Intersect_analysis([buf_100_path, CE_path2], buf_100_JX_line, "ALL", "", "LINE")
arcpy.Intersect_analysis([buf_100_path, CE_path1], buf_100_JX_line, "ALL", "", "LINE")

# 获取交线的两个端点
arcpy.FeatureVerticesToPoints_management(buf_100_JX_line, start_and_end_point, "BOTH_ENDS")
point_path = [po_prj, start_and_end_point]

# 给点添加XY坐标
for po in point_path:
    arcpy.AddXY_management(po)

# 选取下游的端点
# 下游在上，故选取最大的Y坐标值
po_Y_lis = []
with arcpy.da.SearchCursor(point_path[0], ["POINT_Y"]) as po1:
    for row in po1:
        po_Y_lis.append(row[0])
with arcpy.da.SearchCursor(point_path[1], ["POINT_Y"]) as po2:
    for row in po2:
        po_Y_lis.append(row[0])
Y_max = max(po_Y_lis)

# 选出下游端点
arcpy.Select_analysis(point_path[1], point_JD, "\"POINT_Y\" = %s" % str(Y_max))

# 特例1（续）：获取最终河流中心线
# arcpy.AddXY_management(point_JD)
# arcpy.SpatialJoin_analysis(CE_path2, point_JD, CE_line_join)

# 筛选出最终的河流中心线
# arcpy.Select_analysis(CE_line_join, CE_line_end, "\"Join_Count\" = 1")
# print(U"河流中心线提取完毕")

# 获取河流中心线生成的buffer
# arcpy.Buffer_analysis(CE_line_end, CE_line_buf, buf_CE_line_distance, "FULL", "ROUND", "ALL")
arcpy.Buffer_analysis(CE_path1, CE_line_buf, buf_CE_line_distance, "FULL", "ROUND", "ALL")

# 去除超过1000缓冲区的范围
arcpy.Clip_analysis(CE_line_buf, buf_1000_path, CE_line_buf_clip)

# 将CE_buf 转线
arcpy.FeatureToLine_management(CE_line_buf_clip, CE_buf_line)

# ---------------------------------------------------------------------------
print(U"开始生成下游分界线")
# 处理下游分界线、路/防洪堤坝、分水岭
# (1)下游分界线
# 获取下游端点与河流的最近点
arcpy.Near_analysis(point_JD, HL_JX_1000, near_distance, "LOCATION", "NO_ANGLE", "PLANAR")

# 获取下游端点到河流的线
arcpy.XYToLine_management(point_JD, CX_line, "NEAR_X", "NEAR_Y", "POINT_X", "POINT_Y", "1", "", spatial_ref)
# 合并线与河流中心线缓冲区线
arcpy.Merge_management([CX_line, CE_buf_line], CX_line_extend)

# 构建的河流中心线缓冲区为450米缓冲区，延长距离要大于缓冲区距离
arcpy.ExtendLine_edit(CX_line_extend, CX_len_extend, "EXTENSION")
print(U"下游分界线生成完毕")

# ---------------------------------------------------------------------------
print(U"处理道路数据")
# (2)路/防洪堤坝
# 优化道路/防洪堤坝
# 筛选道路及防洪堤坝
try:
    arcpy.Select_analysis(sd_clip_1000, rode_path, "\"DLBM\" = '1006'")
    print(U"道路筛选成功")
except arcpy.ExecuteError:
    print(U"ERROR: 该字段或字段值不存在")
    field_list = [field.name for field in arcpy.ListFields(sd_clip_1000)]
    if "DLMC" in field_list:
        print(U"ERROR: 该字段存在，但字段值不存在")
    else:
        print(U"ERROR: 该字段不存在")


# 面转线
arcpy.FeatureToLine_management(rode_path, rode_line)

# 融合道路dissolve
arcpy.Dissolve_management(rode_line, rode_dis)

# 整合道路
arcpy.Integrate_management(rode_dis, rode_width)

# 裁剪出中心线缓冲区内的路
arcpy.Clip_analysis(rode_dis, CE_line_buf_clip, rode_line_clip)

# 合并道路及中心线缓冲区
arcpy.Merge_management([CE_buf_line, rode_line_clip], rode_merge)

# 融合道路及中心线缓冲区
arcpy.Dissolve_management(rode_merge, rode_and_buf_dis, "FID")

# 本案例特殊处理2: 延伸 80 Meters
arcpy.ExtendLine_edit(rode_and_buf_dis, rode_line_extend2)
print(U"道路数据处理完毕")

# ---------------------------------------------------------------------------
# (3)分水岭
print(U"开始处理分水岭数据")
# 参数: 分水岭投影、分水岭转线、分水岭线裁剪、分水岭与河流交线、分水岭去除河流交线、河流1000米、河流中心线缓冲区路径
def fsl(fsl_prj, fsl_line, fsl_clip, fsl_and_hl, fsl_del_hl, hl_path, CE_line_buf_clip):
    # 分水岭转线
    arcpy.FeatureToLine_management(fsl_prj, fsl_line)

    # 裁剪出中心线缓冲区内的分水岭
    arcpy.Clip_analysis(fsl_line, CE_line_buf_clip, fsl_clip)

    # 分水岭与河流相交的部分
    arcpy.Intersect_analysis([fsl_clip, hl_path], fsl_and_hl)

    # 分水岭去掉与河流相交的部分
    arcpy.SymDiff_analysis(fsl_and_hl, fsl_line, fsl_del_hl)
    return

fsl(fsl_prj, fsl_line, fsl_clip, fsl_and_hl, fsl_del_hl, HL_shp[0], CE_line_buf_clip)
print(U"分水岭处理完成")

# ---------------------------------------------------------------------------
print(U"开始数据整合")
# 合并分水岭、路、下游分界线
arcpy.Merge_management([fsl_del_hl, CX_line_extend, rode_and_buf_dis], ly_line)

# 延伸其中的线
arcpy.ExtendLine_edit(ly_line, rode_line_extend1, "EXTENSION")

# 获取总的面
arcpy.FeatureToPolygon_management(ly_line, ly_mian)

# 筛选陆域与水域
# 空间链接点与陆域
arcpy.SpatialJoin_analysis(ly_mian, po_prj, ly_po_join)

# 筛选出陆域和水的整个区域
arcpy.Select_analysis(ly_po_join, ly_select, "\"Join_Count\" = 1")

# 相交筛选水域
arcpy.Intersect_analysis([ly_select, HL_shp[0]], sy)

# 取反得出陆域
arcpy.SymDiff_analysis(ly_select, sy, ly_select1)

# 消除陆域中可能存在的空洞
arcpy.EliminatePolygonPart_management(ly_select1, ly, "PERCENT", "", 5)
print(U"数据整合完成，陆域与水域分离")
print(U"所有数据处理完毕")

