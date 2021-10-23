# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import csv
import re


class CountriesPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = ['nombre', 'continente', 'area', 'poblacion', 'gdp', 
        'desempleo', 'impuestos', 'deuda', 'tasa_de_cambio','usuarios_internet',
        'porcentaje_internet', 'aeropuertos', 'carreteras_km', 'inversion_militar', 'image_name', 'image_urls']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CountriesImagenesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name': item['image_name']})
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None, *, item=None):
        # Replace '/' symbol, delete 'Imagen m de n de ' text
        # at the beginning of the image name, and restrict its length 
        image_name = item.get('image_name').replace('/', '-')
        image_name = image_name[:100]

        return f'{image_name}'

