## Ejemplo 06

### Funciones lambda

Las funciones lambda son funciones anónimas, es decir, sin un nombre, y por lo general se utilzan una sola vez. Normalmente se crean para pasarlas a otras funciones de orden superior.

`funciones-lambda.py`
```python
In [1]: nombre = lambda: print("Hola soy lambda") 

In [2]: nombre()                          
Hola soy lambda

In [3]: # Con parametros                                                         
In [4]: nombre = lambda nom: print("Hola {}!".format(nom))

In [5]: nombre("Bedu")                                
Hola Bedu!

```

`lambda-sort.py`

Las listas puede ordenarse mediante la función sort. Normalmente, se ordenan de menor a mayor. Este comportamiento se puede cambiar mediante una función lambda.

Crear una lambda para invertir el orden de una lista de 5 elementos.

```
Lista antes de ordenar: [1, 5, 5, 1, 7]
Lista de menor a mayor: [1, 1, 5, 5, 7]
Lista de mayor a menor: [7, 5, 5, 1, 1]
```