# index_scraper
Scraper for hungarian news site

```
# create new virtualenv for the project
python3 -m venv venv

# activate it
source venv/bin/activate

# install libs
pip3 install requirements.txt

# run main page spider
scrapy crawl main -o index_headlines.jl
```
