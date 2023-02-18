
# 爬取网址：https://www.shicimingju.com/book/sanguoyanyi.html
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 Safari/537.36 '
}
get_url = "https://www.shicimingju.com/book/sanguoyanyi.html"
page_text = requests.get(url=get_url, headers=headers).text
page_soup = BeautifulSoup(page_text, 'lxml')
# print(soup.select('.book-mulu a')[0])
outpath = 'E:/temp/爬虫/requests/三国演义/'
# fp = open(outpath + '三国演义（全集）.txt', 'w', encoding='utf-8')
for label in page_soup.select('.book-mulu a'):
    title = label.text
    content_url = 'https://www.shicimingju.com' + label['href']
    content_text = requests.get(url=content_url, headers=headers).text
    content_soup = BeautifulSoup(content_text, 'lxml')
    content_label = content_soup.find('div', class_='chapter_content')
    content = content_label.text
    with open(outpath + '分章/' + title + '.txt', 'w', encoding='utf-8') as fp:
        fp.write(title + content)
    print(title, "爬取成功")
# fp.close()
print('end')
