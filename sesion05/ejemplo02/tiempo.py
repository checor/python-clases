import time
import random

def tiempo_ejecucion(funcion):
    def ejecutar(*args):
        inicio = time.time()
        r = funcion(*args)
        fin = time.time()
        tiempo_transcurrido = (fin - inicio) * 1000
        print("Tiempo de ejecucion: {:.2f} msecs".format(tiempo_transcurrido))
        return r
    return ejecutar

@tiempo_ejecucion
def genera_lista(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100))
    return lista

print("Lista de 10 elementos")
a = genera_lista(10)
print("Lista de 100 elementos")
b = genera_lista(100)
print("Lista de 1000 elementos")
c = genera_lista(1000)
print("Lista de 10000 elementos")
d = genera_lista(1000)