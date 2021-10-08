import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/text()').extract_first()
            job_url = 'https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href').extract_first()
            print(job_name)
            # yield scrapy.Request(job_url, callback=self)


