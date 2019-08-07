from producto import Producto
from reservaciones import entradas, salidas

elementos = [
    Producto("Habitacion doble", 150000.0, 3),
    Producto("Transporte", 3000.0, 2),
    Producto("Tour en lancha", 2170, 1),
    Producto("Alimentos y bebidas", 5000, 2)
]

elementos.sort(key=lambda x: x.precio * x.cantidad * -1)

apartado = entradas.requiere_apartado()

salidas.imprime_reservacion(elementos, apartado)