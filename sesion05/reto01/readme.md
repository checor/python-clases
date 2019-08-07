## Reto 01

Para el sistema de reservación de Bedu Travels, crear una clase llamada Producto la cual contendrá los elementos clave para cada elemento de una reservacion. Cambiar la lista de diccionarios que tenía originalmente, por una lista de objetos.

[Clase Producto](./clase_producto.png)

La función subtotal, será calculada con base al precio por cantidad, como atributos. De la misma manera, IVA, dará el 16% del subtotal.

```
$ python3 main.py 
Desea conocer el apartado (si/no)?no
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PRECIO   |SUBTOTAL 
Habitacion doble                |        3|150000.00|450000.00
Alimentos y bebidas             |        2|  5000.00| 10000.00
Transporte                      |        2|  3000.00|  6000.00
Tour en lancha                  |        1|  2170.00|  2170.00                                                                   
                                              Total |468170.00

```