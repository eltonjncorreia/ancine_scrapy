# -*- coding: utf-8 -*-
import scrapy


class AncineSpider(scrapy.Spider):
    # spider's name
    name = 'ancine'
    # domain
    allowed_domains = ['ancine.gov.br']
    # url name
    start_urls = ['https://www.ancine.gov.br/pt-br/brasil-nas-telas']

    # parse
    def parse(self, response):
        # is capturing the links, through the table
        items = response.xpath('//*[@id="conteudo"]/div/div/table/tbody/tr')

        # is capturing href and passes the captured items to the method
        for item in items:
            urls = item.xpath('.//td/h3/a/@href').extract_first()

            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.detail)

        # advanced on page
        next_page = response.xpath(
                    '//*[@id="conteudo"]/div//ul/li//a/@href'
        ).extract_first()

        # takes only the href and goes to the proper function parse()
        if next_page:
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(next_page), callback=self.parse)

    # receives the response and displays the data
    def detail(self, response):
            # was used .css, because I found it simpler and readable,
            # but the xpath "" could be used.
            yield {
                'title': response.css(
                    'div.content-header h2::text').extract_first(),

                'sinopse': response.css(
                    'div.field-item p::text').extract_first(),

                'image': response.xpath(
                    './/div//table//a/img/@src').extract_first()

            }
