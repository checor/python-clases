n = input("Tamaño de la lista: ")

if not n.isdigit():
    print("Número invalido")

else:
    n = int(n)

    lista = list(range(n))
    for i in lista:
        print(i)

