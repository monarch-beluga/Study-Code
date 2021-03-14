import scrapy
from ..items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response, **kwargs):
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []
    #     for div in div_list:
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         response.body.decode('utf-8')
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         # author = author.strip()
    #         content = content.strip('\n')
    #         dic = {
    #             'author': author,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #     return all_data
    def parse(self, response, **kwargs):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            author = author.strip()
            content = ''.join(content)
            content = content.strip('\n')

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item

