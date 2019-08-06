## Reto 04

`info_archivos2.py`

Mejora el código del reto anterior, mediante el uso de argumentos y excepciones.
* Si el usuario agrega un argumento, este será la carpeta a mostrar. Si no, mostrar carpeta actual.
* Con el argumento --json, mostrar resultados en json. Si no se agrega, en diccionario.
* El argumento --help deberá mostrar ayuda y salir inmediatamente.
* Capturar la excepción en caso de que la carpeta no exista e informar al usuario del error.
* Capturar la excepción en caso de que el argumento sea un archivo e informar al usuario del error.

```
$ python3 info_archivos2.py --help
Uso: info_archivos.py [PATH] [--json]

Path:   Carpeta a mostrar. Carpeta actual si no se coloca
--json: Imprime json. Diccionario si no se coloca.

$ python3 info_archivos2.py 
[{'tamanio': 1070, 'nombre': 'info_archivos2.py', 'fecha': 'Fri Aug  2 17:05:18 2019'}, {'tamanio': 566, 'nombre': 'readme.md', 'fecha': 'Fri Aug  2 17:01:57 2019'}]

$ python3 info_archivos2.py --json
[
    {
        "tamanio": 1070, 
        "nombre": "info_archivos2.py", 
        "fecha": "Fri Aug  2 17:05:18 2019"
    }, 
    {
        "tamanio": 566, 
        "nombre": "readme.md", 
        "fecha": "Fri Aug  2 17:01:57 2019"
    }
]

$ python3 info_archivos2.py readme.md 
El path corresponde a un archivo, no a un directorio.

$ python3 info_archivos2.py noexiste
Carpeta no existente!
```
