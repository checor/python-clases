## Ejemplo 01

### Módulos y paquetes

Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar grandes códigos. Un paquete, por su parte, es una carpeta que contiene varios módulos.

Python, es un lenguaje con "baterías incluidas", esto quiere decir que incluye una buena cantidad de módulos consigo, para hacer las tareas mas cómunes con su instalación base.

`modulos.py`
```python
In [1]: # Importando algun modulo  

In [2]: import os 

In [3]: # Obteniendo ayuda

In [4]: help(os)

In [5]: # Lista de archivos

In [6]: os.listdir()
Out[6]: 
['sesion03',
 'manage.py',
 'sesion01',
 'sesion02',
 '.gitignore',
 '.git',
 '.vscode']

In [7]: # Obteniendo el tamaño de un archivo    

In [8]: os.path.getsize('manage.py')

Out[8]: 630

In [10]: # Otras maneras de importar modulos

In [11]: import os.path # Solo algun submodulo, llamando os.path

In [12]: from os import path # Similar, se llama path directamente
```


`lista_de_archivos.py`

Mostar en pantalla una lista de archivos en el directorio actual.

```
----------------------------------------
lista_de_archivos.py...............  135
readme.md.......................... 1141
modulos.py.........................  412
----------------------------------------
```
