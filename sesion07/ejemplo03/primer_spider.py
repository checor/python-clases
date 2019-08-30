import scrapy

class QuotesSpider(scrapy.Spider):
    # Nombre de la araña
    name = 'quotes'
    # Indica las URL's a visitar inicialmente, pero no las únicas. Se podrá navegar en ella.
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        # Se puede navegar por el HTML o mediante CSS
        # Para este caso, buscaremos todas las etiquetas <div> con las clase quote
        for quote in response.css('div.quote'):  
            # Yield es para entregar la información en forma de diccionario.
            # scrapy se encarga de convertir estos datos al formato espcificado.
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            # También podemos dirigirnos a otra página mediante el comando response.follow(url, parser)
            # Este comando es opcional
            yield response.follow(next_page, self.parse)
