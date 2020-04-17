'''
@Author: your name
@Date: 2020-03-13 14:58:28
@LastEditTime: 2020-03-13 15:01:27
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: \ScrapyRedisDemo\ScrapyRedisDemo\pipelines.py
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re


class ProcessPipeline(object):
    def process_item(self, item, spider):
        # item['unit_price'] = item['unit_price'].replace('单价', '')
        item['unit_price'] = re.sub(r'单价', '', item['unit_price'])
        if not item['type'].endswith('厅'):
            raise DropItem("error item%s" % item)
        else:
            return item


class LianjiaHomePipeline(object):
    file = None

    def open_spider(self, spider):
        self.file = open('home.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        home_str = item['name'] + ',' + \
                   item['type'] + ',' + \
                   item['area'] + ',' + \
                   item['direction'] + ',' + \
                   item['fitment'] + ',' + \
                   item['floor'] + ',' + \
                   item['year'] + ',' + \
                   item['category'] + ',' + \
                   item['total_price'] + ',' + \
                   item['unit_price'] + ',' + \
                   item['property'] + '\n'
        self.file.write(home_str)
        return item

    def close_spider(self):
        self.file.close()
