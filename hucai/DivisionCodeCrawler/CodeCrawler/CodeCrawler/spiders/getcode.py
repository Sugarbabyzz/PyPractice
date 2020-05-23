# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from CodeCrawler.items import CodeItem


class GetcodeSpider(scrapy.Spider):
    name = 'getcode'
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ 解析各城市url """
        for tr in response.xpath('//tr[@class="provincetr"]'):

            for td in tr.xpath('td'):

                name = td.xpath('a/text()').extract_first()

                if name is not None:
                    url = parse.urljoin(response.url, td.xpath('a/@href').extract_first())
                    print(name, url)
                    yield scrapy.Request(url=url, callback=self.recursion_parse, meta={'name': name})

    def recursion_parse(self, response):
        """ 递归 """
        for tr in response.xpath('//tr[@class="citytr" or @class="countytr" or @class="towntr" or @class="villagetr"]'):

            if 'villagetr' in tr.xpath('@class').extract_first():
                code = tr.xpath('td[1]/text()').extract_first()
                name = tr.xpath('td[3]/text()').extract_first()
            else:
                code = tr.xpath('td[1]/a/text()').extract_first()
                name = tr.xpath('td[2]/a/text()').extract_first()

            if name == '市辖区':
                name = response.meta['name']

            print(code, name)

            # 存结果
            if name is not None and code is not None:
                item = CodeItem()
                item['name'] = name
                item['code'] = code
                yield item

            # 递归
            url = parse.urljoin(response.url, tr.xpath('td[1]/a/@href').extract_first())
            yield scrapy.Request(url=url, callback=self.recursion_parse, meta={'name': name})
