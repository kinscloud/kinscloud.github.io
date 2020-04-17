import scrapy
from zhaopin.items import BoosZhiPinItem
import time
import json
from furl import furl

'''
用途：爬取BOSS直聘数据
参数：地区，职位信息
运行代码：scrapy crawl BoosZhiPin
'''


class BoosZhiPin(scrapy.Spider):
    name = 'BoosZhiPin'  # 运行时爬虫名称
    allowed_domains = ['www.zhipin.com']  # 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。
    start_urls = ['https://www.zhipin.com/wapi/zpCommon/data/city.json']  # 默认制定url，获取城市代码url
    city_name = ['乌鲁木齐', '喀什']  # 需要抓取的城市
    city_code_list = []  # 用于存储城市代码
    query = 'python'  # 需要查询的职位
    F = furl('https://www.zhipin.com/job_detail/?')  # URL母版

    # 发送 header，伪装为浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    def parse(self, response):
        self.get_city_code(response)  # 获取城市code
        for c in self.city_code_list:  # 根据生成的城市代码 生成请求
            yield self.request_city(c)

    # 获取城市code
    def get_city_code(self, response):
        city_code = json.loads(response.body_as_unicode())
        for city_name in self.city_name:
            for area in city_code['zpData']['cityList']:  # 循环地区
                for index, city in enumerate(area['subLevelModelList']):  # 循环该城市
                    if city['name'] == city_name:  # 查询需要抓取的城市的code
                        self.city_code_list.insert(index, str(city['code']))

    # 生成请求
    def request_city(self, city_code, page=0):
        '''构造 爬取某个具体的城市 的请求对象'''
        page += 1
        url_data = {
            'city': city_code,
            'query': self.query,
            'page': page
        }
        # 要爬取的页面的URL
        url = self.F.copy().add(url_data).url
        req = scrapy.Request(url, callback=self.get_data, dont_filter=False, headers=self.headers)
        # 使用 meta 传递附加数据，在 callback 中可以通过 response.meta 取得
        req.meta['city_code'] = city_code
        req.meta['page'] = page
        return req

    # 获取数据
    def get_data(self, response):
        job_list = response.css('div.job-list > ul > li')
        for job in job_list:
            item = BoosZhiPinItem()
            job_primary = job.css('div.job-primary')
            item['pid'] = job.css(
                'div.info-primary > h3 > a::attr(data-jobid)').extract_first().strip()
            item["positionName"] = job_primary.css(
                'div.info-primary > h3 > a::text').extract_first().strip()
            item["salary"] = job_primary.css(
                'div.info-primary > h3 > a > span::text').extract_first().strip()
            info_primary = job_primary.css(
                'div.info-primary > p::text').extract()
            item['city'] = info_primary[0].strip()
            item['workYear'] = info_primary[1].strip()
            item['education'] = info_primary[2].strip()
            item['companyShortName'] = job_primary.css(
                'div.info-company > div.company-text > h3 > a::text'
            ).extract_first().strip()
            company_infos = job_primary.css(
                'div.info-company > div.company-text > p::text').extract()
            if len(company_infos) == 3:  # 有一条招聘这里只有两项，所以加个判断
                item['industryField'] = company_infos[0].strip()
                item['financeStage'] = company_infos[1].strip()
                item['companySize'] = company_infos[2].strip()
            item['positionLables'] = job.css(
                'li > div.job-tags > span::text').extract()
            item['time'] = job.css('span.time::text').extract_first()
            item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            yield item

        city_name = response.meta['city_code']
        page = response.meta['page']
        if job_list:  # 判断是否有数据
            # 发送下一页请求
            time.sleep(5)  # ip多就可以注释掉了
            yield self.request_city(city_name, page=page + 1)
