import scrapy


class IndexMainSpider(scrapy.Spider):
    name = "main"

    def start_requests(self):
        urls = [
            'http://index.hu/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for res in response.xpath('//div[@class="cim"]//a/text()').extract():
            yield {
                'headline': res
            }