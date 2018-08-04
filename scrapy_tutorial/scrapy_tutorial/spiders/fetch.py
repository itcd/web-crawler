# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
from unidecode import unidecode

class FetchSpider(scrapy.Spider):
    name = "fetch"
    count = 0

    def start_requests(self):
        urls = ["https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP2.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP3.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP4.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP5.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP6.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP7.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP8.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP9.htm", "https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16_IP10.htm"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = response.xpath('//*/div[3]/div/div[2]/div[2]/div/div/ul/li/span/text()').extract()
        for d in items:
            self.count += 1
            yield {self.count: unidecode(d)}