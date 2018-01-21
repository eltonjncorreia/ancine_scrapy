# -*- coding: utf-8 -*-
import scrapy


class AncineSpider(scrapy.Spider):
    name = 'ancine'

    allowed_domains = ['ancine.gov.br']
    start_urls = ['https://www.ancine.gov.br/pt-br/brasil-nas-telas']

    def parse(self, response):
        items = response.xpath('//*[@id="conteudo"]/div/div/table/tbody/tr')

        for item in items:
            urls = item.xpath('.//td/h3/a/@href').extract_first()

            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.detail)

        next_page = response.xpath(
                    '//*[@id="conteudo"]/div//ul/li//a/@href'
        ).extract_first()

        if next_page:
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(next_page), callback=self.parse)

    def detail(self, response):
            yield {
                'title': response.css(
                    'div.content-header h2::text').extract_first(),

                'sinopse': response.css(
                    'div.field-item p::text').extract_first(),

                'image': response.xpath(
                    './/div//table//a/img/@src').extract_first()

            }
        # title = response.xpath('.//div[contains(@class, "content-header")]//h2/text()').extract_first()

        # sinopse = response.xpath(
        #     './/div[2]//td/div//p/text()'
        # ).extract_first()

        #
        # producao = response.xpath(
        #     './/td[2]/div/div/div/text()'
        # ).extract_first()
        #
        # coproducao = response.xpath(
        #     './/div[2]/table//tr[3]/td[2]//div/text()'
        # ).extract_first()
        #
        # yield {
        #     'title': title,
        #     'sinopse': sinopse,
        #     'producao': producao,
        # }





