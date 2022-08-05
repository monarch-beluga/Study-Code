
import requests
from osgeo import osr
import shapefile
import math

data_address = r'E:\Data\地图数据\飞机场.shp'
file = shapefile.Writer(data_address)
file.field('ProvinceName', 'C', '40')
file.field('CityName', 'C', '40')
file.field('AdName', 'C', '40')
file.field('Name', 'C', '40')

key = r''
keywords = '中国'
subdistrict = '1'
output = 'json'
extensions = 'base'
u = 'https://restapi.amap.com/v3/config/district?key={0}&keywords={1}&subdistrict={2}&output={3}&extensions={4}'
url = u.format(key, keywords, subdistrict, output, extensions)
r = requests.get(url)
s = r.json()
for i in s['districts'][0]['districts']:
    u1 = 'https://restapi.amap.com/v3/place/text?key={0}&city={1}&keywords={2}&output={3}&page={4}'
    url1 = u1.format(key, i['name'], '飞机场', output, 1)
    r1 = requests.get(url1)
    s1 = r1.json()
    for j in range(1, math.ceil(int(s1['count']) / 20)+1):
        url2 = u1.format(key, i['name'], '飞机场', output, j)
        r2 = requests.get(url2)
        s2 = r2.json()
        for k in s2['pois']:
            file.point(float(k['location'].split(',')[0]), float(k['location'].split(',')[1]))
            file.record(k['pname'], k['cityname'], k['adname'], k['name'])
file.close()
proj = osr.SpatialReference()
proj.ImportFromEPSG(4326)
wkt = proj.ExportToWkt()
f = open(data_address.replace(".shp", ".prj"), 'w')
f.write(wkt)
f.close()

