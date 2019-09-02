
## Partes de una araña

### URLs

Para definir las páginas iniciales a visitar, se entrega un iterable en el atributo `start_urls`, o bien, mediante la función `start_requests`.

```python
start_urls = [
    'http://paginaprincipal.com/',
]
```

### Parse

Esta función indica cómo obtener la información relevante. Con `yield`, se puede entregar datos en forma de diccionario, y después, opcionalmente utilizar `response.follow`, para continuar navegando.

```python
yield {
    'text': elemento.selector,

}

yield response.follow(siguiente_pagina, parser)
```
### Selector

Los selectores son la herramienta para hacer scrap de los datos. Scrapy cuenta con su propia herramienta basada en la herramienta parsel, pero se puede utilizar cualquier otra, como Beautiful Soup, sin problemas.


`selectores.py`
```python
In [1]: from scrapy.selector import Selector

In [2]: body = '<html><body><span>good</span></body></html>'

In [3]: Selector(text=body).xpath('//span/text()') # Texto de elementos span
Out[3]: 'good'

In [4]: Selector(text=body).css('span::text') # Mediante CSS
Out[4]: 'good'
```

##  Scrapy Shell

Para probar el funcionamiento en un intérprete, se recomienda utiliza scrapy shell, incluido en con el módulo, con el comando `scrapy shell <url o archivo>`.

`scrapy shell ./piramide.html`

```python
In [1]: response.xpath('//title/text()').get() # Título del documento
Out[1]: 'Example website'

In [2]: # get() obtiene 1 elemento, getall obtiene todos en una lista

In [3]: response.xpath('//title/text()').getall()
Out[3]: ['Eco Pyramid']

In [4]: # Se pueden colocar entre corchetes un filtro de elementos

In [4]: response.xpath('//div[@class="name"]').get()
Out[4]: '<div class="name">plants</div>'

In [5]: # Se puede recorrer el árbol de elementos de diferentes maneras

In [6]: response.xpath('//div[@class="ecopyramid"]/ul/li').get() # Hacia adentro
Out[6]: '<li class="producerlist">\n                <div class="name">plants</div>\n                <div class="number">100000</div>\n            </li>'

In [7]: response.xpath('//div[@class="name"]/..').get() # Hacia afuera
Out[7]: '<li class="producerlist">\n                <div class="name">plants</div>\n                <div class="number">100000</div>\n            </li>'

In [8]: response.xpath('//div[@class="name"]/following-sibling::*').get() # Hacia los lados
Out[8]: '<div class="number">100000</div>'

In [9]: # CSS utiliza selectores de estilo, puede conbinarse con xpath

In [10]: response.css('li').xpath("@class").getall() # Clase de todos los elementos li
Out[10]: 
['producerlist',
 'producerlist',
  ...
 'tertiaryconsumerlist']

In [11]: # .attrib también se puede utilizar para elegir atributos, pero solo con 1 elemento

In [12]: response.css('li').attrib['class']
Out[12]: 'producerlist'

```

`spider_piramide.py`

Utilizar Scrapy para crear una araña que obtenga toda la información de la pirámide ecológica en el siguiente formato:

```json
{
    "name": "fox",
    "number": 100,
    "type": "secondaryconsumers",
}
```

