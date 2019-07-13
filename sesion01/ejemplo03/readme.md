### Cadenas

Las cadenas son texto asignado a una variable. Deben estar encerrados en comillas simples, dobles, o tres comillas dobles seguidas. También podemos hacer ciertas operaciones con ellas.

`cadenas.py`
```python
In [8]: # Esto es una cadena                                                                                                                                                                 

In [9]: d = "Hola mundo"                                                                                                                                                                     

In [10]: # Podemos comprobar el dato con type()                                                                                                                                              

In [11]: type(d)                                                                                                                                                                             
Out[11]: str

In [12]: # Podemos utilizar comillas simples, o tres comillas dobles                                                                                                                         

In [13]: e = 'Saludos'                                                                                                                                                                       

In [14]: f = """What's your name?"""                                                                                                                                                         

In [15]: # Operaciones con cadenas                                                                                                                                                           

In [16]: "Hola" * 5                                                                                                                                                                          
Out[16]: 'HolaHolaHolaHolaHola'

In [17]: "Hola" + " Mundo"                                                                                                                                                                   
Out[17]: 'Hola Mundo'

```
Python no convierte automáticamente tipos de datos, por lo cual, no podemos hacer una suma desde con un numero entero y una cadena. Esto lo hace un lenguaje **fuertemente tipado**. Podemos convertir datos utilizando con el nombre del tipo de dato, y el dato entre paréntesis.

```
In [18]: 5 + "5"                                                                                                                                                                             
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-b265071c056c> in <module>
----> 1 5 + "5"

TypeError: unsupported operand type(s) for +: 'int' and 'str'

In [19]: 5 + int("5")                                                                                                                                                                        
Out[19]: 10

In [20]: str(5) + "5"                                                                                                                                                                        
Out[20]: '55'

```
Podemos asignarle variables a una cadena, mediante la función *format()*. Esta convierte los datos a *string*, para posteriormente, ingresarlos en la cadena.
Para la entrada de texto por parte del usuario, podremos utilizar input(), con una cadena a mostrar como argumento.
`formato.py`
```python
In [21]: nombre = input("Cual es tu nombre? ")
Cual es tu nombre? Sergio                                                                                                                                                                

In [22]: "Hola mi nombre es {}".format(nombre)                                                                                                                                               
Out[22]: 'Hola mi nombre es Sergio'

In [23]: "{} * {} = {}".format(4, 4, 4*4)                                                                                                                                                    
Out[23]: '4 * 4 = 16'

```

### Formato de cadenas
La función format tiene una gran cantidad de configuraciones para insertar nuestros datos en una cadena. Podemos conocer mas a fondo su funcionamiento en la página https://pyformat.info