# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class DoubanItem(Item):
    collection = 'film'

    id = Field()
    title = Field()
    year = Field()
    region = Field()
    language = Field()
    director = Field()
    type = Field()
    actor = Field()
    date = Field()
    runtime = Field()
    rate = Field()
    rating_num = Field()





