class TemperaturaC:
    def __init__(self, temperatura=0):
        self._temperatura = temperatura
    
    @property
    def temperatura(self): # Getter
        print("Obteniendo temperatura")
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, valor): # Setter
        if valor < -273:
            print("Temperatura debajo de -273° C no es posible")
        else:
            self._temperatura = valor
            print("Guardada nueva temperatura")

temp = TemperaturaC(30)

print("Temperatura: {}° C".format(temp.temperatura))
print("")
print("Cambiando temperatura a 45° C")
temp.temperatura = 45
print("")
print("Cambiando temperatura a -500° C")
temp.temperatura = -500
print("")
print("Temperatura final: {}° C".format(temp.temperatura))
