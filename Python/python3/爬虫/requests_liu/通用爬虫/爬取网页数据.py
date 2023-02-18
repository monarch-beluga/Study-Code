# 爬取搜狗首页页面数据
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
url = r'https://api-zero.livere.com/v1/comments/list?callback=jQuery112408493283337889896_1603935607545&limit=10' \
      r'&offset=4&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq' \
      r'=5154&code=&_=1603935607550'     # 指定url
r = requests.get(url=url, headers=headers)           # 发起请求，get会返回一个响应对象
sogou_text = r.text                 # 获取响应数据

with open(r'E:\temp\爬虫\requests\hello-world-p.html', 'w', encoding='utf-8') as f:
    f.write(sogou_text)
print('end')




