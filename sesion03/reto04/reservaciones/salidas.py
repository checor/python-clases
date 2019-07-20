"""Módulo para conocer el apartado en pantalla"""

def imprime_reservacion(elementos, apartado=False):
    total = 0
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