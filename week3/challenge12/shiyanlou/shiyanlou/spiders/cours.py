# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanlouItem

class CoursSpider(scrapy.Spider):
    name = 'cours'
    start_urls = ['https://github.com']

    def parse(self, response):
        sub_url = '/shiyanlou?page={}&tab=repositories'
        for x in range(1, 5):
            yield scrapy.Request(response.urljoin(sub_url.format(x)), callback=self.parse_repositories)

    def parse_repositories(self, response):
        for resp in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            item = ShiyanlouItem()
            item['name'] = resp.xpath('.//div/h3/a/text()').re_first('[^\s*|\\*]+'),
            item['update_time'] = resp.xpath('.//div/relative-time/@datetime').extract_first()

            sub_url = self.start_urls[0] + resp.xpath('.//div/h3/a/@href').extract_first()
            request = scrapy.Request(sub_url, callback=self.parse_info)
            request.meta['item'] = item
            yield request

    def parse_info(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//div[@class="stats-switcher-wrapper"]/ul/li/a[contains(@href, "commits")]/span/text()').re_first('[^\s*|\\*]+')
        item['branches'] = response.xpath('//div[@class="stats-switcher-wrapper"]/ul/li/a[contains(@href, "branches")]/span/text()').re_first('[^\s*|\\*]+')
        item['releases'] = response.xpath('//div[@class="stats-switcher-wrapper"]/ul/li/a[contains(@href, "releases")]/span/text()').re_first('[^\s*|\\*]+')

        yield item