l1 = ["a", "b", "c"]
print("l1:", l1)

l1.append("d")
print("l1:", l1)

l2 = [ 2, 3, 4, 5]
print("l2:", l2)

l2.insert(0, 1) 
print("l2:", l2)

l1 + l2
print("l1 + l2 = {}".format(l1 + l2))

print("".join(l1))


print(", ".join(l1))
print('a, b, c, d')


import random
random.choice([1,2,3,4,5,6])

l3 = list("abc123")
print(l3)

random.shuffle(l3)
print(l3)

lista_de_listas = [ [0,1,2], [3,4,5], [6,7,8] ]
print(lista_de_listas)
print(lista_de_listas[1][0])
print(lista_de_listas[2])

