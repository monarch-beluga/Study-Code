import scrapy
from ..items import Bizi4KproItem


class Bizi4kSpider(scrapy.Spider):
    name = 'bizi4K'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://pic.netbian.com/']

    url = 'http://pic.netbian.com/index_%d.html'
    page_num = 1

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            item = Bizi4KproItem()
            img_name = li.xpath('./a/b/text()').extract_first() + '.jpg'
            img_url = 'http://pic.netbian.com' + li.xpath('.//img/@src').extract_first()
            item['img_name'] = img_name
            item['img_url'] = img_url
            yield item
        print('--------', self.page_num, '爬取成功！！！')

        if self.page_num < 3:
            self.page_num += 1
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
