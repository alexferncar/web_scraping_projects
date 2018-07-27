# -*- coding: utf-8 -*-
import scrapy
from cryptoScrape.items import CryptoscrapeItem
from time import sleep
import random

class CryptospiderSpider(scrapy.Spider):
    name = 'cryptospider'
    #allowed_domains = ['coinmarketcap.com/']
    start_urls = ['https://coinmarketcap.com/']

    def parse(self, response):
        links = response.xpath("//td[@class='no-wrap currency-name']/a/@href").extract()
        #new_links = links[:100]
        for link in links:
            url = response.urljoin(link)
            sleep(random.randrange(1,2))
            yield scrapy.Request(url,callback=self.parse_dir_content)
        for i in range(2,4):
            next_page_url = 'https://coinmarketcap.com/'+str(i)+''
            absolute_url = response.urljoin(next_page_url)
            sleep(random.randrange(1,2))
            yield scrapy.Request(absolute_url)

    def parse_dir_content(self, response):
        item = CryptoscrapeItem()
        item['name'] = response.xpath("//h1[@class='details-panel-item--name']/img/@alt")[0].extract()
        item['ticker'] = response.xpath("//h1[@class='details-panel-item--name']/span/text()")[0].extract()
        item['price'] = response.xpath("//div[@class='details-panel-item--price bottom-margin-1x']/span/span/text()")[0].extract()
        item['marketCap'] = response.xpath("//div[@class='coin-summary-item-detail']/span/span/text()")[0].extract()
        item['circulatingSupply'] = response.xpath("//div[@class='coin-summary-item-detail details-text-medium']/span/text()")[0].extract()
        try:
            item['maxSupply'] = response.xpath("//div[@class='coin-summary-item-detail details-text-medium']/span/text()")[1].extract()
        except IndexError:
            item['maxSupply'] = ''
        item['website'] = response.xpath("//ul[@class='list-unstyled details-panel-item--links']/li[2]/a/@href")[0].extract()
        yield item
