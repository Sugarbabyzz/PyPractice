# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapyuniversal.items import NewsItem
from scrapyuniversal.loader import ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles']

    # 定义的Rule已经实现页面的打开详情页和翻页
    rules = (
        Rule(LinkExtractor(allow='article\/.*.\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
                        callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )

    # 通常写法：
    # def parse_item(self, response):
    #     item = NewsItem()
    #     item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
    #     item['url'] = response.url
    #     item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
    #     item['datatime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
    #     item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
    #     item['website'] = '中华网'
    #     yield item

    # 以上写法不规整，下面采用ItemLoader实现配置化提取
    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()
