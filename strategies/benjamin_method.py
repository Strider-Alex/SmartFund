import json
import scrapy
from scrapy.crawler import CrawlerProcess
from strategies.strategy import Strategy
from utils.constants import Region
from SmartFund.spiders.cn_index import CNIndexSpider



class BenjaminMethod(Strategy):
    '''
    Class implementation for Benjamin Method to select index funds. Details about this
    method: https://zhuanlan.zhihu.com/p/71644345
    '''
    def __init__(self, data_path, region=Region.cn):
        super().__init__(data_path)
        self.region = region
        self.selected_funds = []

    def select_funds(self):
        if self.region == Region.cn:
            self.selected_funds = ['中证红利','上证50','基本面50','恒生指数']
        else:
            self.selected_funds = []

    def collect_data(self):
        process = CrawlerProcess()
        process.crawl(CNIndexSpider, filename=self.data_path)
        process.start()  # the script will block here until the crawling is finished
    
    def suggest(self):
        self.select_funds()
        with open(self.data_path) as f:
            res = json.load(f)
            items = res['data']['items']
            for item in items:
                if item['name'] in self.selected_funds:
                    ep = 1/item['pe']
                    if ep > 0.1:
                        print(item['name']+': buy')
                    elif ep > 0.064:
                        print(item['name']+': hold')
                    else:
                        print(item['name']+': sell')