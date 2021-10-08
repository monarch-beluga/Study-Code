
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
get_url = r'https://pcw-api.iqiyi.com/album/album/fytoplist'
param = {
    'type': 'realTime',
    'dim': 'hour',
    'cid': '1',
    'size': '25',
    'page': '1'
}
get_r = requests.get(url=get_url, params=param, headers=headers)
dic_obj = get_r.json()
df = pd.DataFrame(dic_obj['data'])

