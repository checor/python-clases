import scrapy

class PiramidSpider(scrapy.Spider):
    name = 'piramid'
    start_urls = [
        # Para utilizar archivos locales, se debe de utilizar el path completo
        'file:///home/checor/dev/python-clases/sesion07/ejemplo04/piramide.html'
    ]

    def parse(self, response):
        for ul in response.xpath("//ul"):
            for li in ul.xpath("li"):
                yield {
                    'name': li.xpath("div[@class='name']/text()").get(),
                    'number': li.xpath("div[@class='number']/text()").get(),
                    "type": ul.attrib['id']
                }