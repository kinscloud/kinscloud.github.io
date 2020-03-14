# -*- coding: utf-8 -*-
import scrapy
from splashdemo.items import SplashdemoItem
from scrapy_splash import SplashRequest

    
lua_script = '''
    function main(splash,args)
        splash:go(args.url)
        splash:wait(args.wait)
        splash:runjs("document.getElementsByClassName('mod_turn_page clearfix mt20')[0].scrollIntoView(true)")
        splash:wait(args.wait)
        return splash:html()
    end
'''

class IphoneSpider(scrapy.Spider):
    name = 'iphone'
    #allowed_domains = ['yhd.com']
    url = ['https://search.yhd.com/c0-0/kiphone']
    start_urls = [
        'https://search.yhd.com/c0-0/kiphone'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse,      endpoint='execute',
                            args={'lua_source': lua_script, 'images': 0, 'wait': 3}, cache_args=['lua_source'])


    def parse(self, response):
        item = SplashdemoItem()
        list_selector = response.xpath('//div[@class="itemBox"]')
        for one_selector in list_selector:
            try:
                price = "".join(one_selector.xpath('.//em[@class="num"]//text()').getall())
                price = price.strip()
                title = "".join(one_selector.xpath('p[@class="proName clearfix"]/a/text()').getall())
                title = title.strip()
                positiveRatio = one_selector.xpath('.//span[@class="positiveRatio"]/text()').get()
                storeName = one_selector.xpath('.//span[@class="shop_text"]/text()').get()
                item['price'] = price
                item['title'] = title
                item['positiveRatio'] = positiveRatio
                item['storeName'] = storeName
                
                yield item
            except:
                continue
        
        next_url = response.xpath('//a[text()="下一页"]/@href').get()
        if next_url:
            next_url = response.urljoin(next_url)
            yield SplashRequest(next_url, callback=self.parse,      endpoint='execute',
                            args={'lua_source': lua_script, 'images': 0, 'wait': 3}, cache_args=['lua_source'])