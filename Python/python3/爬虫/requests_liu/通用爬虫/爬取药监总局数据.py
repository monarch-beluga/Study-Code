
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = r'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
kw = input('enter keyword:')
data = {
    'on': 'true',
    'page': '1',        # 爬取第二页，可以设置动态变量
    'pageSize': '15',
    'productName': kw,  # 按关键值爬取
    'conditionType': '2',   # 设置关键词检索方式
    'applyname': '',
    'applysn': ''
}
r_text = requests.post(url=url, data=data, headers=headers).json()
outpath = 'E:/temp/爬虫/requests/药监局/'
with open(outpath + kw + '-药监局.json', 'w', encoding='utf-8') as f:
    for page in range(1, r_text['pageCount']+1):
        data1 = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': kw,
            'conditionType': '2',
            'applyname': '',
            'applysn': ''
        }
        r = requests.post(url=url, data=data1, headers=headers).json()
        for i in r['list']:
            j = list(i.values())
            post_url = r'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
            data2 = {
                'id': j[0]
            }
            page_json = requests.post(url=post_url, data=data2, headers=headers).json()
            json.dump(page_json, f, ensure_ascii=False, indent=2)
print('end')
