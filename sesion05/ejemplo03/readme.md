## Ejemplo 03

### Herencia

Proceso en el cual una clase, obtiene los atributos y métodos de otra(s), y opcionalmente extenderlos y cambiarlos. La nueva clase se conoce como hija y la otra como padre.

Representación de herencia:

[Clase Ave](./ave.png)

`herencia.py`

```python
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
  
In [2]: class Ave(Animal): 
   ...:     def __init__(self, nombre, especie, sonido, vuela=True): 
   ...:         super().__init__(nombre, especie, sonido)  # Extiende la clase 
   ...:         self.vuela = vuela 
   ...:  
   ...:     def volar(self): 
   ...:         if self.vuela: 
   ...:             print("{} se eleva en el aire".format(self.nombre)) 
   ...:         else: 
   ...:             print("{} aletea pero no vuela".format(self.nombre)) 
   ...:

In [3]: paloma = Ave("Paloma", "Columba", "Cucu", True) 

In [4]: paloma.info()
Nombre: Paloma - Especie Columba

In [5]: paloma.volar()
Paloma se eleva en el aire

In [6]: gallina = Ave("Gallina", "Gallus", "Kikiriki", False)

In [7]: gallina.volar()
Gallina aletea pero no vuela
```
