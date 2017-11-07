# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    base_url = 'https://movie.douban.com/top250?start='
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        item = DoubanItem()
        info = response.xpath("//div[@class='info']")
        for i in info:
            item['title'] = i.xpath(".//div[@class='hd']/a/span[@class='title'][1]/text()").extract_first()
            detail = i.xpath(".//div[@class='bd']/p[1]/text()").extract_first()
            item['detail'] = detail.strip().replace('\xa0', '')
            item['star'] = i.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract_first()
            item['quote'] = i.xpath(".//div[@class='bd']/p[@class='quote']/span/text()").extract_first()
            yield item

        if self.offset < 225:
            self.offset+=25
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)