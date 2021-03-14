import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunporItem, PageItem
# from scrapy_redis.spiders import RedisCrawlSpider


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pic.netbian.com/']
    # redis_key = 'sun'

    link = LinkExtractor(allow=r'index[_]?[2]?\.html')
    link_page = LinkExtractor(allow=r'tupian/\d+\.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_page, callback='parse_page', follow=False),
    )

    def parse_item(self, response):
        print(response)
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            page_url = li.xpath('./a/@href').extract_first()
            item = SunporItem()
            item['page_url'] = page_url
            yield item

    def parse_page(self, response):
        title = response.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()').extract_first()
        item = PageItem()
        item['title'] = title
        yield item
        # print(title)


