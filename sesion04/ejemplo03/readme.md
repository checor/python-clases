## Ejemplo 03

### Json

JSON (JavaScript Object Notation), es un formato basado en texto, utilizado para transmitir y almacenar información estruturada. Es muy utilizado en diversas herramientas web. Guarda cierta similitud con los diccionarios de Python.


`ejemplo_json.py`
```python
In [1]: import json

In [2]: mi_dic = {"nombre": "Armando", 
   ...:           "apellido": "Armada", 
   ...:           "lista": [1,2,3,4]}

In [3]: json.dumps(mi_dic)  # Conviertelo a string JSON
Out[3]: '{"nombre": "Armando", "apellido": "Armada", "lista": [1, 2, 3, 4]}'

In [4]: mi_json = """{"nombre": "Caballero", "apellido": "Caballo", "lista": [5,6,7,8]}"""

In [5]: json.loads(mi_json) # De string JSON a diccionario

In [6]: mi_json = """{"nombre": "Caballero", "apellido": "Caballo", "lista": [5,6,7,8]}""" 

In [7]: dic = json.loads(mi_json) # De string JSON a diccionario
Out[7]: {'nombre': 'Caballero', 'apellido': 'Caballo', 'lista': [5, 6, 7, 8]}

In [8]: dic['nombre']
Out[7]: 'Caballero'
```

### Elementos similares en JSON y diccionarios

Los elementos de un diccionario de Python, son convertidos al tipo de dato mas cercano en JavaScript, y viceversa.

[Equivalencias](./elementos.png)

### Archivos JSON

La 's' en los comandos de json (load**s** y dump**s**), indican que se trata de un string. También podemos manejar archivos mediante *load* y *dumps*

`ejemplo_json_archivo.py`
```python
In [1]: import json 

In [2]: with open("ejemplo.json", "w") as fjson: # Guardarlo como archivo
   ...:     mi_dicc = {"nombre": "diccionario", "year": 2019} 
   ...:     json.dump(mi_dicc, fjson, indent=4)  
   ...:      
   ...:

In [3]: !cat ejemplo.json    
{
    "nombre": "diccionario",
    "year": 2019
}

In [4]: with open("ejemplo2.json", "w") as fjson: 
   ...:     mi_dicc = {"fecha": datetime.now().strftime("%c")} # Las fechas necesitan convertirse 
   ...:     json.dump(mi_dicc, fjson, indent=4)  # Puede agregarse indentación
   ...: 

In [5]: with open("ejemplo2.json", 'r') as fjson: 
   ...:     mi_json = json.load(fjson) 
   ...:     print(mi_json) 
   ...:                                                                                                                                                         
{'fecha': 'Fri Aug  2 00:25:46 2019'}

```