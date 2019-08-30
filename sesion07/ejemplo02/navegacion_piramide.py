import requests
from bs4 import BeautifulSoup, element

def read_page():
    with open("piramide.html", 'r') as html:
        page = html.read()
    return page

def navigate_page(page):
    soup = BeautifulSoup(page, features="html.parser")
    # Content tiene una lista de todos los elementos
    html = soup.contents[0]
    body = html.contents[1]
    ecopyramyd = body.contents[1]
    # Children etnre un iterable para acceder a sus elementos con un for
    uls = ecopyramyd.children
    for ul in uls:
        # NavigableString es un string entre tags, se debe ignorar
        if type(ul) == element.NavigableString:
            continue
        print(ul['id'].capitalize())
        for child in ul.children:
            if type(child) == element.NavigableString:
                continue
            li = child.contents[0]
            name = li.nextSibling.text.capitalize()
            number = li.nextSibling.nextSibling.nextSibling.text.capitalize()
            print("\t-{}: {}".format(name, number))



if __name__ == '__main__':
    page = read_page()
    navigate_page(page)