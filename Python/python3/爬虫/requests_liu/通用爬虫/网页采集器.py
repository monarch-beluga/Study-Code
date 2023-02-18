
import requests

# 进行UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = r'https://www.sogou.com/web'
# 处理url携带参数
query = input('输入搜索词：')
param = {
    'query': query
}
r = requests.get(url=url, params=param, headers=headers)
page_text = r.text
outpath = 'E:/temp/爬虫/requests/'
filename = query + '.html'
with open(outpath + filename, 'w', encoding='utf-8') as f:
    f.write(page_text)
print('end')

