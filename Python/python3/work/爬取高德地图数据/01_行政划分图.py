
import requests
from osgeo import osr
import shapefile

u = 'https://restapi.amap.com/v3/config/district?key={0}&keywords={1}&subdistrict={2}&output={3}&extensions={4}'


def get_poly(dis, res, k, f):
    poly_url = u.format(k, dis['adcode'], '0', 'json', 'all')
    poly_r = requests.get(poly_url)
    poly_s = poly_r.json()
    ploy = poly_s['districts'][0]['polyline'].split('|')
    for px in ploy:
        ps = []
        for p in px.split(';'):
            ps.append([float(p.split(',')[0]), float(p.split(',')[1])])
        f.poly([ps])
        f.record(*res)


def create_field(f, dis):
    f.field(dis['level'], 'C', '40')
    if dis['districts']:
        create_field(f, dis['districts'][0])


def get_districts(f, res, dis, k):
    res.append(dis['name'])
    if not dis['districts']:
        get_poly(dis, res, k, f)
    else:
        for d in dis['districts']:
            get_districts(f, res, d, k)
    res.pop()


# shp保持地址
data_address = r'D:\Work\Starfm\jiujiang.shp'

# 需要下载的最高级行政区名
keywords = '九江'
# 高德地图API的Key
key_file = r'D:\System_Path\高德地图Key\Key.txt'
with open(key_file) as fp:
    key = fp.readline()
# 返回下几级行政区
subdistrict = 0
output = 'json'
extensions = 'base'
# 使用requests进行爬取

url = u.format(key, keywords, subdistrict, output, extensions)
r = requests.get(url)
s = r.json()

file = shapefile.Writer(data_address, encoding='utf-8')
create_field(file, s['districts'][0])
get_districts(file, [], s['districts'][0], key)
file.close()

proj = osr.SpatialReference()
proj.ImportFromEPSG(4326)
wkt = proj.ExportToWkt()
fp = open(data_address.replace(".shp", ".prj"), 'w', encoding='utf-8')
fp.write(wkt)
fp.close()

