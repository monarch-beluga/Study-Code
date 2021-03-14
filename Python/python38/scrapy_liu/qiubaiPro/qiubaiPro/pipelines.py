# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class QiubaiproPipeline(object):
    fp = None

    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('E:/temp/爬虫/scrapy/qiubai.txt', 'w', encoding='utf-8')

    # 专门来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + '\n' + content + '\n')
        return item

    def close_spider(self, spider):
        print('结束爬虫.......')
        self.fp.close()


class mysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                                    password='160925LQsxyz', db='start')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("insert into qiubai values('%s', '%s')" % (item['author'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
