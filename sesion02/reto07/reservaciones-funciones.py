def requiere_apartado():
    """Pide entrada al usuario para saber si desea conocer su apartado. Repite si es necesario."""
    while True:
        apartado = input("Desea conocer el apartado (si/no)?") 
        if len(apartado) == 0:
            print("Entrada inválida. Responda si o no.")
        elif apartado[0] == 'S' or apartado[0] == 's':
            return True
        elif apartado[0] == 'N' or apartado[0] == 'n':
            return False
        else:
            print("Entrada inválida. Responda si o no.")


def costo_total(elementos):
    total = 0
    for elemento in elementos:
        total += elemento['precio'] * elemento['cantidad']
    return total


def imprime_reservacion(elementos, apartado=False):
    total = costo_total(elementos)
    print("-"*63)
    print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
    for elemento in elementos:
        total += elemento['precio'] * elemento['cantidad']
        print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento['nombre'], 
                                                elemento['cantidad'],
                                                elemento['precio'], 
                                                elemento['cantidad'] * elemento['precio']))
    print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
    if apartado:
        print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, total/10.0, 9))

def ordenar_elementos(elementos):
    elementos.sort(key=lambda x: x['precio'] * x['cantidad'] * -1)


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

ordenar_elementos(elementos)
apartado = requiere_apartado()
imprime_reservacion(elementos, apartado)
    