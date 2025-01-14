# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

'''
class IndeedPipeline:
    def process_item(self, item, spider):
        return item
'''


from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter

class ValidateItemPipeline(object):

    def process_item(self, item, spider):
        ###relaxing this condition
        # if not all(item.values()):
        #     raise DropItem("Missing values!")
        # else:
        #     return item
        return item

class WriteItemPipeline(object):

    def __init__(self):
        self.filename = 'indeed.csv' #change the file name

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item