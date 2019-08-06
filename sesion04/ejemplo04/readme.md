## Ejemplo 04

### Argumentos

Cuando un script es invocado, puede llevar una cantidad variable de argumentos, intrepretados como texto, por ejemplo: `git status` invoca el comando `git` con el argumento `status`.

En Python, podemos acceder a los argumentos mediante `sys.argv`

`argumentos.py`

```python
import sys

for arg in sys.argv:
    print(arg)
```
El cual, al ser llamado con argumentos, lo podremos visualizar en pantalla:

```
$ python argumentos.py estos son mis argumentos
argumentos.py
estos
son
mis
argumentos
```

Nótese que siempre el primer argumento será cómo llamó el usuario el programa o script.


## Excepciones

Cuando nuestro programa falla en alguna parte, levanta una excepción y detiene la ejecución del programa. Las excepciones pueden controlarse mediante el uso de **try** y **except**.

`excepciones.py`

``` python
In [1]: a = int("10.5")  # Sin excepcion                                                                                                                        
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-0baa3ce627ce> in <module>
----> 1 a = int("10.5")  # Sin excepcion

ValueError: invalid literal for int() with base 10: '10.5'

In [2]: try: 
   ...:     a = int("10.5") 
   ...: except ValueError:
   ...:     print("10.5 no es entero") 
   ...:     a = 0 
   ...:                                                                                                                                                         
10.5 no es un entero
```

A **except** se le puede indicar que tipo de excepciones capturar. Esto es recomendable para evitar que si el programa falla por otra causa no esperada, aplicar una acción incorrecta. También se pueden utilizar múltiples excepts para un try.

`except_archivo.py`
```python
import os
import sys

try:
    print(os.listdir(sys.argv[1]))
except FileNotFoundError:
    print("Error: Folder no existente")
except Exception as e:  # Se captura la excepción en una variable
    print("Error: {}".format(e))
```

```
$ python3 excpet_archivo.py folder_no_existente
Error: Folder no existente

$ python3 except_archivo.py .
['except_archivo.py', 'readme.md', 'argumentos.py']
```
