## Ejemplo 02

### Operaciones con listas

Las listas pueden modificar, agregar y eliminar sus elementos. También pueden hacerse operaciones con ellas.

`modificando-listas.py`
```python
In [1]: l1 = ["a", "b", "c"]

In [2]: # Agrega un elemento al final de la lista

In [3]: l1.append("d")

In [4]: l1
Out[4]: ['a', 'b', 'c', 'd']

In [5]: l2 = [ 2, 3, 4, 5]

In [6]: # Inserta un elemento en cualquier lado de la lista

In [7]: l2.insert(0, 1)  # Indice, valor

In [8]: l2
Out[8]: [1, 2, 3, 4, 5]

In [9]: # Sumando listas

In [10]: l1 + l2
Out[10]: ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5]

In [11]: # Convertir a cadena

In [12]: "".join(l1)
Out[12]: 'abcd'

In [13]: ", ".join(l1)
Out[13]: 'a, b, c, d'

In [14]: # Usando random

In [15]: import random

In [16]: random.choice([1,2,3,4,5,6])
Out[16]: 5 # Elemento al azar

In [17]: l3 = list("abc123")

In [18]: random.shuffle(l3) # Desordena la lista

In [19]: l3
Out[19]: ['a', '3', 'c', 'b', '2', '1']

In [20]: lista_de_listas = [ [0,1,2], [3,4,5], [6,7,8] ]

In [21]: # Accediendo a valores

In [22]: lista_de_listas[1][0]
Out[22]: 3

In [23]: lista_de_listas[2]
Out[23]: [6, 7, 8]

```

`genera-claves.py`

Objetivo: Generar `n`claves de forma aleatoria, que deben tener al menos 1 mayúscula, una minúscula y un dígito, con longitud `m`. `n` y `m` serán solicitados al usuario, este úlutmo con un valor de 8 por defecto.

```
$ python3 genera-claves.py 
Número de claves a generar: 3
Longitud de claves (8): 
wDxIg9BJ
8U3lNI2E
0QiZqQRY
```