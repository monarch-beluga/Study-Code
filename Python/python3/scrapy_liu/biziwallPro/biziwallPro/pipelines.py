# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline

# class BiziwallproPipeline:
#     def process_item(self, item, spider):
#         print(item['img_name'], '\n', item['img_url'])
#         return item


class BiziwallPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        return request.url.split('/')[-1]

    def item_completed(self, results, item, info):
        return item


