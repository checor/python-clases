## Ejemplo 01
### Manipulación de archivos

Los archivos en Python son objetos tipo *file* creados mediante la función *open* (abrir). Toma como parámetros una cadena con la ruta, y 2 opcionales, modo de acceso y tamaño de búfer.

`archivo_hola.py`
```python
In [1]: # Escribiendo un archivo 

In [2]: archivo = open("hola.txt", "w") # w para escritura

In [3]: archivo.write("Primer linea de este archivo\n")
Out[3]: 28

In [4]: archivo.writelines(["Multiples ", "Linea\n", "En ", "Lista"])

In [5]: archivo.close() # Debemos cerrar el archivo

In [6]: # Leyendo un archivo

In [7]: archivo = open("hola.txt", 'r')

In [8]: archivo.readline()  
Out[8]: 'Primer linea de este archivo\n'

In [9]: archivo.readlines()
Out[9]: ['Multiples Lineas\n', 'En Lista']
```

### El comando with

A pesar de que podemos utilizar archivos como el ejemplo anterior, se recomienda utilizar el comando *with*, que automaticamente cierra el archivo una vez dejemos de utilizar. Para ellos debemos indentar en un bloque su uso:

`hola_with.py`
```python
In [1]: with open("hola2.txt", 'w') as archivo: 
   ...:     archivo.write("Primer linea de este archivo\n") 
   ...:     archivo.writelines(['Multiples Lineas\n', 'En Lista']) 
   ...:
   
In [2]: with open("hola2.txt", 'r') as archivo: 
   ...:     print(archivo.readline()) 
   ...:     print(archivo.readlines()) 
   ...:      
   ...:
   
Primer linea de este archivo

['Multiples Lineas\n', 'En Lista']
```
