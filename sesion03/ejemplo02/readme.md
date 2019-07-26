## Librería estándar

La libería estándar ofrece una cantidad de objetos y funciones, algunos escritos en C, otros en Python. Posee desde interación del sistema operativo (os), fechas (datetime), hasta un pequeño servidor web!

https://docs.python.org/3/library/


## Fechas en python

Python tiene el módulo *datetime* para poder representar fechas y horas. Se recomienda revisar su ayuda y documentación para conocer más acerca del mismo.

`fechas.py`

```python
In [1]: from datetime import datetime

In [2]: help(datetime)

In [3]: datetime.now()
Out[3]: datetime.datetime(2019, 7, 18, 23, 4, 15, 829545)

In [4]: datetime(2019, 7, 10)
Out[4]: datetime.datetime(2019, 7, 10, 0, 0)

In [5]: import os

In [6]: os.path.getmtime("readme.md")  # Fecha de modificacion, estilo C
Out[6]: 1563507793.7691352

In [7]: datetime.fromtimestamp(1563507793.7691352)
Out[7]: datetime.datetime(2019, 7, 18, 22, 43, 13, 769135)
```

