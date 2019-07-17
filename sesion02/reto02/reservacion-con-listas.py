elementos = [
    "Habitación doble",
    "Transporte",
    "Reserva en evento",
    "Tour en lancha",
    "Alimentos y bebidas"
]

precios = [
    150000.0,
    3000.0,
    3999.99999999,
    2170,
    5000
]

total = sum(precios)

print("-"*80)
print("{:59}|{:20}".format("RESERVACION", "PRECIO"))
print("-"*80)
print("{:59}|{:20.2f}".format(elementos[0], precios[0]))
print("{:59}|{:20.2f}".format(elementos[1], precios[1]))
print("{:59}|{:20.2f}".format(elementos[2], precios[2]))
print("{:59}|{:20.2f}".format(elementos[3], precios[3]))
print("{:59}|{:20.2f}".format(elementos[4], precios[4]))
print("{:>59}|{:20.2f}".format("Total ", total))
