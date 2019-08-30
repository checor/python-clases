## Ejemplo 02

### Navegación

En BS, la navegación permite moverse entre los difrentes nodos del HTML, como si de un árbol se tratase.

Se tienen los siguientes atributos para navegar entre los nodos:

* .content: Tiene una lista de todos los hijos de un nodo
* .children: Similar a content, pero es un generador, ideal para ciclos.
* .descendats: Regeresa todos los descendientes, no sólo los hijos.
* .parent: Entrega el padre de un elemento, si es que tiene.
* .parents: Entrega todos sus padres, en un generador.

Para navegar a los lados, se tienen los atributos `next_sibling` y `previous_sibling`.

`navegacion_piramide.py`

Utilizando úncamente la navegación para moverse entre elementos, enlistar la pirámide en orden, con su debida tabulación, y entregando nombre y número de cada elemento. No utilizar comandos de búsqueda.

```
$ python nvegacion_piramide.py
Producers
        -Plants: 100000
        -Algae: 100000
Primaryconsumers
        -Deer: 1000
        -Rabbit: 2000
Secondaryconsumers
        -Fox: 100
        -Bear: 100
Tertiaryconsumers
        -Lion: 80
        -Tiger: 50
```