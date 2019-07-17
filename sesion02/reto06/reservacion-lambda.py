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

elementos.sort(key=lambda x: x['precio'] * x['cantidad'] * -1)

total = 0
for elemento in elementos:
    total += elemento['precio'] * elemento['cantidad']

apartado = input("Desea conocer el apartado (si/no)?")

print("-"*63)
print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
for elemento in elementos:
    print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento['nombre'], 
                                              elemento['cantidad'],
                                              elemento['precio'], 
                                              elemento['cantidad'] * elemento['precio']))
print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
if len(apartado) > 0 and (apartado[0] == 'S' or apartado[0] == 's'):
    print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, total/10.0, 9))
