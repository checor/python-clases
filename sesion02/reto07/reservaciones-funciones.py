def calcula_total(elementos):
    total = 0
    for elemento in elementos:
        total += elemento['precio'] * elemento['cantidad']
    return total

def ordena_elementos(elementos):
    elementos.sort(key=lambda x: x['precio'] * x['cantidad'] * -1)
    return elementos

def calcula_apartado(total):
    return total * .1

def imprimir_reservacion(elementos):
    total = calcula_total(elementos)
    elementos = ordena_elementos(elementos)
    print("-"*63)
    print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
    for elemento in elementos:
        print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento['nombre'], 
                                                elemento['cantidad'],
                                                elemento['precio'], 
                                                elemento['cantidad'] * elemento['precio']))
    print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
    if len(apartado) > 0 and (apartado[0] == 'S' or apartado[0] == 's'):
        print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, calcula_apartado(total), 9))



elementos = [
    {
        "nombre": "Habitación doble",
        "precio": 150000.0,
        "cantidad": 3
    },
    {
        "nombre": "Transporte",
        "precio": 3000.0,
        "cantidad": 2
    },
    {
        "nombre": "Tour en lancha",
        "precio": 2170,
        "cantidad": 1
    },
    {
        "nombre": "Alimentos y bebidas",
        "precio": 5000,
        "cantidad": 2
    },
]

apartado = input("Desea conocer el apartado (si/no)?")

imprimir_reservacion(elementos)
