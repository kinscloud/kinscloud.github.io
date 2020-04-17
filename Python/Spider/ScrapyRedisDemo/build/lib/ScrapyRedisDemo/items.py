'''
@Author: your name
@Date: 2020-03-13 14:58:28
@LastEditTime: 2020-03-13 15:00:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \ScrapyRedisDemo\ScrapyRedisDemo\items.py
'''
import scrapy


class LianjiaHomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    fitment = scrapy.Field()
    floor = scrapy.Field()
    year = scrapy.Field()
    category = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    property = scrapy.Field()