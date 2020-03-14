# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {
            'email':'970138074@qq.com',
            'password':'pythonspider'
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request
    
    def parse_page(self,response):
        print(response.text)