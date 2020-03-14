# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-f]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        #部分元素获取不到，是后期用AJAX加载的
        avatar = response.xpath("//img[@class='_13D2Eh']/@src").get()
        author = response.xpath("//span[@class='_22gUMi']/text()").get()
        pub_time  = response.xpath("//div[@class='s-dsoj']/time/text()").get()
        url = response.url.split("?")[0]
        article_id = url.split("/")[-1]
        content = response.xpath("//article[@class='_2rhmJa']").get()
        read_count = response.xpath("//div[@class='s-dsoj']/span[3]/text()").get().replace("阅读 ", "")
        like_count = response.xpath("//div[@class='s-dsoj']//span[1]/text()").get()
        word_count = response.xpath("//div[@class='s-dsoj']/span[2]/text()").get().replace("字数 ", "")
        subjects = ",".join(response.xpath("//div[@class='_2Nttfz']/a").getall())
        item = JianshuSpiderItem(title=title,
                                 avatar=avatar,
                                 author=author,
                                 pub_time=pub_time,
                                 origin_url=response.url,
                                 article_id=article_id,
                                 content=content,
                                 read_count=read_count,
                                 like_count=like_count,
                                 word_count=word_count,
                                 subjects=subjects
                                 )
        #print(item)
        yield item
