'''
@Author: your name
@Date: 2020-03-12 09:23:57
@LastEditTime: 2020-03-12 09:43:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \FilesPipelineDemo\FilesPipelineDemo\spiders\file.py
'''
# -*- coding: utf-8 -*-
import scrapy
from FilesPipelineDemo.items import SeabornFileItem

class FileSpider(scrapy.Spider):
    name = 'file'
    allowed_domains = ['pydata.org']
    start_urls = ['http://seaborn.pydata.org/examples/index.html']

    def parse(self, response):
        urls = response.xpath('//div[@class="figure align-center"]/a/@href').getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url,callback=self.parse_file)

    def parse_file(self, response):
        href = response.xpath('//a[@class="reference download internal"]/@href').get()
        url = response.urljoin(href)
        item = SeabornFileItem()
        item['file_urls'] = [url]
        yield item