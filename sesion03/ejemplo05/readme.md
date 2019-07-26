## Ejemplo 05

### Paquetes en Python

Son directorios que contienes más módulos o paquetes. La única diferencia entre un paquete y una directorio, es el archivo `__init__.py`, que indica la inicialización de un módulo.

`utilerias/__init__.py`

Para este ejemplo, vamos a crear la carpeta utilerias y dentro su archivo `__init__.py`.

```python
In [1]: import utilerias

In [2]: utilerias?
Type:        module
String form: <module 'utilerias' from '/home/sergio/dev/python-clases/sesion03/ejemplo04/utilerias/__init__.py'>
File:        ~/dev/python-clases/sesion03/ejemplo04/utilerias/__init__.py
Docstring:   Conjunto de modúlo que resuelve pequeñas tareas
```

Si colocamos los módulos realizados anteriormente, se podrán utilizar, de la siguiente manera:

```
$ tree utilerias
utilerias/
├── archivos.py
├── __init__.py
├── mi_primer_modulo.py
└── tablas.py
```

```python
In [1]: import utilerias

In [2]: utilerias.archivos  # Los submodulo no se importan por defecto
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-2-93e3b4b725b7> in <module>()
----> 1 utilerias.archivos

AttributeError: module 'utilerias' has no attribute 'archivos'

In [3]: import utilerias.archivos # Modo 1

In [4]: from utilerias import tablas # Modo 2

In [5]: utilerias.archivos?
Type:        module
String form: <module 'utilerias.archivos' from '/home/sergio/dev/python-clases/sesion03/ejemplo04/utilerias/archivos.py'>
File:        ~/dev/python-clases/sesion03/ejemplo04/utilerias/archivos.py
Docstring:   Móudlo para mostrar una lista de archivos, con fecha y tamaño

In [6]: tablas?
Type:        module
String form: <module 'utilerias.tablas' from '/home/sergio/dev/python-clases/sesion03/ejemplo04/utilerias/tablas.py'>
File:        ~/dev/python-clases/sesion03/ejemplo04/utilerias/tablas.py
Docstring:   <no docstring>

In [7]: 
```
