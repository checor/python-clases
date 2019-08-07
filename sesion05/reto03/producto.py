class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def subtotal(self):
        return self.precio * self.cantidad

    def iva(self):
        return self.precio * self.cantidad * 0.16

class Hotel(Producto):
    def __init__(self, nombre, precio, cantidad, personas=1):
        super().__init__(nombre, precio, cantidad)
        self.personas = personas

    @property
    def subtotal(self):
        return self.precio * self.cantidad * self.personas