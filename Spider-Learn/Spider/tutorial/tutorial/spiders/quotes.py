# -*- coding: utf-8 -*-
import scrapy
# 这里导入对应的Item，Item相当于一个字典
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()  # 此时获得的是一个长度为1的列表，需要用extract_first来获取第一个元素
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()  # 要获取所有标签，直接用extract即可
            yield item

        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)  # urljoin将相对url构成一个绝对url
        yield scrapy.Request(url=url, callback=self.parse)
