import random

n = input("Número de claves a generar: ")

if not n.isdigit():
    print("Valor inválido")
    quit()
else:
    n = int(n)

m = input("Longitud de claves (8): ")

if m == "":
    m = 8
elif m.isdigit():
    m = int(m)
else:
    print("Valor inválido")
    quit()

# Listas de elementos para generar claves
digits = "1234567890"
minus = "qwertyuiopasdfghjklzxcvbnm"
mayus = minus.upper()

for i in range(n):
    # Obtener minimo 1 de cada elemento
    digito = random.choices(digits)
    minuscula = random.choices(minus)
    mayuscula = random.choices(mayus)
    # El resto seran elementos al azar de las 3 listas
    resto = random.choices(digits + minus + mayus, k=m-3)
    contrasena = digito + minuscula + mayuscula + resto
    random.shuffle(contrasena) # Mezclar los elementos para cambiar su orden
    contrasena = "".join(contrasena) # Convertirla a string
    print(contrasena)
