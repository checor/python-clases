## Reto 03

Para el sistema de reservación, agrega una nueva clase llamada Hotel, que herede de producto, para incluir informacion extra acerce del mismo en la reservación. El subtotal, ahora será calculado por cantidad * precio * personas.

[Clase Hotel](./hotel.png)

Agregar la columna de Personas, e utilizar la función `isinstance`, para saber si es hotel o producto.

```
Desea conocer el apartado (si/no)?si
---------------------------------------------------------------
RESERVACION                     |CANTIDAD |PERSONAS |PRECIO   |SUBTOTAL 
Hotel Plus                      |        3|        2| 15000.00| 90000.00
Alimentos y bebidas             |        2|N/A      |  5000.00| 10000.00
Transporte                      |        2|N/A      |  3000.00|  6000.00
Tour en lancha                  |        1|N/A      |  2170.00|  2170.00
                                                        Total |108170.00
                                                     Apartado | 10817.00
```