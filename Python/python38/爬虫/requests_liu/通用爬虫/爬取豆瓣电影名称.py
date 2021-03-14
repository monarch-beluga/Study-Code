
import requests
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
get_url = r'https://movie.douban.com/j/chart/top_list'
start = input('enter start:')
end = input('enter end:')
limit = int(end) - int(start)
param = {
    'interval_id': '100:90',
    'type': '24',
    'action': '',
    'start': start,
    'limit': str(limit)
}
get_r = requests.get(url=get_url, params=param, headers=headers)
list_obj = get_r.json()
df = pd.DataFrame(list_obj)

# df.to_csv()

