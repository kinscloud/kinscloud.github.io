# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
import json


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    currentPage = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/new_search_subjects?tags=%E7%94%B5%E5%BD%B1&countries=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86&start=0'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        json_text = response.text
        movie_dict = json.loads(json_text)

        if len(movie_dict['data']) == 0:
            return

        for one_movie in movie_dict['data']:
            item['title'] = one_movie['title']
            item['directors'] = one_movie['directors']
            item['casts'] = one_movie['casts']
            item['rate'] = one_movie['rate']
            print(item)
            yield item
        url_next = 'https://movie.douban.com/j/new_search_subjects?tags=%E7%94%B5%E5%BD%B1&countries=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86&start=' + str(
            self.currentPage * 20)
        self.currentPage += 1
        yield scrapy.Request(url_next, headers=self.headers)
