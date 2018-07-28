# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestatescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    dimensions = scrapy.Field()
    pricePerSqF = scrapy.Field()
    homeType = scrapy.Field()
    yearBuilt = scrapy.Field()
    address = scrapy.Field()
    realtor = scrapy.Field()
    realtorGroup = scrapy.Field()
    description = scrapy.Field()
    pass
