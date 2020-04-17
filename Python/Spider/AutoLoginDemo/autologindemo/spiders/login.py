# -*- coding: utf-8 -*-
import scrapy
from autologindemo.items import DoubanLoginItem
import json,re


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/j/mobile/login/basic']

    def start_requests(self):
        data = {
            'ck': '',
            'name': '18576400070',
            'password': 'xx123456',
            'remember': 'True',
            'ticket': ''
        }

        for url in self.start_urls:
            yield scrapy.FormRequest(url, formdata=data, method='POST')

    def parse(self, response):
        result = json.loads(response.text)
        if result['status'] == 'success':
            url = 'https://www.douban.com/doulist/124283433/'
            yield scrapy.Request(url,callback=self.parse_doulist)
        else:
            self.logger.info('用户名或密码错误。')
            
    def parse_doulist(self,response):
        doulist = response.xpath('//div[@class="doulist-item"]')
        item = DoubanLoginItem()
        for one in doulist:
            try:
                title = one.xpath('.//div[@class="title"]/a/text()').get().strip()
                detail  = one.xpath('.//div[@class="abstract"]//text()').getall()
                author = re.findall('作者:(.*?)\n',detail[0])[0]
                publishing_house = re.findall('出版社:(.*?)\n',detail[1])[0]
                publish_time = re.findall('出版年:(.*?)\n',detail[2])[0]
                item['title'] = title
                item['author'] = author
                item['publishing_house'] = publishing_house
                item['publish_time'] = publish_time
                print(item)
            except:
                pass
