#!/usr/bin/env python
from subprocess import check_call

def test_scrapy():
	check_call(r"""cd scrapy_tutorial
scrapy crawl order -a url="https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm" -o ~temp.json
""", shell=True)