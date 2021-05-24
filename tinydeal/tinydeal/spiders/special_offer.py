# -*- coding: utf-8 -*-
import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = 'special_offer'
    allowed_domains = ['web.archive.org']
    # since we created the following start_request method start_urls is no more needed
    # start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    # the headers argument needs to be copied in the
    def start_requests(self):
        yield scrapy.Request(url= 'https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html', callback = self.parse, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        })

    def parse(self, response):
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):
            yield{
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price':product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price':product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
                'User-Agent': response.request.headers['User-Agent']
            }

        next_page = response.xpath("//a[@class='nextPage']/@href").get() 
        if(next_page):
            yield scrapy.Request(url=next_page, callback = self.parse, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        })   
