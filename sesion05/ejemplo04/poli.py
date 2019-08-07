class A:
    def saludo(self):
        print("Soy la primera clase, la A")

class B:
    def saludo(self):
        print("Soy la segunda clase, la B")

a = A()
b = B()

lista = [a, b, a, b]  # Clases distintas

for objeto in lista:
    objeto.saludo()