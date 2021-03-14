
from osgeo import gdal, osr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll


def Write(file, data, ds, tr):
    driver = gdal.GetDriverByName('GTiff')
    Size = data.shape
    out_ds = driver.Create(
        file,
        Size[1],
        Size[0],
        1,
        gdal.GDT_Float32)

    out_ds.SetProjection(ds.ExportToWkt())
    out_ds.SetGeoTransform(tr)
    for i in range(1, 2):
        out_band = out_ds.GetRasterBand(i)
        out_band.WriteArray(data)
    out_ds.FlushCache()
    del out_ds


# C = np.loadtxt(fname='F:/文件/工作/leida/data_txt/ref.txt', delimiter='\t')
# Y = np.loadtxt(fname='F:/文件/工作/leida/data_txt/r_lat.txt', delimiter='\t')
# X = np.loadtxt(fname='F:/文件/工作/leida/data_txt/r_lon.txt', delimiter='\t')
# Ny, Nx = X.shape
# X = X.ravel()
# Y = Y.ravel()
# C = C.ravel()
#
#
# lonmin, latmax, lonmax, latmin = [lon.min(), lat.max(), lon.max(), lat.min()]
# lon_d = ((lon - lonmin) // ((lonmax - lonmin)/400)).astype('int')
# lat_d = ((lat - latmin) // ((latmax - latmin)/400)).astype('int')

# data = np.full([400, 400], dtype=float, fill_value=np.nan)
# for i in range(0, 366):
#     for j in range(0, 400):
#         x = lon_d[i][j]
#         y = lat_d[i][j]
#         r = r_data[i][j]
#         data[y][x] = r
# lon_c = lon.flatten()
# lat_c = lat.flatten()
# r_c = r_data.flatten()
# p = Proj(proj='utm', zone=12, ellps='WGS84', preserve_units=False)
# lon_d, lat_d = p(lon, lat)
# lonmin, latmax, lonmax, latmin = [lon_c_m.min(), lat_c_m.max(), lon_c_m.max(), lat_c_m.min()]
# d = {'x': lon_c, 'y': lat_c, 'value': r_c}
# data = pd.DataFrame(d)
# data1 = data.sort_values(by=['y'])
# a = []
# for i in range(400):
#     a += [i] * 366
# data1['col'] = a
# data2 = data1.sort_values(by=['col', 'x'])
# data_r = data2['value'].values.reshape([400, 366])
# lon_data = data2['x'].values.reshape([400, 366])
# lat_data = data2['y'].values.reshape([400, 366])
# lonmin, latmax, lonmax, latmin = [lon_data.min(), lat_data.max(), lon_data.max(), lat_data.min()]
# lon_d = ((lon_data - lonmin) // ((lonmax - lonmin)/366)).astype('int')
# lat_d = ((lat_data - latmin) // ((latmax - latmin)/400)).astype('int')
#
# data = np.full([400, 366], dtype=float, fill_value=np.nan)
# for i in range(0, 400):
#     for j in range(0, 366):
#         x = lon_d[i][j]
#         y = lat_d[i][j]
#         r = data_r[i][j]
#         data[x][y] = r
# fig = plt.figure()
# plt.imshow(data_r)
# data.to_csv("data.txt", sep='\t')
# Size = r_data.shape
# lon_ce = (lonmax - lonmin)/Size[1]
# lat_ce = (latmax - latmin)/Size[0]
# geotransform1 = [lonmin, lon_ce, 0, latmin, 0, lat_ce]
# geo1 = osr.SpatialReference()
# geo1.ImportFromEPSG(4326)
# Write('F:/文件/工作/leida/data_txt/ref1.tif', data3, geo1, geotransform1)
