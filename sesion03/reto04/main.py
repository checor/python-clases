from reservaciones import entradas, salidas

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

apartado = entradas.requiere_apartado()

salidas.imprime_reservacion(elementos, apartado)