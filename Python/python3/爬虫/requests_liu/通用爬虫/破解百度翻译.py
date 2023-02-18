
import requests
# import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
# 指定post请求的url
post_url = r'https://fanyi.baidu.com/sug'
kw = input("输入单词：")
# data为post请求参数处理
data = {
    'kw': kw
}
# 发送post请求
post_r = requests.post(url=post_url, data=data, headers=headers)
# 获取响应数据（这里服务器端响应的是json数据）
# 使用json()时要确定响应数据为json数据（在抓包工具的response headers的content-type中）
# 这里返回的是一个字典数据
# text()可以适用于所有数据
dic_obj = post_r.json()
for i in dic_obj['data']:
    print(i)
# print(dic_obj)
# outpath = 'E:/temp/爬虫/requests/'
# filename = kw + '.json'
# with open(outpath + filename, 'w', encoding='utf-8') as f:
#     json.dump(dic_obj, f, ensure_ascii=False)
print('end')
