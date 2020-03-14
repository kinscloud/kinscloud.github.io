# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import requests,json,random



class UseragentandipDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    PROXY_LIST = []
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    
    def __init__(self, name=None, **kwargs):
        url = 'http://api.newday.me/proxy/extract'
        params={"token":"970eba4e11d70f47","format":"json"}
        #通过format为json接收代理
        response = requests.get(url, params=params)
        response_json = json.loads(response.text)
        ip_list = response_json["data"]["list"]
        
        for ip in ip_list:
            self.PROXY_LIST.append("%s:%d"%(ip['ip'],ip['port']))

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random
        print(request.headers['User-Agent'])   
        
        proxy = random.choice(self.PROXY_LIST)
        # while not self.validateIp(proxy):
        #     proxy = random.choice(self.PROXY_LIST)
        if request.url.startswith("http://"):
            request.meta['proxy'] = "http://" + proxy         # http代理
        elif request.url.startswith("https://"):
            request.meta['proxy'] = "https://" + proxy         # https代理
        
        
        return None    
        

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
