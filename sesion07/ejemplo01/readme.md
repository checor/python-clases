## Introducción

Web scrapping es una técnica para obtener información de sitios web, con el proósito de convertirlos en información útil y esto sean almacenados en alguna base de datoso o mostrados directamente al usuario.

## Beautiful Soup

Beautiful Soup 4 es una librería de Python útil para extraer contenido de páginas web. No maneja en si peticiones web, por lo tanto, se usará junto con requests.

### Instalación

Basta con instalar la herramienta mediante el uso de pip.

``` 
$ pip install beautifoulsoup4
$ pip install requests
```

### Objeto BeautifulSoup

Un objeto BeautifulSoup es el putno de partida de cualquier proyecto de scraping con la librería. Representa un archivo HTML o XML, del cual se puede navegar en el y encontrar los datos relevantes.

`google_soup.py`

Utilizar BeautifulSoup para obtener el título y las imágenes que contenga, de la página principal de Google. El contendio de la página se debe de obtener mediante la librería requests.

```python
In [1]: from bs4 import BeautifulSoup                        

In [2]: import requests

In [3]: response = requests.get("http://www.google.com")

In [4]: response.status_code        
Out[4]: 200

In [5]: soup = BeautifulSoup(response.content)  

In [6]: soup.title  # Titulo de la página
Out[6]: <title>Google</title>

In [7]: soup.title.string # Texto de cualquier elemento
Out[7]: Google

In [8]: soup.find_all("img")  # Encuentra todas las imágenes

Out[8]: [<img alt="Google" height="92" id="hplogo" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272"/>]

```

Invitar al alumno a realizar el ejemplo con su página favorita.


### Tipos de objetos

BS transforma un documento HTML, que puede provenir de la web o de un archivo, en un árbol de objetos de Python. Esto objetos puede ser: *Tag*, *NavigableString* y *Comment*.

`objetos_soup.py`

```python
In [1]: from bs4 import BeautifulSoup

In [2]: # TAG: Corresponde a un objeto HTML dentro del documento original

In [3]: soup = BeautifulSoup('<b class="bold" id="1">Saludos!</b>')

In [4]: tag = soup.p # Accediendo al tag <b> 

In [5]: type(tag)
Out[5]: bs4.element.Tag

In [6]: # El atributo name define el tipo de tag que es 

In [7]: tag.name = "blockquote" 

In [8]: tag
Out[8]: <blockquote class="bold" id="1">Saludos!</blockquote>

In [9]: tag["class"]  
Out[9]: ['bold']

In [10]: tag["id"] = "2" 

In [11]: tag
Out[11]: <blockquote class="bold" id="2">Saludos!</blockquote>
```

Para el caso de los comentarios y texto dentro o entre tags, se manejan de forma similar a un string de Python, con la diferencia que para cambiar su contenido, se utiliza el método `replace_with`.

`strings_soup.py`

```python
In [12]: # NavigableString es muy similar a un string de Python, sólo cambia como se reemplaza

In [13]: tag.string    
Out[13]: 'Saludos!'

In [14]: type(tag.string) 
Out[14]: bs4.element.NavigableString

In [15]: tag.string.replace_with("Bienvenidos!") 

In [16]: tag
Out[16]: <blockquote class="bold" id="2">Bienvenidos!</blockquote>

In [17]: soup = BeautifulSoup("<b><!--Yo soy un comentario HTML--></b>")

In [18]: soup.b.string
Out[18]: 'Yo soy un comentario HTML'

In [19]: type(soup.b.string)
Out[19]: bs4.element.Comment
```

### Encontrando elementos

El comando `find_all` sirve para encontrar todos las etiquetas dentro del documento. Para facilitar la búsqueda de elementos, BS tiene variedad de métodos, como los siguientes:

* find(): Encuentra un elemento de acuerdo al cursor donde se encuentre.
* find_all(): Entrega una lista de todos los elementos en el documento.
* find_parent(): Entrega el elemente padre inmediato.
* find_next_sibling(): Entrega el siguiente elemento, al mismo nivel de herencia.

Cualquiera se puede utilizar recursivamente.

`find_piramide.py`

Utilizar el HTML de ejemplo, piramide.html, para realizar las siguientes tareas.

1. Listar a los productores de la pirámide alimenticia.
2. El número total de todos los elementos.
3. El nombre de las clases padre del elemento con nombre Tigre.