# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称
    title = scrapy.Field()
    # 信息
    detail = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 引述
    quote = scrapy.Field()
