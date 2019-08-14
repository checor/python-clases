## Ejemplo 03

### JSON con Bottle

Una de los formatos habituales de un API es recibir y enviar información en formato JSON, el cual es soportado por Bottle.py. Para hacer uso del mismo, basta con enviar un diccionario con la información.

`json_bottle.py`

### Ficheros

Para permitir a un usuario descargar archivos, se pueden enviar archivos en Bottle.py de manera similar a como se leen archivos en Python. Cualquier clase que tenga la función `read()`, puede enviarse como archivo.

`archivo_bottle.py`