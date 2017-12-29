# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanlouItem

class CoursSpider(scrapy.Spider):
    name = 'cours'
    allowed_domains = ['www.github.com']
    start_urls = ['http://www.github.com/']

    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = [url.format(x) for x in range(1, 5)]
        return urls

    def parse(self, response):
        for resp in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            item = ShiyanlouItem({
                'name': resp.xpath('.//div/h3/a/text()').re_first('[^\s*|\\*]+'),
                'update_time': resp.xpath('.//div/relative-time/@datetime').extract_first()
            })
            yield item
