import scrapy
import csv
from selenium import webdriver

class Selenium(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = [
        'https://www.example.com/'
    ]    

    def __init__(self):
        self.driver = webdriver.Chrome() # Driver de Selenium

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)