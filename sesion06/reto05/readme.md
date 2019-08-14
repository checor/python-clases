## Reto final

`bedu_travels_api.py`

Crea un API sencilla en JSON para modificar una reservación utilizando Bottle y sus [verbos](https://bottlepy.org/docs/dev/api.html#bottle.Bottle.get), para agregar, quitar o editar elementos de una reservación, almacenada en un archivo CSV. Debe de contar con las siguientes direcciones:

* GET /productos: Muestra todos los prductos de la reservación, así como su total. 
* GET /producto/<num>: Muestra un producto en particular, identificado por número de linea.
* POST /producto: Agrega un nuevo producto a la reservación.
* DELETE /producto/<num>: Elimina un producto de la reservación.
* PUT /producto/<num>: Edita un producto existente. El producto debe existir.

El formato JSON que entregue o reciba debe de ser similar al utilizado en sesiones anteriores.