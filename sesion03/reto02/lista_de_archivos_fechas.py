import os
from datetime import datetime

# En este reto, los alumnos pueden usar las estruturas y la forma que deseen
# Para este caso, se ejemplificará con 2 listas
files = os.listdir()
sizes = [os.path.getsize(x) for x in files]
dates = [os.path.getmtime(x) for x in files]

# Explicar que zip sirve para intercalar 2 o mas listas
data = list(zip(files, sizes, dates))
data.sort(key = lambda x: x[1])

print("-" * 80)
print("{:<35}{:5}{:>39}".format("NOMBRE", "TAMAÑO", "FECHA"))
print("-" * 80)
for _file, size, timestamp in data:
    date = datetime.fromtimestamp(timestamp)
    print("{:<35}{:5}{:>40}".format(_file, size, date.strftime("%c")))
print("-" * 80)