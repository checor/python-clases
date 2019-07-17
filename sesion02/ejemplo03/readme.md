## Ejemplo 03

### Tuplas

Las tuplas son secuencias de objetos, similares a las listas, con la diferencia que su contenido y tamaño no es modificable.

Debido a que no son modificables, son más rápidas que las listas, por lo que se recomienda su uso si no se necesita modificar su composición.
`tuplas.py`
```python
In [1]: # Creando una tupla
In [2]: t1 = ()

In [3]: t2 = tuple()

In [4]: # Obteniendo el tipo de dato

In [5]: type(t1)
Out[5]: tuple

In [6]: type(t1) == type(t2)
Out[6]: True

In [7]: # Tupla de un elemento

In [8]: t3 = (1, )  # Ojo con la coma

In [9]: # Asignacion multiple con tupla

In [10]: a, b = (10, 20)

In [11]: print(a, b)
10 20

In [12]: # Modificando (no se puede)

In [13]: t1.insert(0, 1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-13-a59a2ffbbbe6> in <module>
----> 1 t1.insert(0, 1)

AttributeError: 'tuple' object has no attribute 'insert'
```

### Sets

Los conjuntos o *sets*, son solecciones no mutables y no ordenadas, utilizados principalmente en operaciones de lógica y matemática.

A diferencia de las listas y tuplas, al no estar ordenadas, no se puede acceder mediante un índice. Se puede utlizar un *for* para acceder a todos sus elementos uno por uno. Tampoco permite elementos repetidos.

`sets.py`
```python
In [1]: # Creando un set 

In [2]: s1 = set()

In [3]: type(set)
Out[3]: type

In [4]: s1 = {1, 2, 3, 4, 5}

In [5]: s1.add(6)  # Agregando elementos

In [6]: s1
Out[6]: {1, 2, 3, 4, 5, 6}

In [7]: s1.remove(6)  # Quitando elementos

In [8]: s1 
Out[8]: {1, 2, 3, 4, 5}

In [9]: list(s1)  # Convirtiendo a listas
Out[9]: [1, 2, 3, 4, 5]

In [10]: # Operaciones

In [11]: s2 = {4, 5, 6, 7, 8}

In [12]: s1 & s2 # Union 
Out[12]: {4, 5}

In [13]: s1.intersection(s2)  # Interseccion
Out[13]: {4, 5}
```