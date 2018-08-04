SET URL1="https://www.glassdoor.com/Interview/Google-Australia-Interview-Questions-EI_IE9079.0,6_IL.7,16_IN16.htm"
SET URL2="https://www.glassdoor.com/Interview/Amazon-Australia-Interview-Questions-EI_IE6036.0,6_IL.7,16_IN16.htm"
SET URL3="https://www.glassdoor.com/Interview/Facebook-Australia-Interview-Questions-EI_IE40772.0,8_IL.9,18_IN16.htm"
SET URL4="https://www.glassdoor.com/Interview/Accenture-Australia-Interview-Questions-EI_IE4138.0,9_IL.10,19_IN16.htm"

del /f temp.json
scrapy crawl order -a url=%URL1% -o temp.json
copy /y temp.json Google.json

del /f temp.json
scrapy crawl order -a url=%URL2% -o temp.json
copy /y temp.json Amazon.json

del /f temp.json
scrapy crawl order -a url=%URL3% -o temp.json
copy /y temp.json Facebook.json

del /f temp.json
scrapy crawl order -a url=%URL4% -o temp.json
copy /y temp.json Accenture.json

del /f temp.json
