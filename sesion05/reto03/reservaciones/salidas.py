"""Módulo para conocer el apartado en pantalla"""
from producto import Hotel

def imprime_reservacion(elementos, apartado=False):
    total = 0
    print("-"*63)
    print("{:32}|{:9}|{:9}|{:9}|{:9}".format("RESERVACION", "CANTIDAD", "PERSONAS", "PRECIO", "SUBTOTAL"))
    for elemento in elementos:
        total += elemento.subtotal
        if isinstance(elemento, Hotel):
            personas = elemento.personas
        else:
            personas = "N/A"
        print("{:32}|{:9}|{:9}|{:9.2f}|{:9.2f}".format(elemento.nombre, 
                                                elemento.cantidad,
                                                personas,
                                                elemento.precio, 
                                                elemento.subtotal))
    print("{:>{}}|{:{}.2f}".format("Total ", 32+9+9+9+2, total, 9))
    if apartado:
        print("{:>{}}|{:{}.2f}".format("Apartado ", 32+9+9+9+2, total/10.0, 9))