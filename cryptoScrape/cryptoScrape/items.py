# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CryptoscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    ticker = scrapy.Field()
    price = scrapy.Field()
    marketCap = scrapy.Field()
    circulatingSupply = scrapy.Field()
    maxSupply = scrapy.Field()
    website = scrapy.Field()
