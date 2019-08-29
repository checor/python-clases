import requests
from bs4 import BeautifulSoup


PAGE = "http://books.toscrape.com/"

def scrap_books(page):
    soup = BeautifulSoup(page, features="html.parser")
    products = soup.find_all("article", {'class': 'product_pod'})
    books = []
    for product in products:
        title = product.find("a", {"title": True}).text
        price = product.find("p", {"class": "price_color"}).text
        books.append([title, price])
    return books

def print_books(books):
    print("-" * 49)
    print("|{:40}|{:4}|".format("AUTOR", "PRECIO"))
    print("-" * 49)
    for book in books:
        print("|{:40}|{:4}|".format(book[0], book[1]))
    print("-" * 49)

        


if __name__ == "__main__":
    print("Obteniendo libros. . .")
    print("")
    response = requests.get(PAGE)
    if response.status_code == 200:
        books = scrap_books(response.content)
        print_books(books)
