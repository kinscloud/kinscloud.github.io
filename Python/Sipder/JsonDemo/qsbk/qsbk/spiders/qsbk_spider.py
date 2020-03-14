# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['www.yicommunity.com']
    #start_urls = ['http://www.yicommunity.com/30date/index_2.html']
    start_urls = ['http://www.yicommunity.com/30date/index.html']
    url_head = "http://www.yicommunity.com"
    
    def parse(self, response):
        contents = response.xpath("//div[@class='content']")
        for content in contents:
            text = content.xpath("text()").get().strip()
            if text != "":
                item = QsbkItem(content=text)
                yield item
        
        print("page {} finished...".format(response.url))
        page_next = response.xpath("//div[@class='pagebar']/a[text()='下一页']/@href").get()
        if not page_next:
            return
        else:
            page_next_url = self.url_head + page_next
            yield scrapy.Request(page_next_url,callback=self.parse)
