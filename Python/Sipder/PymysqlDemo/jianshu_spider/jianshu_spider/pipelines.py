# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors


class JianshuSpiderPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '192.168.1.101',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        print(self.conn)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item["title"], item["content"], item["author"],
                                       item["avatar"], item["pub_time"], item["origin_url"], item["article_id"]))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            INSERT INTO article(id,title,content,author,avatar,pub_time,origin_url,article_id)
             VALUES(null, %s, %s, %s, %s, %s, %s, %s)
            """
        return self._sql


class JianshuTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '192.168.1.101',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None
        
    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            INSERT INTO article(id,title,content,author,avatar,pub_time,origin_url,article_id,read_count,like_count,word_count,subjects)
             VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)
    
    def insert_item(self,cursor,item):
        cursor.execute(self.sql, (item["title"], item["content"], item["author"],
                                       item["avatar"], item["pub_time"], item["origin_url"], 
                                       item["article_id"],item["read_count"], item["like_count"],
                                       item["word_count"], item["subjects"]
                                       ))
        #self.conn.commit()
    
    def handle_error(self,error,item,spider):
        print('='*10+"error"+'='*10)
        print(error)
        print('='*10+"error"+'='*10)