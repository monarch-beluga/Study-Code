# coding=utf-8
import arcpy
import os
from arcpy.sa import *


arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = r'E:\pybook\MeteoGrid\tmean_year'
# arcpy_liu.env.scratchWorkspace = r'E:\pybook\MeteoGrid' + os.sep +'tmean_year'
rasterlist = arcpy.ListRasters('TAVG' + '*', 'tif')
rasterlistout = r'E:\pybook\MeteoGrid\tmean_year' + os.sep + 'TAVG_MEAN.tif'
outCellStatistics = CellStatistics(rasterlist, 'MEAN', "DATA")
outCellStatistics.save(rasterlistout)
print(rasterlistout)
fvars = ['tmean_year', 'prcp_mean']
for v in fvars:
    if v == 'tmean_year':
        i = 'TAVG_MEAN'
        x = 'TAVG_county'
        func = 'MEAN'
    else:
        i = 'prcp_meanMEAN'
        x = 'prcp_county'
        func = 'MEAN'
    arcpy.env.workspace = r'E:\pybook\MeteoGrid' + os.sep + v
    inValueRaster = r'E:\pybook\MeteoGrid' + os.sep + v + os.sep + i + '.tif'
    outTable = r'E:\pybook\MeteoGrid' + os.sep + x + os.sep + x + func + '.dbf'
    # Set local variables
    # inZoneData = "zones.shp"
    # zoneField = "Classes"
    # inValueRaster = "valueforzone"
    # outTable = "zonalstattblout02.dbf"
    print(outTable)
    inZoneData = r'E:\pybook\MeteoGrid\qinghai_boundary\qinghai_county.shp'
    zoneField = 'NAME'
    outZSaT = ZonalStatisticsAsTable(
        inZoneData,
        zoneField,
        inValueRaster,
        outTable,
        "DATA",
        func)
