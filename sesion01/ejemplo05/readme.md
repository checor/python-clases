## Estruturas de control

### If, elif, else
Permite ejecutar cierta porción de código, si es que una condición se evalúa como verdadero.
Elif, permite probar otra condición, en caso de no cumplirse la anterior. Else, ejecuta una pieza de código, si ninguna condición se cumplió.

`positivo_negativo.py`
```python
In [1]: numero = 0                                                                                                                                                                           

In [2]: if numero == 0: 
   ...:     print("Este numero es 0") 
   ...: elif numero > 0: 
   ...:     print("Este numero es positivo") 
   ...: else: 
   ...:     print("Este numero es negativo") 
   ...:                                                                                                                                                                                      
Este numero es 0

```

### While
Ejecuta una pieza de código, en ciclos, hasta que la condición indicada se deje de cumplir.
`while_5.py`
```
In [5]: while n<5: 
   ...:     print("Numero {}".format(n)) 
   ...:     n = n + 1 
   ...:                                                                                                                                                                                      
Numero 0
Numero 1
Numero 2
Numero 3
Numero 4

`for_5.py`
```
### For
Itera sobre cada uno de los elementos que se le indiquen.
```
In [7]: for i in range(5): 
   ...:     print("Numero {}".format(i)) 
   ...:      
                                                                                                                                                        
Numero 0
Numero 1
Numero 2
Numero 3
Numero 4

```
#### Ejemplo: par_non.py
De una lista de 10 numeros, imprimir en pantalla par o non, dependiendo de si son divisibles entre 2 o no.

```python
In [8]: for i in range(11): 
   ...:     if i % 2 == 0: 
   ...:         print("Par") 
   ...:     else: 
   ...:         print("Non") 
   ...:   
   
Par
Non
Par
Non
Par
Non
Par
Non
Par
Non

```
