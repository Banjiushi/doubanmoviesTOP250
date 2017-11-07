# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings

class DoubanPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        sheet_name = settings['MONGODB_SHEETNAME']

        # 创建 MongoDB 的数据库连接
        client = pymongo.MongoClient(host=host, port=port)

        # 指定数据库
        mydb = client[db_name]

        # 存放数据的数据库表名
        self.post = mydb[sheet_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)

        return item
