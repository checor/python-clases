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

`lista-de-enteros-funciones.py`

Generar una lista de enteros, mediante el uso de una función con nombre genera_lista(n), donde n corresponderá al tamaño.

```
Tamaño de lista: 5
0
1
2
3
4
```