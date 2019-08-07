class Animal():
    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido
    
    def grito(self):
        print("El {} hace {}".format(self.nombre, self.sonido))
    
    def info(self):
        print("Nombre: {} - Especie {}".format(self.nombre, self.especie))

    def __str__(self):
        return "{:15}|{:15}|{:15}".format(self.nombre, self.especie, self.sonido)

class Ave(Animal):
    def __init__(self, nombre, especie, sonido, vuela=True):
        super().__init__(nombre, especie, sonido)  # Extiende la clase
        self.vuela = vuela

    def volar(self):
        if self.vuela:
            print("{} se eleva en el aire".format(self.nombre))
        else:
            print("{} aletea pero no vuela".format(self.nombre))
    
    def __str__(self):
        return "{:15}|{:15}|{:15}|{:15}".format(self.nombre, self.especie, self.sonido, str(self.vuela))

def imprimir(animales):
    print("{:15}|{:15}|{:15}|{:15}".format("NOMBRE", "ESPECIE", "SONIDO", "VUELA"))
    for animal in animales:
        print(animal)

animales = [
    Animal("Perro", "Canis", "Guau"),
    Animal("Gato", "Felino", "Miau"),
    Ave("Paloma", "Columba", "Cucu", True),
    Ave("Gallo", "Gallus", "Kikiriki", False)
]

imprimir(animales)