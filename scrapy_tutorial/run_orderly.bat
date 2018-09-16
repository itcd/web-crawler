@echo off
set URL1="https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm"
set URL2="https://www.glassdoor.com/Interview/Amazon-Australia-Interview-Questions-EI_IE6036.0,6_IL.7,16_IN16.htm"
set URL3="https://www.glassdoor.com/Interview/Facebook-Australia-Interview-Questions-EI_IE40772.0,8_IL.9,18_IN16.htm"
set URL4="https://www.glassdoor.com/Interview/Microsoft-Australia-Interview-Questions-EI_IE1651.0,9_IL.10,19_IN16.htm"
del /f ~temp.json
@echo on

scrapy crawl count_and_fetch -a url=%URL1% -o ~temp.json
copy /y ~temp.json GOOG.json
del /f ~temp.json

scrapy crawl count_and_fetch -a url=%URL2% -o ~temp.json
copy /y ~temp.json AMZN.json
del /f ~temp.json

scrapy crawl count_and_fetch -a url=%URL3% -o ~temp.json
copy /y ~temp.json FB.json
del /f ~temp.json

scrapy crawl count_and_fetch -a url=%URL4% -o ~temp.json
copy /y ~temp.json MSFT.json
del /f ~temp.json
