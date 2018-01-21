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


            # yield {
            #    'url': urls
            # }
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.detail)

        if urls:
            # yield scrapy.Request(self.url.format('pt-br/brasil-nas-telas'))
            yield scrapy.Request('https://www.ancine.gov.br{}'.format(urls), callback=self.parse)


    def detail(self, response):
        self.log("estou na funcao "+response.url)




# response.xpath('//*[@id="conteudo"]/div[contains(@class, "node clear-block")]').extract_first()








#
# # -*- coding: utf-8 -*-
# import scrapy
#
#
# class AncineSpider(scrapy.Spider):
#     name = 'ancine'
#
#     allowed_domains = ['ancine.gov.br/brasil-nas-telas']
#     start_urls = ('https://www.ancine.gov.br/brasil-nas-telas/',)
#
#     # title = response.xpath('//*[@id="node-23822"]/div/h2/text()').extract_first()
#
#
#     def parse(self, response):
#         items = response.xpath('//*[@id="conteudo"]/div/div/table/tbody/tr')
#         # items = response.xpath('//table[contains(@class, "views-table")]/tbody/tr')
#
#         for item in items:
#             url = item.xpath('./td/h3/a').extract_first()
#
#             yield scrapy.Request(response.urljoin(url), callback=self.detail)
#
#         # response.xpath('//*[@id="conteudo"]/div/div/table/tbody/tr/td/h3/a').extract_first()
#
#
#     def detail(self, response):
#         self.log(response.url)
#
#
#
