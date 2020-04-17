'''
@Author: your name
@Date: 2020-03-13 15:00:04
@LastEditTime: 2020-03-13 15:12:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \ScrapyRedisDemo\ScrapyRedisDemo\spiders\home.py
'''
from scrapy import Request
from scrapy.spiders import Spider
from ScrapyRedisDemo.items import LianjiaHomeItem
from scrapy_redis.spiders import RedisSpider


class HomeSpider(RedisSpider):
    name = 'home'

    # allowed_domains = ['lianjia.com']
    # start_urls = ['https://sz.lianjia.com/ershoufang/']

    # def start_requests(self):
    #     url = 'https://sz.lianjia.com/ershoufang/'
    #     yield Request(url)

    def parse(self, response):
        list_selector = response.xpath('//li/div[@class="info clear"]')
        for one_selector in list_selector:
            try:
                name = one_selector.xpath('div[@class="title"]/a/text()').get()
                # 获取其他信息
                other = one_selector.xpath('.//div[@class ="houseInfo"]//text()').get()
                other = other.split('|')
                type = other[0].strip()
                area = other[1].strip()
                direction = other[2].strip()
                fitment = other[3].strip()
                floor = other[4].strip()
                year = other[5].strip()
                category = other[6].strip()
                total_price = "".join(one_selector.xpath('.//div[@class ="totalPrice"]//text()').getall())
                unit_price = one_selector.xpath('.//div[@class ="unitPrice"]//text()').get()
                item = LianjiaHomeItem()
                item["name"] = name
                item["type"] = type
                item["area"] = area
                item["direction"] = direction
                item["fitment"] = fitment
                item["floor"] = floor
                item["year"] = year
                item["category"] = category
                item["total_price"] = total_price
                item["unit_price"] = unit_price

                url = one_selector.xpath('div[@class="title"]/a/@href').get()
                url = response.urljoin(url)

                yield Request(url, meta={"item": item}, callback=self.property_parse)
            except:
                pass
            # yield item
        # url = response.xpath('//a[text()="下一页"]/@href').get()
        # url = response.urljoin(url)
        # print(url)
        for i in range(2, 11):
            next_url = response.urljoin('/ershoufang/pg%s' % i)
            yield Request(next_url)

    def property_parse(self, response):
        item = response.meta["item"]
        property_list = response.xpath('//div[@class="transaction"]//text()').getall()
        property_list = list(map(lambda x: x.strip(), property_list))
        property = " ".join(property_list)
        item["property"] = property
        yield item