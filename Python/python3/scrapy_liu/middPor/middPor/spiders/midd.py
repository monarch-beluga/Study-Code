import scrapy


class MiddSpider(scrapy.Spider):
    name = 'midd'
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response, **kwargs):
        page_text = response.text

        with open('E:/temp/爬虫/scrapy/ip.html', 'w', encoding='utf-8') as fp:
            fp.write(page_text)


