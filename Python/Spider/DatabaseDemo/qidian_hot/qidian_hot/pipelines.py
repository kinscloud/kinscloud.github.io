# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo, redis


class QidianHotPipeline(object):
    def __init__(self):
        self.author_set = set()

    def process_item(self, item, spider):
        author = item['author']
        if author in self.author_set:
            raise DropItem("dupli author%s" % item)
        else:
            self.author_set.add(author)
        return item


class SaveToTxtPipeline(object):
    file = None

    @classmethod
    def from_crawler(cls, crawler):
        cls.file_name = crawler.settings.get('FILE_NAME', 'hot2.txt')
        return cls()

    def open_spider(self, spider):
        self.file = open(self.file_name, 'a', encoding='utf-8')

    def process_item(self, item, spider):
        novel_str = item['name'] + ";" + \
                    item['author'] + ";" + \
                    item['intro'] + '\n'
        self.file.write(novel_str)
        return item

    def close_spider(self, spider):
        self.file.close()


class MySQLPipeline(object):

    def open_spider(self, spider):
        db_name = spider.settings.get('MYSQL_DB_NAME')
        host = spider.settings.get('MYSQL_HOST')
        user = spider.settings.get('MYSQL_USER')
        pwd = spider.settings.get('MYSQL_PASSWORD')

        self.db_conn = pymysql.connect(db=db_name, host=host,
                                       user=user, password=pwd, charset='utf8')
        self.db_cursor = self.db_conn.cursor()

    def process_item(self, item, spider):
        values = (item['name'],
                  item['author'],
                  item['intro'])
        sql = 'insert into hot(name,author,intro) values (%s,%s,%s)'
        self.db_cursor.execute(sql, values)

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_cursor.close()
        self.db_conn.close()


class MongoDBPipeline(object):

    def open_spider(self, spider):
        host = spider.settings.get('MONGODB_HOST')
        port = spider.settings.get('MONGODB_PORT')
        db_name = spider.settings.get('MONGODB_NAME')
        user = spider.settings.get('MONGODB_USER')
        pwd = spider.settings.get('MONGODB_PASSWORD')
        collection_name = spider.settings.get('MONGODB_COLLECTION')
        self.db_client = pymongo.MongoClient(host=host, port=port)
        self.db_client.admin.authenticate(user, pwd)
        self.db = self.db_client[db_name]
        self.db_collection = self.db[collection_name]

    def process_item(self, item, spider):
        item_dict = dict(item)
        self.db_collection.insert_one(item_dict)
        return item

    def close_spider(self, spider):
        self.db_client.close()


class RedisPipeline(object):

    def open_spider(self, spider):
        host = spider.settings.get('REDIS_HOST')
        port = spider.settings.get('REDIS_PORT')
        db_index = spider.settings.get('REDIS_DB_INDEX')
        self.db_conn = redis.StrictRedis(host=host, port=port, db=db_index)

    def process_item(self, item, spider):
        item_dict = dict(item)
        self.db_conn.rpush('novel', str(item_dict))
        return item

    def close_spider(self, spider):
        self.db_conn.connection_pool.disconnect()
