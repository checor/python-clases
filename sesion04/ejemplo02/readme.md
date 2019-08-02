## Ejemplo 02
## Módulo CSV

Los archivos csv están conformados con valores separados por una coma u otro símbolo, como si fueran un tabla.

El módulo csv cuenta con clases para facilitar leer y escribir archivos csv (*comma separated values*).
Funcionan de manera similar a los archivos, con conversión del archivo a listas y viceversa.

`archivo_csv.py`
```python
In [1]: import csv 

In [2]: with open("ejemplo.csv", 'w') as fcsv: # Creando archivo
   ...:     writer = csv.writer(fcsv) 
   ...:     writer.writerow(["Nombre", "Apellido", "Genero"]) 
   ...:     writer.writerow(["Nombre2", "Apellido2", "Genero2"]) 
   ...:     writer.writerow(["Nombre3", "Apellido3", "Genero3"]) 

In [3]: !cat ejemplo.csv  # Leer contenidos en linux                                                                                                                                 
Nombre,Apellido,Genero
Nombre2,Apellido2,Genero2
Nombre3,Apellido3,Genero3

In [4]: with open("ejemplo.csv", 'r') as fcsv: # Leer archivo
   ...:     reader = csv.reader(fcsv) 
   ...:     for row in reader: 
   ...:         print(row) # Tipo lista
   ...:                                                                                                                                                         
['Nombre', 'Apellido', 'Genero']
['Nombre2', 'Apellido2', 'Genero2']
['Nombre3', 'Apellido3', 'Genero3']
```

Aunque por defecto el CSV se maneja como listas, es posible que también se maneje como diccionarios, si la primera línea del CSV corresponde Es posible también elegir eal nombre de sus columnas

`archivo_csv_dict.py`

```python
In [1]: import csv

In [2]: with open("ejemplod.csv", 'w') as fcsv: 
   ...:     fields = ("Nombre", "Apellido", "Edad") 
   ...:     writer = csv.DictWriter(fcsv, fieldnames=fields)
   ...:     writer.writeheader() 
   ...:     writer.writerow({'Nombre': 'Pedro', 'Apellido': 'Picapiedra', 'Edad': 30}) 
   ...:     writer.writerow({'Nombre': 'Pablo', 'Apellido': 'Marmol', 'Edad': 29}) 

In [3]: !cat ejemplod.csv                                                                                                                                       
Nombre,Apellido,Edad
Pedro,Picapiedra,30
Pablo,Marmol,29

In [4]: with open("ejemplod.csv", 'r') as fcsv: 
   ...:     reader = csv.DictReader(fcsv) 
   ...:     for row in reader: 
   ...:         print(row['Nombre'], row['Apellido']) 
   ...:          
   ...:                                                                                                                                                        
Pedro Picapiedra
Pablo Marmol
```

## Datetime

Para almacenar y utilizar la fecha y hora, en Python tenemos el módulo datetime, y su clase del mismo nombre.

`fecha_hora.py`

```python
In [1]: from datetime import datetime

In [2]: datetime.now() # Fecha actual local
Out[2]: datetime.datetime(2019, 8, 1, 22, 34, 30, 594329)

In [3]: datetime.utcnow() # Fecha UTC
Out[3]: datetime.datetime(2019, 8, 2, 3, 34, 43, 241030)

In [4]: a = datetime(2019, 8, 2, 3, 12, 20) # Nueva fecha

In [5]: a.year # Elementos individuales
Out[5]: 2019

In [6]: a.month
Out[6]: 8

In [7]: a.day 
Out[7]: 2

In [8]: a.strftime("%Y-%m-%d %H:%M")  # Convertir a string
Out[8]: '2019-08-02 03:12'

In [9]: a.strftime("%d %B, %Y")
Out[9]: '02 August, 2019'

In [11]: b = datetime.strptime("2019-07-01 13:45", "%Y-%m-%d %H:%M") # De string a datetime
     
In [12]: b
Out[12]: datetime.datetime(2019, 7, 1, 13, 45)
```

Las fechas son inmutables, es decir, no se permite cambiar sus elementos directamente una vez que se crearon, pero se puede utilizar `timedelta`, que permite relizar operaciones con ellas.

```python
In [24]: a
Out[24]: datetime.datetime(2019, 8, 2, 3, 12, 20)

In [25]: a + timedelta(days=5) # Agrega 5 dias
Out[25]: datetime.datetime(2019, 8, 7, 3, 12, 20)

In [26]: a - timedelta(weeks=1) # Resta una semana
Out[26]: datetime.datetime(2019, 7, 26, 3, 12, 20)
```
