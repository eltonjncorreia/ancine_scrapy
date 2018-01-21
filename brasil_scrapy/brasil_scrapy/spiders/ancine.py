# -*- coding: utf-8 -*-
import scrapy


class AncineSpider(scrapy.Spider):
    name = 'ancine'

    url = 'https://www.ancine.gov.br/pt-br/brasil-nas-telas'

    allowed_domains = ['ancine.gov.br']
    start_urls = [url]

    def parse(self, response):
        items = response.xpath('//*[@id="conteudo"]/div/div/table/tbody/tr')

        for item in items:
            urls = item.xpath('.//td/h3/a/@href').extract_first()


            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.detail)

        if urls:
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.parse)


    def detail(self, response):
        self.log("estou na funcao "+response.url)


