import requests
from bs4 import BeautifulSoup

def read_page():
    with open("piramide.html", 'r') as html:
        page = html.read()
    return page

def navigate_page(page):
    soup = BeautifulSoup(page)

if __name__ == '__main__':
    page = read_page()
    navigate_page(page)