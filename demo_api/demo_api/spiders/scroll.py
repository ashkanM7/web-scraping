# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
import json


class ScrollSpider(scrapy.Spider):
    name = 'scroll'
    INCREMENTED_BY = 30
    offset = 30
    allowed_domains = ['ashkanm7.github.io']
    start_urls = [f'https://api.unsplash.com/photos/random/?client_id=H4AlmDbQswo8NGgdbzE31D7ChdEEjUIHy19OXusl8xY&count={offset}']

    def parse(self, response):
        if self.offset >= 2000:
            raise CloseSpider('Scraped 2000 titles...')

        resp = json.loads(response.body)
        
        for e in resp:
        
            yield{
                'id': e.get('id'),
                'description':e.get('description'),
                'alt_description': e.get('alt_description'),
                
            }

        self.offset += self.INCREMENTED_BY    
        yield scrapy.Request(url=f"https://api.unsplash.com/photos/random/?client_id=H4AlmDbQswo8NGgdbzE31D7ChdEEjUIHy19OXusl8xY&count={self.offset}",
        callback = self.parse)


