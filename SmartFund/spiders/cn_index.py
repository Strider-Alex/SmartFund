import scrapy

class CNIndexSpider(scrapy.Spider):
    name = "CNIndex"

    def start_requests(self):
        urls = [
            'https://danjuanapp.com/djapi/index_eva/dj',
        ]
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        with open(self.filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % self.filename)