## Ejemplo 04

### Creando tu propio módulo

Los módulos en Python son practicamente archivos con extensión .py pensados para ser reutilizados. En ellos, se definen funciones, clases y variables, así como código de inicialización.

`mi_primer_modulo.py`

Este primer módulo debe escribir en pantalla: "Hola, soy tu primer módulo"

```python
In [1]: !cat mi_primer_modulo.py
print("Hola, soy tu primer módulo")

In [2]: import mi_primer_modulo
Hola, soy tu primer módulo

In [3]: # Si lo importamos de nuevo, no se ejecutara de vuelta ese codigo

In [4]: import mi_primer_modulo

In [5]: 
```

El código que contiene cualquier código sólo es ejecutado una vez. Una vez que está importado, permanece en caché.

`tablas.py`

Este módulo deberá contener una función llamada `tabla(n)`, y deberá de imprimir la tabla del número n en pantalla. Sólo debe de contener la función dentro, sin que sea llamado.

```python
In [1]: !cat tablas.py
def tabla(n):
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n * i))
In [2]: import tablas

In [3]: tablas.tabla(3)
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

In [4]: tablas.tabla?
Signature: tablas.tabla(n)
Docstring: <no docstring>
File:      ~/dev/python-clases/sesion03/ejemplo03/tablas.py
Type:      function
```

`tablas2.py`

Los scripts en Python pueden ser módulo y función a la vez agregando una sección que sólo se ejecutará si se llamó directamente:

```python
if __name__ == "__main__":
    print("Me acabas de llamar directamente!")
```

También podemos escribir strings de documentación, definida entre 3 comillas dobles, a nivel módulo, función o clase.

Modificando el script `tablas.py`, agregando docstrings, y funcionamiento como archivo indepiendente, obtenemos lo siguiente:

```python
$ python3 tablas2.py 
TABLA DE DEL 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

$ipython

In [1]: import tablas2

In [2]: tablas2?
Type:        module
String form: <module 'tablas2' from '/home/sergio/dev/python-clases/sesion03/ejemplo03/tablas2.py'>
File:        ~/dev/python-clases/sesion03/ejemplo03/tablas2.py
Docstring:   Módulo para imprimir tablas de multiplicar en la pantalla.

In [3]: tablas2.tabla?
Signature: tablas2.tabla(n)
Docstring: Imprime la tabla N en la pantalla
File:      ~/dev/python-clases/sesion03/ejemplo03/tablas2.py
Type:      function

In [4]: tablas2.tabla(3)
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```
