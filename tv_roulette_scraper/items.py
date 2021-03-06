# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Episodes(Item):
    name = Field()
    page = Field()
    season = Field()
    episode = Field()
    title = Field()
    url = Field()
    link = Field()
    response = Field()

class Video(Item):
    url = Field()
    page = Field()
    name = Field()