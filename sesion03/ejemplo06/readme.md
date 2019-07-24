## Ejemplo 06

### Numpy

Numpy es una librería de Python, que agrega mayor soporte de matrices y vectores al lenguaje, así como mayor velocidad en procesamiento de los mismos. Numpy es la base para gran cantidad de librerías de *data science* y *machine learning*.

Para instalarlo basta con correr `pip3 install numpy`.

`uso_numpy.py`

```python
In [1]: import numpy as np

In [2]: a1 = np.array([1,2,3])

In [3]: type(a1)                                                                                                                     
Out[3]: numpy.ndarray

In [4]: a1[0]                                                                                                                        
Out[4]: 1

In [5]: a2 = np.full((3,3), True, dtype=bool) 

In [6]: a2                                                                                                                           
Out[6]: 
array([[ True,  True,  True],
       [ True,  True,  True],
       [ True,  True,  True]])

In [7]: a3 = np.arange(5, 10)

In [8]: a3                                                                                                                           
Out[8]: array([5, 6, 7, 8, 9])

In [9]: np.sum(a3)                                                                                                                   
Out[9]: 35

In [10]: a4 = np.arange(10)                                                                                                          

In [11]: a4                                                                                                                          
Out[11]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [12]: a4.reshape(2, -1)                                                                                                           
Out[12]: 
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
```

`cuadrado_magico.py`

Detecta si un array de 2 dimensiones de numpy, es un cuadrado mágico. Un cuadrado mágico se compone de un array de dimensiones n x n, en los cuiales cada fila y columna, tendrá el mismo valor, sumando cada fila y columna. Supón que los valores en el array no estarán repetidos en ningún momento.

```
[[2 7 6]
 [9 5 1]
 [4 3 8]]
Es cuadrado mágico? True

[[2 7 6]
 [9 1 5]
 [3 4 8]]
Es cuadrado mágico? False
```