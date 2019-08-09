## Ejemplo 01

La programación orientada a objetos (POO) es un paradigma de programación basado en el mundo real. Las partes básicas son clases y objetos, así como su interacción entre ellas en nuestro programa.

### Clases y objetos

Para entender este paradigma debemos conocer la diferencia entre clase y objeto.

Una clase es la definición genérica a partir de la cual se elaboran objetos.

Un objeto es una instancia de una clase. Entre ellas, sus atributos pueden ser tener diferentes valores.

[Clase y objetos](./clase_objetos.jpg)

### Definición de una clase

Crear una clase llamada Animal con los siguientes elementos, y 3 objetos animales a partir de ella.

[Clase Animal](./clase_animal.png)

`animales.py`

```python
class Animal():
    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido
    
    def grito(self):
        print("El {} hace {}".format(self.nombre, self.sonido))
    
    def info(self):
        print("Nombre: {} - Especie {}".format(self.nombre, self.especie))

In [1]: class Animal(): 
   ...:     def __init__(self, nombre, especie, sonido): 
   ...:         self.nombre = nombre 
   ...:         self.especie = especie 
   ...:         self.sonido = sonido 
   ...:      
   ...:     def grito(self): 
   ...:         print("El {} hace {}".format(self.nombre, self.sonido)) 
   ...:      
   ...:     def info(self): 
   ...:         print("Nombre: {} - Especie {}".format(self.nombre, self.especie)) 
   ...: 
   
In [2]: gato = Animal("Gato", "Felino", "Miau")

In [3]: perro = Animal("Perro", "Canino", "Guau")

In [4]: cerdo = Animal("Cerdo", "Porcino", "Oink")

In [5]: gato.grito()  # Metodo
El Gato hace Miau

In [6]: perro.nombre  # Atributo
Out[6]: 'Perro'

In [7]: cerdo.info()
Nombre: Cerdo - Especie Porcino
```

## Métodos integrados

Todas las clases en Python 3 cuentan con ciertos métodos integrados, que sirven de apoyo y mejor uso de los objetos. Algunas importantes son:

`__init__` - Llamada al crear un objeto.
`__del__` - Llamada a punto de destruir un objeto.
`__str__` - Representación en string de un objeto.
`__bool__` - Para evaluar el objeto como booleano.

`clase_str.py`

```python
class MiClase():
    def __init__(self):
        print("Clase creada")
    
    def __del__(self):
        print("Clase borrada")
    
    def __str__(self):
        return "Mi propio objeto"

In [1]: class MiClase(): 
   ...:     def __init__(self): 
   ...:         print("Clase creada") 
   ...:      
   ...:     def __del__(self): 
   ...:         print("Clase borrada") 
   ...:      
   ...:     def __str__(self): 
   ...:         return "Mi propia objeto" 
   ...:
   
In [2]: a = MiClase()
Clase creada

In [3]: str(a)
Out[3]: 'Mi propia clase'

In [4]: del a
Clase borrada
```
