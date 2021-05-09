
import requests
from osgeo import osr
import shapefile

data_address = r'E:\Data\地图数据\中国行政区.shp'
file = shapefile.Writer(data_address)
file.field('ProvinceName', 'C', '40')
file.field('Name', 'C', '40')
key = r'2e49c5e1b5c8d7331a3f25cf0166fceb'
keywords = '中国'
subdistrict = '1'
output = 'json'
extensions = 'base'
u = 'https://restapi.amap.com/v3/config/district?key={0}&keywords={1}&subdistrict={2}&output={3}&extensions={4}'
url = u.format(key, keywords, subdistrict, output, extensions)
r = requests.get(url)
s = r.json()
for i in s['districts'][0]['districts']:
    url1 = u.format(key, i['name'], '0', output, 'all')
    r1 = requests.get(url1)
    s1 = r1.json()
    ploy = s1['districts'][0]['polyline'].split('|')
    for px in ploy:
        ps = []
        for p in px.split(';'):
            ps.append([float(p.split(',')[0]), float(p.split(',')[1])])
        file.poly([ps])
        file.record(s['districts'][0]['name'], i['name'])
file.close()
proj = osr.SpatialReference()
proj.ImportFromEPSG(4326)
wkt = proj.ExportToWkt()
f = open(data_address.replace(".shp", ".prj"), 'w')
f.write(wkt)
f.close()

