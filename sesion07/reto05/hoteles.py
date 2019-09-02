import scrapy
from scrapy.selector import Selector
from selenium import webdriver # Driver, maneja Chrome, Firefox, IE...
from selenium.webdriver.support.ui import WebDriverWait # Para esperar una condición en el navegador
from selenium.webdriver.support import expected_conditions as EC # Para definir la condicion esperada
from selenium.webdriver.common.by import By # Para localizar elementos en un documento HTML
from selenium.common.exceptions import TimeoutException # Excepcion si no se cumple la condición después de X tiempo

class Selenium(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = [
        'https://www.tripadvisor.com.mx/Hotels-g187147-Paris_Ile_de_France-Hotels.html'
    ]
    max_pages = 5 

    def __init__(self):
        self.driver = webdriver.Chrome() # Driver de Selenium

    def parse(self, response):
        # Con driver.get, le indicamod al navegador que cargue la página indicada
        page = self.driver.get(response.url)
        try:
            # Con este comando indicamos que espero 10 segundos máximo, o hasta que encuentre un elemento
            # con la clase QUOTE, que para este caso, sginifica que el Javascript ha cargado exitosamente
            # y que los datos están listos para obtenerse
            myElem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'hasDates')))
            print("Pagina lista!")
        except TimeoutException:
            print("Tardó mucho tiempo en cargar!")
        
        # Aquí, cargamos el contenido del navegador en un selector, para realizar el scraping
        selector = Selector(text = self.driver.page_source)

        # Realizarmos el scraping de manera normal, con el elemento selector
        for hotel in selector.xpath('//div[contains(@class, "main_col")]'):  
            price = hotel.xpath('.//div[contains(@class, "price")]/text()').get()
            price = float(price.replace('$', '').replace(',', ''))
            rating = hotel.xpath('.//a[contains(@class, "ui_bubble_rating")]/@alt').get()[0:3]
            if '.' not in rating:
                rating = rating[0:2]
            rating = float(rating)
            yield {
                'name': hotel.xpath('.//a[contains(@class, "property")]/text()').get(),
                'price': price,
                'rating': rating
            }

        next_page = selector.css('a.next').attrib['href']
        if next_page is not None and self.max_pages > 0:
            self.max_pages -= 1
            # Response.follow para seguir con la siguiente página, de existir
            yield response.follow(next_page, self.parse)