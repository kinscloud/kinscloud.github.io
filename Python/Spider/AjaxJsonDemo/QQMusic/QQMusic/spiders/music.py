# -*- coding: utf-8 -*-
import scrapy
import json
from QQMusic.items import QqmusicItem
from scrapy import Request


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['qq.com']
    start_urls = ['http://qq.com/']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8532501558761572&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-03-08%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = QqmusicItem()
        json_text=response.text
        music_dict = json.loads(json_text)
        songs = music_dict['detail']['data']['data']['song']
        for one_music in songs:
            item['song_name'] = one_music['title']
            item['album_name'] = one_music['albumMid']
            item['singer_name'] = one_music['singerName']
            item['interval'] = one_music['rankValue']

            yield item

