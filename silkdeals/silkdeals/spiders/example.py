# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys

class ExampleSpider(scrapy.Spider):
    name = 'example'
   
    def start_request(self):
        yield SeleniumRequest(
            url = 'https://duckduckgo.com',
            wait_time = 2,
            screenshot = True,
            callback = self.parse

        )
            

    def parse(self, response):
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)
        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_from_input_homepage']")
        search_input.send_keys("Hello world")

        search_input.send_keys(Keys.ENTER)
        driver.save_screenshot('after_filling_input.png')