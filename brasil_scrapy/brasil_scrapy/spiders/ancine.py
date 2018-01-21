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

        next_page = response.xpath(
            '//*[@id="conteudo"]/div//ul/li//a/@href'
        ).extract_first()

        if next_page:
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(next_page), callback=self.parse)


    def detail(self, response):
        self.log(response.url)
        title = response.xpath(
            './/div[contains(@class, "content-header")]//h2/text()'
        ).extract_first()

        sinopse = response.xpath(
            './/tr/td/b/text()'
        ).extract_first()

        producao = response.xpath(
            './/td[2]/div/div/div/text()'
        ).extract_first()

        yield {
            'title': title,
            'sinopse': sinopse,
            'producao': producao,
        }





