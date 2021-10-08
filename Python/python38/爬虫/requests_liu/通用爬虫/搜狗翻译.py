
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
post_url = r'https://fanyi.sogou.com/reventondc/suggV3'
word = input('enter in word:')
data1 = {
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'wap',
    'text': word,
    'uuid': '0ce410c4-9ca4-4b48-89b4-5312e2af1c40',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
}
r = requests.post(url=post_url, data=data1, headers=headers)
dic_obj = r.json()
for i in dic_obj['sugg']:
    print(i)

