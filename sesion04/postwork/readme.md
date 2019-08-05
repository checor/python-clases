## Postwork

## Objetivos

Dividir datos del código en el proyecto, de tal forma que no existan datos colocados directamente en el código fuente. Para eso, podemos utilizar desde archivos de texto, valores separados por comma o JSON. Así también utilizar las excepciones para evitar cierres inesperados de la aplicación.

# Requisitos
* Contar con Python 3 instalado

## Instrucciones

* Si no terminaste alguno de los retos que se realizó durante la sesión 3, termínalos.
* Comienza a localizar secciones de tu proyecto las cuales utilizen datos para funcionar.
  * ¿Qué estructura se acopla mejor a tu proyecto? Define tipos de archivos y localización. Separa el código de tus datos.
  * ¿Qué hacer si no se encuentra ese archivo, o está corrupto? Usa excepciones para definir como proceder ante esos casos.
* Revisa que otras partes del código es propensa a errores, y agrega manejo de excepciones. Toma en cuenta que a nivel mas granular, mejor. No es reocmendable que un try-catch capture todo el programa.
* Agrega argumentos a tus scripts, si es necesario. Usalos por ejemplo para:
  * Mostrar ayuda al usuario de tu programa
  * Cambiar localización de un archivo de se va a leer o escribir
  * Agregar diferentes funciones dependiendo la necesidad
* Sube a Github tus cambios para revisión.
