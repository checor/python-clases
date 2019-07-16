#  Estructuras de datos y funciones

## Objetivos

* Conocer el uso y sintaxis de las estructuras para almacenar y acceder a elementos.
* Aprender a utilizar funciones en Python.
* Conocer las bases de la progración estructurada y el concepto DRY (*Don't repeat yourself*)

## Ejemplo 01

### Estructuras de datos

### Listas
Son secuencias de datos mutables, accesibles mediante un índice. Pueden contener cualquier tipo de dato, y no necesariamente deben ser del mismo tipo.

`creacion_de_listas.py`
```python 
n [1]: # Creando una lista

In [2]: l1 = []

In [3]: l2 = list()

In [4]: l1 == l2 #Ambas formas son validas
Out[4]: True

In [5]: # Creando una lista con enteros

In [6]: l2 = [1, 2, 3, 4, 5]

In [7]: # Creando una lista con floats

In [8]: l3 = [1.2, 3.5, 6.5, 0.7, 4.6]

In [9]: # Creando una lista con strings

In [10]: l4 = ["a", "agg", "Hola Lista"]

In [11]: # Lista con productos mixtos

In [12]: l5 = [10, 5.0, "Doscientos"]

In [13]: type(l5)
Out[13]: list
```
#### Ejemplo
`listas-de-enteros.py`
Crear e imprimir una lista con números enteros, comnezando con 0, y finalizando con un número entero definido por el usuario.

```
$ python3 lista-de-enteros.py
Tamaño de la lista: 10
0
1
2
3
4
5
6
7
8
9
```

Este script, que parece inofensivo a simple vista, puede colapsar un equipo! Si la lista es demasiado grande, puede llenar la memoria RAM.

## Reto 01

Modifica el archivo `lista-de-enteros.py` para poner un límite en el valor máximo de la lista, en 50 millones.

A su vez, imprime la lista en enteros como flotantes.

```
$ python3 lista-de-flotantes.py
Tamaño de la lista: 4
0.0
1.0
2.0
3.0
```

## Ejemplo 02

### Operaciones con listas

Las listas pueden modificar, agregar y eliminar sus elementos. También pueden hacerse operaciones con ellas.

`modificando_listas.py`
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

In [21]: l3
Out[21]: ['a', '3', 'c', 'b', '2', '1']
```

## Ejemplo 0x

### Tuplas

Las tuplas son secuencias de objetos, similares a las listas, con la diferencia que su contenido y tamaño no es modificable.

Debido a que no son modificable, son más rápidas que las listas, por lo que se recomienda su uso si no se necesita modificar su composición.
`tuplas.py`
```

