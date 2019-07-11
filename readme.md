# Python fundamentals

Bienvenido a Python! Python es un lenguaje de programación de alto nivel, fácil de usar, versátil y potente. Es uno de los lenguajes más populares actualmente según el ínidce de TIOBE:

## Objetivo

Conocer la sintaxis básica de Python, variables y tipos de datos; operadores lógicos y condiciones, así como ciclos de control.

## Usos

Python tiene diversos campos de aplicación:
 - Aplicaciones web (Flask, Django...)
 - Aplicaciones multiplataforma (PyQt, TCL, click..)
 - Aplicaciones móviles (Kivy)
 - Electrónica, IOT (Micropython)
 - Data science (Tensorflow, Scipy...)
 - Robótica (ROS)

## Instalación
La instalación dependerá del sistema operativo que tengamos. Para este curso, cualquier versión superior a Python 3.4 es válida para seguirlo.

### Windows

Descargar el instalador de la última versión de Python 3 desde https://python.org, y seguir las instrucciones del instalador. También puedes descargar [Ubuntu para Windows 10](https://www.microsoft.com/es-mx/p/ubuntu/9nblggh4msv6), y así tener un sistema Linux en tu equipo, accesible desde Windows.

### Linux
Python 3 ya se encuentra disponible en la mayoría de distribuciones Linux. Basta con instalar la herramienta `pip`, que utilizaremos más adelante, mediante el comando el consola (Debian y Ubuntu): `sudo apt-get install python3-pip`.

### Mac OS X
Para Mac, la forma de instalación recomendada es mediante *Homebrew*, un gestor de paquetes para Mac. Seguir las instrucciones de instalación en https://brew.sh, y posteriormente correr el comando `brew install python3`.

Una vez que tengamos instalado Python, podemos revisar que esté instalado correctamente mediante el comando:
```bash
$ python3 -V
Python 3.6.8
```
Ahora estamos listos para correr nuestro primer programa en Python.

## ¿Python 2 o Python 3?

Cuando Python 3 salió al mundo, en 2008, tuvo una serie de cambios que lo hacían incompatible con código escrito de Python 2, así como librerías. Esto hizo que su nivel de adopción fuera bajo comparado con su antecesor. Esto fue cambiando gradualmente con el paso de los años.

Actualmente, se recomienda utilizar Python 3 para todo nuevo proyectos, Python 2 dejará de tener soporte para 2020. En proyectos con Python 2, se debe contemplar una estrategia para migrar a Python 3.

## Hola Mundo
El ejercicio primerizo por defecto, en cualquier lenguaje, es escribir Hola Mundo en nuestra pantalla. En Python, basta con crear un archivo con el siguiente contenido:
`hola_mundo.py`
```python
print("Hola Mundo!")
```
Y lo ejecutamos de la siguiente manera:
```bash
$ python3 hola_mundo.py
Hola Mundo!
```

## iPython

iPython es una consola interactiva de Python, con mas funcionalidades que la consola que trae por defecto. Para instalarla, corremos el comando:

```bash
$ pip3 install ipython
Collecting ipython
[...]
Successfully installed ipython
```
Y la abrimos con ipython3:

```
$ ipython3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import this                                                                                                                                                                                                                                   
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
[...]
Namespaces are one honking great idea -- let's do more of those!

```

## Variables y tipos de datos

Para crear una variable, basta con asignarle el nombre que queramos, empezando por una letra. Python es un lenguaje de **tipado dinámico**, esto es, podemos asignarle cualquier tipo de dato a las variables.

### Datos numéricos
Pueden llevar cantidades enteras o decimales. Soportan operaciones aritméticas.

```python
In [1]: a = 5                                                                                                                                                                                

In [2]: b = 2.5                                                                                                                                                                              

In [3]: a + b                                                                                                                                                                                
Out[3]: 7.5

In [4]: a * b                                                                                                                                                                                
Out[4]: 12.5

In [5]: c = a - b                                                                                                                                                                            

In [6]: c                                                                                                                                                                                    
Out[6]: 2.5
```

#### Ejercicio: operaciones.py
Crea dos variables, y muestra en pantalla las operaciones básicas aritméticas entre ellos: Suma, resta, multiplicación, divisón.

```bash
$ python3 operaciones.py
5 + 9 = 10
5 - 9 = -4
5 * 9 = 45
5 / 9 = 0.5555555555555556
```
### Cadenas

Las cadenas son texto asignado a una variable. Deben estar encerrados en comillas simples, dobles, o tres comillas dobles seguidas. También podemos hacer ciertas operaciones con ellas.

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

```python
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
```python
In [21]: nombre = "Sergio"                                                                                                                                                                   

In [22]: "Hola mi nombre es {}".format(nombre)                                                                                                                                               
Out[22]: 'Hola mi nombre es Sergio'

In [23]: "{} * {} = {}".format(4, 4, 4*4)                                                                                                                                                    
Out[23]: '4 * 4 = 16'

```

#### Ejercicio:  tabla_multiplicar.py
Muestra en pantalla la tabla de multiplicar de algún numero del 1 al 9. Guarda el número de la tabla a mostrar en una variable, y utiliza la función *format* para mostar la tabla de una manera indicada.

```bash
# python3 tabla_multiplicar.py
TABLA DEL 4
------------
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
------------
```

### Formato de cadenas
La función format tiene una gran cantidad de configuraciones para insertar nuestros datos en una cadena. Podemos conocer mas a fondo su funcionamiento en la página https://pyformat.info


#### Ejercicio: reservacion.py

Imprimir un ejemplo de una reservación en Bedu Travels, incluyendo 5 elementos a mostrar con precio. Utilizar format para mostrarlo en forma de tabla.

```
-----------------------------------------------------------------
RESERVACION                                        | PRECIO    
-----------------------------------------------------------------
Habitación doble                                   |  150000.00
Transporte                                         |   13000.00
Reservación en evento                              |    3999.99
Tour en lancha                                     |   21750.00
Alimentos y bebidas                                |    5000.00
-----------------------------------------------------------------
```

### Operadores lógicos
Los operadores lógicos permiten manipular variables booleanas (verdadero/falso).

#### Ejemplo: tabla_verdad_and.py

#### Ejercicio: tabla_verdad_or.py

## Estruturas de control

### If, elif, else
Permite ejecutar cierta porción de código, si es que una condición se evalúa como verdadero.
Elif, permite probar otra condición, en caso de no cumplirse la anterior. Else, ejecuta una pieza de código, si ninguna condición se cumplió.

```python
In [1]: numero = 0                                                                                                                                                                           

In [2]: if numero == 0: 
   ...:     print("Este numero es 0") 
   ...: elif numero > 0: 
   ...:     print("Este numero es positivo") 
   ...: else: 
   ...:     print("Este numero es negativo") 
   ...:                                                                                                                                                                                      
Este numero es 0

```

### While
Ejecuta una pieza de código, en ciclos, hasta que la condición indicada se deje de cumplir.
```
In [5]: while n<5: 
   ...:     print("Numero {}".format(n)) 
   ...:     n = n + 1 
   ...:                                                                                                                                                                                      
Numero 0
Numero 1
Numero 2
Numero 3
Numero 4

```
### For
Itera sobre cada uno de los elementos que se le indiquen.
```
In [7]: for i in range(5): 
   ...:     print("Numero {}".format(i)) 
   ...:      
   ...:                                                                                                                                                                                      
Numero 0
Numero 1
Numero 2
Numero 3
Numero 4

```
#### Ejemplo: par_non.py
De una lista de 10 numeros, imprimir en pantalla par o non, dependiendo de si son divisibles entre 2 o no.

```python
In [8]: for i in range(10): 
   ...:     if i % 2 == 0: 
   ...:         print("Par") 
   ...:     else: 
   ...:         print("Non") 
   ...:   
   
Par
Non
Par
Non
Par
Non
Par
Non
Par
Non

```

#### Ejercicio: fizzbuzz.py

Muestra en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “Fizz” y, a su vez, los múltiplos de 5 por “Buzz”. Para los números que, al tiempo, son múltiplos de 3 y 5, utiliza el combinado “FizzBuzz”.

## Actividad final

Modificar el script lista_reservacion.py, para preguntar al usuario si quiere conocer o no el monto de apartado. Si escribe S, SI, si o sI, mostrar después del total, el precio del apartado.
