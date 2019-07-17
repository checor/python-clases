def genera_lista(n):
    lista = list()
    for i in range(n):
        lista.append(i)
    return lista

n = input("Tamaño de lista: ")

if n.isdigit():
    n = int(n)
else:
    print("Cantidad no válida")
    quit()

lista = genera_lista(n)

for i in lista:
    print(i)