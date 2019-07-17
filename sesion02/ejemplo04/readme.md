## Ejemplo 04

### Diccionarios

Son objetos contenedores que contienen una llave (*key*), y un valor(*value*). Se accede a sus valores mediante el nombre de la llave, por lo cual se conoces como diccionarios.

`diccionarios.py`
```python
In [1]: # Creando diccionarios  

In [2]: d1 = {}

In [3]: d2 = dict() 

In [4]: type(d1) 
Out[4]: dict

In [5]: d3 = {"Calle": "Monte de las cruces", "Tel": "+555555501", "Ciudad": "Tijuana"} 

In [6]: d4 = {"Medicamento": "Paracetamol", "Dosis": 8}                          

In [7]: d3.keys() 
Out[7]: dict_keys(['Calle', 'Tel', 'Ciudad'])

In [8]: d4.values() 
Out[8]: dict_values(['Paracetamol', 8])

In [15]: for item, value in d3.items():  # Accediendo mediante for
    ...:     print(item, ":", value) 
    ...:                                   
Calle : Monte de las cruces
Tel : +555555501
Ciudad : Tijuana
```