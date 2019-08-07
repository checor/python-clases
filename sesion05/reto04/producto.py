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

    def __str__(self):
        return "{:32}|{:9}|{:9}|{:9.2f}|{:9.2f}".format(self.nombre, 
                                                        self.cantidad,
                                                        "N/A",
                                                        self.precio, 
                                                        self.subtotal)

class Hotel(Producto):
    def __init__(self, nombre, precio, cantidad, personas=1):
        super().__init__(nombre, precio, cantidad)
        self.personas = personas

    @property
    def subtotal(self):
        return self.precio * self.cantidad * self.personas

    def __str__(self):
        return "{:32}|{:9}|{:9}|{:9.2f}|{:9.2f}".format(self.nombre, 
                                                        self.cantidad,
                                                        self.personas,
                                                        self.precio, 
                                                        self.subtotal)