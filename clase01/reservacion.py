elemento1 = "Habitación doble"
precio1 = 150000.0

elemento2 = "Transporte"
precio2 = 3000.0

elemento3 = "Reserva en evento"
precio3 = 3999.99999999

elemento4 = "Tour en lancha"
precio4 = 2170

elemento5 = "Alimentos y bebidas"
precio5 = 5000

total = precio1 + precio2 + precio3 + precio4 + precio5 
print("-"*80)
print("{:59}|{:20}".format("RESERVACION", "PRECIO"))
print("-"*80)
print("{:59}|{:20.2f}".format(elemento1, precio1))
print("{:59}|{:20.2f}".format(elemento2, precio2))
print("{:59}|{:20.2f}".format(elemento3, precio3))
print("{:59}|{:20.2f}".format(elemento4, precio4))
print("{:59}|{:20.2f}".format(elemento5, precio5))
print("{:>59}|{:20.2f}".format("Total ", total))
