import random

def lista_random(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 9))
    return lista

# Creo una lista de 5 elementos al azar
lista = lista_random(5)
print("Lista antes de ordenar: {}".format(lista))

# Ordenamiento normal
lista.sort()
print("Lista de menor a mayor: {}".format(lista))

# La función lambda multiplica todos los elementos que va a comparar por -1
# nota: es lo mismo que sort(reverse=True)
lista.sort(key=lambda x: x * -1)
print("Lista de mayor a menor: {}".format(lista))