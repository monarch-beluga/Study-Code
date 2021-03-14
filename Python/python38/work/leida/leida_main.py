
import cinrad
import numpy as np
import osr
import shapefile

path = r'F:/文件/工作/leida/'
file = path + 'Z_RADR_I_Z9250_20160701001000_O_DOR_SA_CAP.bin'
f_lei = cinrad.io.CinradReader(file)
r = f_lei.get_data(0, 400, "REF")

lon = r["longitude"].values
lat = r["latitude"].values
var = r['REF'].values
point = np.array([lon, lat]).transpose(1, 2, 0).tolist()

data_address = "F:/leida.shp"
file = shapefile.Writer(data_address)

file.field('REF', 'F', 31, decimal=4)

for i in range(len(var)-1):
    for j in range(len(var[0])-1):
        if ~np.isnan(var[i][j]):
            file.poly([[point[i][j], point[i][j+1], point[i+1][j+1],
                        point[i+1][j]]])
            file.record(var[i][j])

file.close()

proj = osr.SpatialReference()
proj.ImportFromEPSG(4326)
wkt = proj.ExportToWkt()
# 写入投影
f = open(data_address.replace(".shp", ".prj"), 'w')
f.write(wkt)
f.close()
