
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


selectores.py
```python
In [1]: from scrapy.selector import Selector

In [2]: body = '<html><body><span>good</span></body></html>'

In [3]: Selector(text=body).xpath('//span/text()').get() # Texto de elementos span
Out[3]: 'good'

In [4]: Selector(text=body).css('span::text').get() # Mediante CSS
Out[4]: 'good'
```

## Shell
