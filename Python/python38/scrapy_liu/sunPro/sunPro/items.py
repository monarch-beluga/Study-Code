# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunporItem(scrapy.Item):
    page_url = scrapy.Field()


class PageItem(scrapy.Item):
    title = scrapy.Field()

