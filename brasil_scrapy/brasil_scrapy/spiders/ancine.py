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

        title = response.xpath('//*[@id="node-23823"]/div[1]/h2/text()').extract_first()
        texto_sinopse = response.xpath('.//tr/td/b/text()').extract_first()
        sinopse = response.xpath('.//tr/td/b/text()').extract_first()
        texto_producao = response.xpath('.//td[contains(@class, "label")]/text()').extract_first()
        producao = response.xpath('//td[2]/div/div/div/text()').extract_first()

        yield {
            'title': title,
            'texto_sinopse': texto_sinopse,
            'sinopse': sinopse,
            'texto_producao': texto_producao,
            'producao': producao,
        }





