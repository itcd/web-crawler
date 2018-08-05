# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
from unidecode import unidecode
from collections import deque

class OrderSpider(scrapy.Spider):
    name = "order"
    count = 0
    _url = 'https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm'
    url_list = deque()
    
    def __init__(self, url=None, *args, **kwargs):
        super(OrderSpider, self).__init__(*args, **kwargs)
        self.log(url)
        if url is not None:
        	self._url = url

    def start_requests(self):
        yield scrapy.Request(url=self._url, callback=self.parse_number)

    def parse_number(self, response):
        self.url_list.append(self._url)
        # Get item number from texts e.g. '94 Candidate Interview Reviews' and generate URLs for other pages
        text = response.xpath('//*[@id="MainCol"]/div[3]/div[1]/div[1]/h2/text()').extract_first()
        self.log(text)
        text_list = text.split()
        if text_list and text_list[0].isdigit():
            # Calculate number of pages
            c = int(int(text_list[0]) / 10)
            url_list = [self._url.replace('.htm', '_IP{0}.htm'.format(i)) for i in range(2, c+2)]
            for u in url_list:
                self.url_list.append(u)

        if self.url_list:
            u = self.url_list.popleft()
            yield scrapy.Request(url=u, callback=self.parse_item, dont_filter=True)
        
        yield {'count': text}

    def parse_item(self, response):
        # Request the next page if available
        if self.url_list:
            u = self.url_list.popleft()
            yield scrapy.Request(url=u, callback=self.parse_item, dont_filter=True)

        # Parse questions and convert to ASCII characters
        items = response.xpath('//*/div[3]/div/div[2]/div[2]/div/div/ul/li/span/text()').extract()
        for d in items:
            self.count += 1
            data = {'q': unidecode(d), 'id': self.count, 'page': response.url.split(',')[-1].split('.')[0]}
            yield data

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
