
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = r'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
kw = input('enter keyword：')
data = {
    'keyword': kw,
    'pageIndex': '1',
    'pageSize': '10',
    'cname': '',
    'pid': ''
}
post_r = requests.post(url=url, data=data, headers=headers).json()
data1 = {
    'keyword': kw,
    'pageIndex': '1',
    'pageSize': post_r['Table'][0].values(),
    'cname': '',
    'pid': ''
}
r_text = requests.post(url=url, data=data1, headers=headers).json()
outpath = 'E:/temp/爬虫/requests/kfc/'
with open(outpath + kw + 'kfc.json', 'w', encoding='utf-8') as f:
    json.dump(r_text, f, ensure_ascii=False, indent=2)
# for i in r_text['Table1']:
#     j = list(i.values())
#     print(j)
print('end')

