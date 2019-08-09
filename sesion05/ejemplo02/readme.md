## Ejemplo 02

### Decoradores

Los decoradores son funciones que reciben otra función como parámetro, y devuelve otra función.

`mi_decorador.py`

```python
In [7]: def mi_decorador(funcion):
   ...:     def nueva(*args):
   ...:         # Codigo antes del llamado
   ...:         print("Llamada a la funcion", funcion.__name__)
   ...:         retorno = funcion(*args)
   ...:         # Codigo despues del llamado
   ...:         print("La función ha sido llamada")
   ...:         return retorno + 1 # Agrega 1 al resultado de la funcion
   ...:     return nueva
   ...:

In [8]: @mi_decorador
   ...: def mi_funcion(numero):
   ...:     return numero * 2
   ...:

In [9]: mi_funcion(5)
Llamada a la funcion mi_funcion
La función ha sido llamada
Out[9]: 11
```

Como se puede observar, un decorador agrega funcionalidad antes o después de ejecutar la función donde es aplicado. Esto permite aplicar un patrón de diseño donde los decoradores agregan fácilmante funcionalidad extra.

### Medición de tiempo

`tiempo.py`

Generar un decorador que cuente el tiempo de ejecución de una función. Probar una función creando una lista con 10, 100, 1000 y 10000 elementos numéricos aleatorios.

```
Lista de 10 elementos
Tiempo de ejecucion: 0.05 msecs
Lista de 100 elementos
Tiempo de ejecucion: 0.32 msecs
Lista de 1000 elementos
Tiempo de ejecucion: 1.08 msecs
Lista de 10000 elementos
Tiempo de ejecucion: 1.07 msecs
```
 
### Decorador @property

Este decorador se utiliza para leer o escribir atributos mediante funciones, o bien, hacerlo de sólo lectura. En otros lenguajes, es mejor conocido como setters y getters. Veamos este ejemplo:

`dec_property.py`
Crear una clase llamada TemperaturaC que permita almacenar una temperatura en grados Celcius. Prevenir cualquier temperatura debajo de -273° C (cero absoluto).
```
Obteniendo temperatura
Temperatura: 30° C

Cambiando temperatura a 45° C
Guardada nueva temperatura

Cambiando temperatura a -500° C
Temperatura debajo de -273° C no es posible

Obteniendo temperatura
Temperatura final: 45° C
```
