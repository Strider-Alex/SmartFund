import json
import scrapy
from scrapy.crawler import CrawlerProcess
from SmartFund.spiders.funds_spider import FundsSpider

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

fn = "funds-index_eva.json"
process.crawl(FundsSpider, filename=fn)
process.start()  # the script will block here until the crawling is finished

selected_funds = ['中证红利','上证50','基本面50','恒生指数']
with open(fn) as f:
    res = json.load(f)
    items = res['data']['items']
    for item in items:
        if item['name'] in selected_funds:
            ep = 1/item['pe']
            if ep > 0.1:
                print(item['name']+': buy')
            elif ep > 0.064:
                print(item['name']+': hold')
            else:
                print(item['name']+': sell')
