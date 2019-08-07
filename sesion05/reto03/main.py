from producto import Producto, Hotel
from reservaciones import entradas, salidas

elementos = [
    Hotel("Hotel Plus", 15000.0, 3, 2),
    Producto("Transporte", 3000.0, 2),
    Producto("Tour en lancha", 2170, 1),
    Producto("Alimentos y bebidas", 5000, 2)
]

elementos.sort(key=lambda x: x.subtotal * -1)

apartado = entradas.requiere_apartado()

salidas.imprime_reservacion(elementos, apartado)