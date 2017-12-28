# coding=utf-8
import scrapy


class SpiderCourse(scrapy.Spider):

    name = 'scrapy_shiyanlou'

    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url.format(x) for x in range(1, 5))
        return urls


    def parse(self, response):
        for resp in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            yield {
                'name': resp.xpath('.//div/h3/a/text()').re_first('[^\s*|\\*]+'),
                'date_time': resp.xpath('.//div/relative-time/@datetime').extract_first()
            }


