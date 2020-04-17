# -*- coding: utf-8 -*-
import scrapy
from qidian_hot.items import QidianHotItem
from scrapy.loader import ItemLoader


class HotsalesSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/hotsales?style=1&page=1s']

    def parse(self, response):
        divs = response.xpath("//div[@class='book-mid-info']")
        for div in divs:
            novel = ItemLoader(item=QidianHotItem(), selector=div)
            novel.add_xpath('name', 'h4/a/text()')
            # name = div.xpath("h4/a/text()").get()
            # name = div.xpath("h4/a/text()").extract()[0]
            novel.add_xpath('author', 'p[@class="author"]/a/text()')
            # author = div.xpath("p[@class='author']/a/text()").get()
            novel.add_xpath('intro', 'p[@class="intro"]/text()')
            # intro = div.xpath("p[@class='intro']/text()").get().strip()
            # print(name, author, intro)
            # item = QidianHotItem()
            # item['name'] = name
            # item['author'] = author
            # item['intro'] = intro
            # item = {"name": name,
            #         "author": author,
            #         "intro": intro
            #         }
            item = novel.load_item()
            print(item)
            yield item
