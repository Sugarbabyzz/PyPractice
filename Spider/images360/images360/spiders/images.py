# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from scrapy import Spider, Request

import scrapy


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {'ch': 'photography', 'listtype': 'new', 'temp': 1}
        base_url = 'https://images.so.com/zj?'
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)


    def parse(self, response):
        pass
