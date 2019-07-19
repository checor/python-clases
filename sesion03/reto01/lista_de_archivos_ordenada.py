import os

# En este reto, los alumnos pueden usar las estruturas y la forma que deseen
# Para este caso, se ejemplificará con 2 listas
files = os.listdir()
sizes = [os.path.getsize(x) for x in files]

# Explicar que zip sirve para intercalar 2 o mas listas
data = list(zip(files, sizes))
data.sort(key = lambda x: x[1])

print("-" * 40)
for _file, size in data:
    print("{:<35}{:5}".format(_file, size))
print("-" * 40)