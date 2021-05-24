# -*- coding: utf-8 -*-
import scrapy
import json

class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['ashkanm7.github.io']
    start_urls = ['https://type.fit/api/quotes/?method=getQuote&format=json']

    def parse(self, response):
        resp = json.loads(response.body)
        
        
        for elem in resp:
            yield{
                'text': elem.get('text'),
                'author': elem.get('author')
            }
