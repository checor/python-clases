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

## Reto 01: 

`lista-de-flotantes.py`

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

## Reto 02

`genera-claves-signos.py`

Modifica el script de ejemplo `genera-claves.py` para que también incluya cuando menos algún símbolo ($%&/#@-_=+-*) como parte de las claves.

```
$ python3 genera-claves-signos.py 
Número de claves a generar: 5
Longitud de claves (8): 8
U2$m=PE1
R+w%8kA1
$y3/tKHi
7m&/OZ0M
I1d/L-j-
```

`reservacion-con-listas.py`

Modifica el script de la sesión anterior `reto03/reservacion.py`, para que cada producto se almancene en una variable tipo lista.

```
-----------------------------------------------------------------
RESERVACION                                        | PRECIO    
-----------------------------------------------------------------
Habitación doble                                   |   15000.00
Transporte                                         |    3000.00
Reservación en evento                              |    3999.99
Tour en lancha                                     |   21750.00
Alimentos y bebidas                                |    5000.00
-----------------------------------------------------------------
                                              Total|  164170.00
```

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

## Ejemplo 04

### Diccionarios

Son objetos contenedores que contienen una llave (*key*), y un valor(*value*). Se accede a sus valores mediante el nombre de la llave, por lo cual se conoces como diccionarios.

`diccionarios.py`
```python
In [1]: # Creando diccionarios  

In [2]: d1 = {}

In [3]: d2 = dict() 

In [4]: type(d1) 
Out[4]: dict

In [5]: d3 = {"Calle": "Monte de las cruces", "Tel": "+555555501", "Ciudad": "Tijuana"} 

In [6]: d4 = {"Medicamento": "Paracetamol", "Dosis": 8}                          

In [7]: d3.keys() 
Out[7]: dict_keys(['Calle', 'Tel', 'Ciudad'])

In [8]: d4.values() 
Out[8]: dict_values(['Paracetamol', 8])

In [15]: for item, value in d3.items():  # Accediendo mediante for
    ...:     print(item, ":", value) 
    ...:                                   
Calle : Monte de las cruces
Tel : +555555501
Ciudad : Tijuana
```

### Reto 04

`reservacion_con_diccionarios.py`
Modifica el ejemplo del reto06 de la clase anterior, `reservacion-apartado.py`, para contener los productos en una sola variable, una lista con diccionarios. Las llaves de los diccionarios deben contener los valores de cada producto: nombre, precio, cantidad. Subtotal **no** debe formar parte del diccionario, calcularlo acorde.

Utilizar ciclos para mostrar todos los productos.


```
Desea conocer el apartado (si/no)?si
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PRECIO   |SUBTOTAL 
Habitación doble                |        3|150000.00|450000.00
Transporte                      |        2|  3000.00|  6000.00
Tour en lancha                  |        1|  2170.00|  2170.00
Alimentos y bebidas             |        2|  5000.00| 10000.00
                                              Total |468170.00
                                           Apartado | 46817.00
```

### Ejemplo 05

### Funciones

Son piezas de código delimitadas y que se les puede asignar un nombre, con el objetivo de modularizar o reutilizarse.

Una función puede recibir argumentos, y a su vez, retornar algún valor, si se require.

`funciones.py`
```python
In [1]: def hola(): 
   ...:     print("Hola mundo!") 
   ...:   

In [2]: hola() 
Hola mundo!

In [3]: def hola(nombre): 
   ...:     print("Hola {}".format(nombre)) 
   ...:

In [4]: hola("Bedu") 

Hola Bedu

In [5]: def cuadrado(a): 
   ...:     return a ** 2 
   ...:                                                                                                     

In [6]: a = cuadrado(5)                                                                                     

In [7]: a                                                                                                   
Out[8]: 25
```

`lista_de_enteros_funciones.py`

Generar una lista de enteros, mediante el uso de una función con nombre genera_lista(n), donde n corresponderá al tamaño.

```
Tamaño de lista: 5
0
1
2
3
4
```

## Reto 05

`genera-claves-funciones.py`

Modifica el script de generación de claves para que cada clave sea creada por una función llamada genera_claves()

```
$ python3 genera-claves.py 
Número de claves a generar: 3
Longitud de claves (8): 
wDxIg9BJ
8U3lNI2E
0QiZqQRY
```

## Ejemplo 06

### Funciones lambda

Las funciones lambda son funciones anónimas, es decir, sin un nombre, y por lo general se utilzan una sola vez. Normalmente se crean para pasarlas a otras funciones de orden superior.

`funciones_lambda.py`
```python
In [1]: nombre = lambda: print("Hola soy lambda") 

In [2]: nombre()                          
Hola soy lambda

In [3]: # Con parametros                                                         
In [4]: nombre = lambda nom: print("Hola {}!".format(nom))

In [5]: nombre("Bedu")                                
Hola Bedu!

```

`lambda_sort.py`

Las listas puede ordenarse mediante la función sort. Normalmente, se ordenan de menor a mayor. Este comportamiento se puede cambiar mediante una función lambda.

Crear una lambda para invertir el orden de una lista de 5 elementos.

```
Lista antes de ordenar: [1, 5, 5, 1, 7]
Lista de menor a mayor: [1, 1, 5, 5, 7]
Lista de mayor a menor: [7, 5, 5, 1, 1]
```

## Reto 06 

`reservacion-lambda.py`

Modificar el script del reto04 `reservacion-con-diccionarios.py`, para que se ordenen sus resultados, basándose en el subtotal de cada producto.

Utilizar la función sort de la lista de diccionarios, e indicarle mediante el lambda, como calcular el subtotal, para que lo ordene de esa manera, en un orden de mayor a menor.

```
Desea conocer el apartado (si/no)?si
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PRECIO   |SUBTOTAL 
Habitación doble                |        3|150000.00|450000.00
Alimentos y bebidas             |        2|  5000.00| 10000.00
Transporte                      |        2|  3000.00|  6000.00
Tour en lancha                  |        1|  2170.00|  2170.00
                                              Total |468170.00
                                           Apartado | 46817.00
```


### Reto final 

`reservaciones-funciones.py`

Divide la reservación de Bedu Travels de tal forma que se cuente con:
* Función para calcular el costo total
* Función para calcular el costo des apartado
* Función para ordenar los valores
* Una función para imprimir productos

```
Desea conocer el apartado (si/no)?si
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PRECIO   |SUBTOTAL 
Habitación doble                |        3|150000.00|450000.00
Alimentos y bebidas             |        2|  5000.00| 10000.00
Transporte                      |        2|  3000.00|  6000.00
Tour en lancha                  |        1|  2170.00|  2170.00
                                              Total |468170.00
                                           Apartado | 46817.00
```