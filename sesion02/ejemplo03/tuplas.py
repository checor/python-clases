# Creando un set 
s1 = set()
print(type(set))

s1 = {1, 2, 3, 4, 5}
s1.add(6)  # Agregando elementos
print(s1)

s1.remove(6)  # Quitando elementos
print(s1)

print(list(s1))

s2 = {4, 5, 6, 7, 8}
print(s1 & s2) # Union 

print(s1.intersection(s2))  # Interseccion