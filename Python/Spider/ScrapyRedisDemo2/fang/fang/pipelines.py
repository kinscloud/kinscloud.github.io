# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
from fang.items import NewHouseItem,EsfHouseItem

class FangPipeline(object):
    def __init__(self):
        self.newhouse_fp = open('newhouse.json','wb')
        self.esf_fp = open('esf.json','wb')
        self.newhouse_exporter = JsonItemExporter(self.newhouse_fp,ensure_ascii=False)
        self.esf_exporter = JsonItemExporter(self.esf_fp,ensure_ascii=False)
        
    def process_item(self, item, spider):
        if isinstance(item, NewHouseItem):
            self.newhouse_exporter.export_item(item)
        if isinstance(item, EsfHouseItem):
            self.esf_exporter.export_item(item)
        return item
    
    def close_spider(self, spider):
        self.newhouse_fp.close()
        self.esf_fp.close()
        