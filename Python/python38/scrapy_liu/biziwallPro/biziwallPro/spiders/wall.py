import scrapy
from ..items import BiziwallproItem


class WallSpider(scrapy.Spider):
    name = 'wall'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wallhaven.cc/search?q=id%3A5&categories=111&purity=110&atleast=1920x1080&ratios=16x9&sorting=relevance&order=desc']

    page_num = 1
    url = 'https://wallhaven.cc/search?q=id%3A5&categories=111&purity=110&atleast=1920x1080&ratios=16x9&sorting=relevance&order=desc&page={0}'

    def parse_url(self, response):
        item = response.meta['item']
        img_url = response.xpath('//*[@id="wallpaper"]/@src').extract_first()
        item['img_url'] = img_url
        yield item

    def parse(self, response, **kwargs):
        item = BiziwallproItem()
        li_list = response.xpath('//*[@id="thumbs"]/section/ul/li/figure/a[1]/@href').extract()
        for li in li_list:
            yield scrapy.Request(li, callback=self.parse_url, meta={'item': item})

        print('-------', self.page_num, "爬取成功！！！！")
        if self.page_num <= 3:
            self.page_num += 1
            new_url = self.url.format(self.page_num)
            yield scrapy.Request(new_url, callback=self.parse)

