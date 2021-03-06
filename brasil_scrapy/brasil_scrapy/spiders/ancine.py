import scrapy


class AncineSpider(scrapy.Spider):
    name = 'ancine'

    start_urls = ['https://www.ancine.gov.br/pt-br/brasil-nas-telas']

    def parse(self, response):
        for div in response.css('table tr'):
            item = div.css('h3 a::attr(href)').extract_first()

            yield scrapy.Request('https://www.ancine.gov.br{}'.format(item), callback=self.detail)

        for div in response.css('div.item-list li'):
            next_page = div.css('a::attr(href)').extract_first()
            if next_page:
                yield scrapy.Request('https://www.ancine.gov.br{}'.format(next_page), callback=self.parse)

    def detail(self, response):
        if response.css('div.field-item p::text').extract_first() is not None:
            sin = response.css('div.field-item p::text').extract_first()
        else:
            sin = response.css('div.field-item::text').extract_first()

        yield {
            'title': response.css('div.content-header h2::text').extract_first(),
            'sinopse': sin,
            'produção': response.css('div.field-name-field-produtora div::text').extract_first(),
            'genero': response.css('div.field-name-field-genero div::text').extract_first(),
            'data-lancamento': response.css('span.date-display-single::text').extract_first(),
            'image': response.css('table.tb-detalhes td img::attr(src)').extract_first()
        }

