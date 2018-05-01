# -*- coding: utf-8 -*-
import scrapy


class TycSpider(scrapy.Spider):
    name = 'tyc'
    allowed_domains = ['www.tianyancha.com']
    start_urls = ['http://www.tianyancha.com/']

    def parse(self, response):
        pass
