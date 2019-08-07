class Animal():
    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido
    
    def grito(self):
        print("El {} hace {}".format(self.nombre, self.sonido))
    
    def info(self):
        print("Nombre: {} - Especie {}".format(self.nombre, self.especie))

class Ave(Animal):
    def __init__(self, nombre, especie, sonido, vuela=True):
        super().__init__(nombre, especie, sonido)  # Extiende la clase
        self.vuela = vuela

    def volar(self):
        if self.vuela:
            print("{} se eleva en el aire".format(self.nombre))
        else:
            print("{} aletea pero no vuela".format(self.nombre))

paloma = Ave("Paloma", "Columba", "Cucu", True)
paloma.info()
paloma.volar()

gallina = Ave("Gallina", "Gallus", "Kikiriki", False)
gallina.info()
gallina.volar()