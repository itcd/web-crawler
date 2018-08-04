# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:44:47 2018
https://doc.scrapy.org/en/latest/intro/tutorial.html
@author: hasee
"""

import scrapy
import json
import fileinput

class CountSpider(scrapy.Spider):
    name = "count"
    count = 0
    url = 'https://www.glassdoor.ie/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm'
#    url = 'https://www.glassdoor.ie/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16.htm'

    def start_requests(self):
        urls = [
            self.url
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Get number of reviews and then calculate number of pages.
        text = response.xpath('//*[@id="MainCol"]/div[3]/div[1]/div[1]/h2/text()').extract_first()
        self.log(text)
        text_list = text.split()
        if(len(text_list) > 0):
            c = int(int(text_list[0]) / 10)
            url_list = [self.url.replace('.htm', '_IP{0}.htm'.format(i)) for i in range(2, c+2)]
            url_list.insert(0, self.url)
            json_str = json.dumps(url_list)
            self.log(json_str)
            
            # Replace the line of urls in the spider file. Note the list of urls must be written in one line.
            pattern = 'urls = ['
            spider_file = "scrapy_tutorial/spiders/fetch.py"
            self.log(spider_file)
            self.log(pattern)
            for line in fileinput.FileInput(spider_file, inplace=1):
                if pattern in line:
                    idx = line.find('[')
                    print(line[0:idx] + json_str)
                else:
                    print(line.rstrip('\r\n'))
            yield {text: json_str}

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
