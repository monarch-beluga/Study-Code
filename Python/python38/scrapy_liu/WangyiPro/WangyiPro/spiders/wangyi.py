import scrapy
from selenium import webdriver
from ..items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls = []

    def __init__(self):
        c_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        option = webdriver.ChromeOptions()
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.binary_location = c_path
        self.Manipulator = webdriver.Chrome(options=option)

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        for index in [3, 4, 6, 7, 8]:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)

        for url in self.model_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    def parse_model(self, response):
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item = WangyiproItem()
            item['title'] = title
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            yield scrapy.Request(url=new_detail_url, callback=self.parase_detail, meta={'item': item})

    def parase_detail(self, response):
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item

    def closed(self, spider):
        self.Manipulator.quit()


