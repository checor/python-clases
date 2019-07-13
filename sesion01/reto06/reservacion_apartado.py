elemento1 = "Habitación doble"
precio1 = 1500
cantidad1 = 7
subtotal1 = precio1 * cantidad1

elemento2 = "Transporte"
precio2 = 3000.0
cantidad2 = 2
subtotal2 = precio2 * cantidad2

elemento3 = "Reserva en evento"
precio3 = 3999.99999999
cantidad3 = 1
subtotal3 = precio3 * cantidad3

elemento4 = "Tour en lancha"
precio4 = 2170
cantidad4 = 1
subtotal4 = precio4 * cantidad4

elemento5 = "Alimentos y bebidas"
precio5 = 5000
cantidad5 = 7
subtotal5 = precio5 * cantidad5

apartado = input("Desea conocer el apartado (si/no)?")

total = subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5
print("-"*63)
print("{:32}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PRECIO", "SUBTOTAL"))
print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento1, cantidad1, precio1, subtotal1))
print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento2, cantidad2, precio2, subtotal2))
print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento3, cantidad3, precio3, subtotal3))
print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento4, cantidad4, precio4, subtotal4))
print("{:32}|{:9}|{:9.2f}|{:9.2f}".format(elemento5, cantidad5, precio5, subtotal5))
print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+2, total, 9))
if len(apartado) > 0 and (apartado[0] == 'S' or apartado[0] == 's'):
    print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+2, total/10.0, 9))