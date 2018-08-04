# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
import json
import fileinput
from unidecode import unidecode

class AutoSpider(scrapy.Spider):
    name = "auto"
    _count = 0
    _url = 'https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm'
#    _url = 'https://www.glassdoor.ie/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16.htm'
    _url_list = []
    
    def __init__(self, url=None, *args, **kwargs):
        super(AutoSpider, self).__init__(*args, **kwargs)
        self.log(url)
        if url is not None:
        	self._url = url

    def start_requests(self):
    	yield scrapy.Request(url=self._url, callback=self.parse_number)

    def parse_number(self, response):
        self._url_list = [response.url]
        # Get item number from e.g. '94 Candidate Interview Reviews' and generate URLs for other pages
        text = response.xpath('//*[@id="MainCol"]/div[3]/div[1]/div[1]/h2/text()').extract_first()
        self.log(text)
        text_list = text.split()
        self.log(text_list)
        self.log(text_list[0].isdigit())
        if text_list and text_list[0].isdigit():
            # Calculate number of pages
            c = int(int(text_list[0]) / 10)
            url_list = [self._url.replace('.htm', '_IP{0}.htm'.format(i)) for i in range(2, c+2)]
            self._url_list.extend(url_list)
            self.log(self._url_list)
            for i in self._url_list:
                yield scrapy.Request(url=i, callback=self.parse_item)

    def parse_item(self, response):
        # Parse questions and convert to ASCII characters
        items = response.xpath('//*/div[3]/div/div[2]/div[2]/div/div/ul/li/span/text()').extract()
        for d in items:
            self._count += 1
            yield {response.url.split(',')[-1].split('.')[0]: unidecode(d)}

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
