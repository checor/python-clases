from bs4 import BeautifulSoup

with open("piramide.html", "r") as html:
    soup = BeautifulSoup(html, "html.parser")

producers = soup.find(id="producers")
producers_name = producers.find_all("div", {"class": "name"})
producers_name = [name.text for name in producers_name]

print("Nombre de organismos productores:", producers_name)

elementos = soup.find_all("div", {"class": "number"})
elementos = [int(elemento.text) for elemento in elementos]

print("Numero total de elementos:", sum(elementos))

tigre = soup.find("div", string="tiger")
padres = 0 
while tigre.parent:
    padres += 1
    tigre = tigre.parent

print("La clase tigre tiene {} padres".format(padres))
