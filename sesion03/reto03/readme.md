## Reto 04

`archivos.py`

De forma similar al ejemplo anterior, modifica `lista_de_archivos.py`, para que se pueda utilizar como módulo o como archivo independiente. Agrega docstrings para indicar al usuario final como utilizarlo.


```python
$ python3 archivos.py 
--------------------------------------------------------------------------------
NOMBRE                             TAMAÑO                                  FECHA
--------------------------------------------------------------------------------
readme.md                            235                Fri Jul 19 16:39:13 2019
archivos.py                          766                Fri Jul 19 16:42:51 2019
__pycache__                         4096                Fri Jul 19 16:42:59 2019
--------------------------------------------------------------------------------
$ ipython3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import archivos

In [2]: archivos?
Type:        module
String form: <module 'archivos' from '/home/sergio/dev/python-clases/sesion03/reto03/archivos.py'>
File:        ~/dev/python-clases/sesion03/reto03/archivos.py
Docstring:   Móudlo para mostrar una lista de archivos, con fecha y tamaño

In [3]: archivos.archivos?
Signature: archivos.archivos(path='.')
Docstring: Muestra la lista de archivos en el path, por defecto en la carpeta de trabajo
File:      ~/dev/python-clases/sesion03/reto03/archivos.py
Type:      function

In [6]: archivos.archivos()
--------------------------------------------------------------------------------
NOMBRE                             TAMAÑO                                  FECHA
--------------------------------------------------------------------------------
readme.md                            235                Fri Jul 19 16:39:13 2019
archivos.py                          765                Fri Jul 19 16:46:43 2019
__pycache__                         4096                Fri Jul 19 16:46:51 2019
--------------------------------------------------------------------------------

```