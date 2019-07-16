n = input("Tamaño de la lista: ")

if not n.isdigit():
    print("Número no válido")
else:
    n = int(n)
    if n > 50000000:
        print("Número demasiado grande")
    else:
        lista = list(range(n))
        for i in lista:
            print(float(i))
