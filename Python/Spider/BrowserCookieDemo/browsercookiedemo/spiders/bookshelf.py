# -*- coding: utf-8 -*-
import scrapy
from browsercookiedemo.items import BookItem
import browsercookie


class BookshelfSpider(scrapy.Spider):
    name = 'bookshelf'
    # allowed_domains = ['qidian.com']
    # start_urls = ['http://qidian.com/']

    def __init__(self, name=None, **kwargs):
        cookiejar = browsercookie.chrome()
        self.cookie_dict = {}
        for cookie in cookiejar:
            if cookie.domain == '.qidian.com':
                if cookie.name in ['_csrfToken',
                                   'e1',
                                   'e2',
                                   'newstatisticUUID',
                                   'ywguid',
                                   'ywkey']:
                    self.cookie_dict[cookie.name]= cookie.value
                    
    def start_requests(self):
        url='https://my.qidian.com/bookcase'
        yield scrapy.Request(url,cookies=self.cookie_dict)
        
    def parse(self, response):
        item = BookItem()
        print(response)
