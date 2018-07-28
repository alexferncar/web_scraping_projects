# -*- coding: utf-8 -*-
import scrapy
from realEstateScrape.items import RealestatescrapeItem
from time import sleep
import random

class RealestatespiderSpider(scrapy.Spider):
    name = 'realestateSpider'
    allowed_domains = ['realtor.com']
    #start_urls = ['http://realtor.com/']
    start_urls = ['https://www.realtor.com/realestateandhomes-search/78617']

    def parse(self, response):
        links = response.xpath("//ul[@class='srp-list-marginless list-unstyled prop-list']/li/@data-url").extract()
        #old selector, doesnt work anymore
        #links = response.xpath("//ul[@class='srp-list-marginless list-unstyled ']/li/@data-url").extract()
        for link in links:
            url = response.urljoin(link)
            sleep(random.randrange(1,2))
            yield scrapy.Request(url,callback=self.parse_dir_content)
        next_page_url = response.xpath("//span[@class='next ']/a/@href").extract_first()
        absolute_next_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_url)


    def parse_dir_content(self,response):
        item = RealestatescrapeItem()
        item['price'] = response.xpath("//div[@class='display-inline']/span/@content")[0].extract()
        item['url'] = response.request.url
        item['dimensions'] = response.xpath("//div[@class='row']/div/div/div/meta/@content")[4].extract() # not dimensions
        item['pricePerSqF'] = response.xpath("//li[@class='ldp-key-fact-item']/div[2]/text()")[1].extract()

        try:
            item['homeType'] = response.xpath("//li[@class='ldp-key-fact-item']/div[2]/text()")[3].extract()
        except IndexError:
            item['homeType'] = ''
        try:
            item['yearBuilt'] = response.xpath("//li[@class='ldp-key-fact-item']/div[2]/text()")[4].extract()
        except IndexError:
            item['yearBuilt'] = ''

        string = response.request.url
        splitURL = string.split('detail/')
        roughADDRESS = ' '.join(splitURL[1].split('_')[:-1:])
        finalADDRESS = ' '.join(roughADDRESS.split('-'))
        item['address'] = finalADDRESS

        try:
            item['realtor'] = response.xpath("//section[@id='ldp-branding']/p/span[3]/span/text()")[0].extract()
        except IndexError:
            item['realtor'] = ''
        try:
            item['realtorGroup'] = response.xpath("//section[@id='ldp-branding']/p/span[4]/text()")[0].extract()
        except IndexError:
            item['realtorGroup'] = ''

        try:
            item['description'] = response.xpath("//p[@id='ldp-detail-romance']/text()")[0].extract()
        except IndexError:
            item['description'] = ''

        yield item
