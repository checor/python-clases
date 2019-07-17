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