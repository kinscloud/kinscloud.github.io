# -*- coding: utf-8 -*-
import scrapy
import re
from fang.items import NewHouseItem,EsfHouseItem
from scrapy_redis.spiders import RedisSpider


#class SfwSpider(scrapy.Spider):
class SfwSpider(RedisSpider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    #start_urls = ['https://www.fang.com/SoufunFamily.htm']
    #从redis数据库里找fang:start_urls的值作为起始url,如果没有，会一直等待
    redis_key="fang:start_urls"

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get()
            province_text = re.sub(r"\s", "", province_text)
            if province_text:
                province = province_text
            if province == "其它":
                continue
            
            city_td = tds[1]
            city_links = city_td.xpath(".//a")
            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                #print(province,city,city_url)
                url_module = city_url.split(".")
                newhouse_url = url_module[0] + ".newhouse." + url_module[1] + "." + url_module[2] + "/house/s/"
                esf_url = url_module[0] + ".esf." + url_module[1] + "." + url_module[2]
                yield scrapy.Request(url=newhouse_url,callback=self.parse_newhouse,meta={"info":(province,city)})
                yield scrapy.Request(url=esf_url,callback=self.parse_esf,meta={"info":(province,city)})
                break
            break
    
    def parse_newhouse(self,response):
        province,city = response.meta.get("info")
        lis = response.xpath("//div[contains(@class,'nl_con')]/ul/li")
        for li in lis:
            name = li.xpath(".//div[@class='nlcd_name']/a/text()").get()
            house_type_list = li.xpath(".//div[contains(@class,'house_type')]/a/text()").getall()
            house_type_list = list(map(lambda x:re.sub("\s","",x),house_type_list))
            rooms = list(filter(lambda x:x.endswith("居") or x.endswith("居以上"),house_type_list))
            area = "".join(li.xpath(".//div[contains(@class,'house_type')]/text()").getall())
            area = re.sub(r"\s|－|/","",area)
            district_text  = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
            district_list = re.search(r".*\[(.+)\].*",district_text)
            district = ""
            if district_list:
                district = district_list.group(1)
            address = li.xpath(".//div[@class='address']/a/@title").get()
            sale = li.xpath(".//div[contains(@class,'fangyuan')]/span/text()").get()
            price = "".join(li.xpath(".//div[contains(@class,'nhouse_price')]//text()").getall())
            price = re.sub("\s|广告","",price)
            origin_url = response.urljoin(li.xpath(".//div[@class='nlcd_name']/a/@href").get())

            if name :
                name = name.strip()
                item = NewHouseItem(name=name,rooms=rooms,area=area,
                                    district=district,address=address,sale=sale,
                                    price=price,origin_url=origin_url,province=province,
                                    city=city)
                yield item
            
        next_url = response.xpath("//div[@class='page']//a[text()='下一页']/@href").get()
        if next_url:
           yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_newhouse,meta={"info":(province,city)})
                
    
    def parse_esf(self,response):
        province,city = response.meta.get("info")
        dls = response.xpath("//div[contains(@class,'shop_list')]/dl")
        for dl in dls:
            name = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            if name:  
                item = EsfHouseItem(province=province,city=city,name=name)
                infos = dl.xpath(".//p[@class='tel_shop']//text()").getall()
                infos = list(map(lambda x:re.sub("\s","",x),infos))
                for info in infos:
                    if "厅" in info:
                        item['rooms']= info
                    elif '层' in info:
                        item['floor']= info
                    elif '向' in info:
                        item['toward']=info
                    elif '㎡' in info:
                        item['area'] = info
                    elif '年建' in info:
                        item['year']=info.replace('年建', '')
                    else:
                        pass
                item['address'] = dl.xpath(".//p[@class='add_shop']/span/text()").get()
                item['price'] = "".join(dl.xpath(".//dd[@class='price_right']/span[@class='red']//text()").getall())
                item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]/text()").get()
                item['origin_url'] = response.urljoin(dl.xpath(".//h4[@class='clearfix']/a/@href").get())
                yield item
        
        next_url = response.xpath("//div[@class='page_al']//a[text()='下一页']/@href").get()

        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse_esf,meta={"info":(province,city)})