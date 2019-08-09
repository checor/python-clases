## Ejemplo 04

### Polimorfismo

Se refiere a la habilidad de objetos de distintas clases a responder a un mismo mensaje. Puede ser mediante herencia o mediante clases diferentes, lo que se conoce en Python como *duck typying*: manejo de objetos sin definir la clase.

`poli.py`
```python
In [1]: class A: 
   ...:     def saludo(self): 
   ...:         print("Soy la primera clase, la A") 
   ...:                                                                                                                          

In [2]: class B: 
   ...:     def saludo(self): 
   ...:         print("Soy la segunda clase, la B") 
   ...:                                                                                                                          

In [3]: a = A() 
   ...: b = B()

In [4]: lista = [a, b]  # Clases distintas                                                                                 

In [5]: for objeto in lista: 
   ...:     objeto.saludo() 
   ...:
Soy la primera clase, la A
Soy la segunda clase, la B

```

`animales_tabla.py`

Con las clases creadas anteriormente: Animal y Ave, mostrar en pantalla sus atributos, mediante la función `__str__`.
Utilizar una misma función llamada `imprimir`, que funcione con ambos tipos de clases.

```
$ python3 animales_tabla.py 
NOMBRE         |ESPECIE        |SONIDO         |VUELA          
Perro          |Canis          |Guau           
Gato           |Felino         |Miau           
Paloma         |Columba        |Cucu           |True           
Gallo          |Gallus         |Kikiriki       |False
```
