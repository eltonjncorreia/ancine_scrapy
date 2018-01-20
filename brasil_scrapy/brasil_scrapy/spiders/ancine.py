# -*- coding: utf-8 -*-
import scrapy


class AncineSpider(scrapy.Spider):
    name = 'ancine'

    allowed_domains = ['ancine.gov.br/brasil-nas-telas']
    start_urls = ['https://www.ancine.gov.br/brasil-nas-telas/']

    def parse(self, response):
        items = response.xpath('//table[contains(@class, "views-table")]/tbody/tr')

        for item in items:
            urls = item.xpath('.//td/h3/a').extract_first()

            yield {
                'urls': urls
            }






